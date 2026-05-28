import os
import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.decomposition import PCA

# Initialize FastAPI App
app = FastAPI(title="LendLogic KNN Predictor API", version="1.0")

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model assets
ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knn_model_assets.joblib")
if not os.path.exists(ASSETS_PATH):
    # Fallback to local dir check
    ASSETS_PATH = "knn_model_assets.joblib"

try:
    assets = joblib.load(ASSETS_PATH)
    knn = assets['knn']
    scaler = assets['scaler']
    label_encoders = assets['label_encoders']
    le_target = assets['le_target']
    X_train_scaled = assets['X_train_scaled']
    X_train_original = assets['X_train_original']
    y_train = assets['y_train']
    numerical_cols = assets['numerical_cols']
    categorical_cols = assets['categorical_cols']
    print("Model assets loaded successfully.")
except Exception as e:
    print(f"Error loading model assets: {e}")
    raise RuntimeError(f"Could not load model assets from {ASSETS_PATH}")

class PredictionRequest(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get("/")
def read_root():
    return {"message": "LendLogic KNN Predictor API is running."}

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # 1. Prepare raw input data dict
        input_data = {
            'ApplicantIncome': request.ApplicantIncome,
            'CoapplicantIncome': request.CoapplicantIncome,
            'LoanAmount': request.LoanAmount,
            'Loan_Amount_Term': request.Loan_Amount_Term,
            'Credit_History': request.Credit_History,
            'Gender': request.Gender,
            'Married': request.Married,
            'Dependents': request.Dependents,
            'Education': request.Education,
            'Self_Employed': request.Self_Employed,
            'Property_Area': request.Property_Area
        }
        
        # 2. Encode categorical inputs
        encoded_data = input_data.copy()
        for col in categorical_cols:
            val = input_data[col]
            le = label_encoders[col]
            # Handle potential unseen values gracefully
            if val not in le.classes_:
                # Use mode or default first class
                encoded_data[col] = 0
            else:
                encoded_data[col] = int(le.transform([val])[0])
        
        # 3. Create DataFrame with correct column order matching training features
        feature_order = [
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
            'Loan_Amount_Term', 'Credit_History', 'Gender', 
            'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area'
        ]
        df_input = pd.DataFrame([encoded_data])[feature_order]
        
        # 4. Scale inputs
        scaled_input = scaler.transform(df_input)
        
        # 5. Predict and predict_proba
        prediction_val = int(knn.predict(scaled_input)[0])
        probabilities = knn.predict_proba(scaled_input)[0]
        confidence = float(probabilities[prediction_val])
        
        prediction_label = le_target.inverse_transform([prediction_val])[0] # 'Y' or 'N'
        
        # 6. Find Nearest Neighbors
        # Find 5 nearest neighbors
        distances, indices = knn.kneighbors(scaled_input, n_neighbors=5)
        distances = distances[0].tolist()
        indices = indices[0].tolist()
        
        # Extract neighbor data
        neighbors_original = X_train_original.iloc[indices]
        neighbors_scaled = X_train_scaled[indices]
        neighbors_targets = y_train[indices]
        
        # 7. Use PCA to project query point and its 5 neighbors to 2D coordinates for UI mapping
        points_to_project = np.vstack([scaled_input, neighbors_scaled]) # Shape: (6, 11)
        pca = PCA(n_components=2)
        projected = pca.fit_transform(points_to_project) # Shape: (6, 2)
        
        # Normalize coordinates to a comfortable display grid (-80 to 80 to fit inside UI container)
        max_val = np.max(np.abs(projected)) if np.max(np.abs(projected)) > 0 else 1.0
        coords_2d = (projected / max_val * 70).tolist()
        
        query_coord = coords_2d[0] # [x, y]
        neighbors_coords = coords_2d[1:] # list of 5 [x, y] coordinates
        
        # Prepare list of neighbors
        neighbors_list = []
        for i, idx in enumerate(indices):
            row = neighbors_original.iloc[i]
            target_val = int(neighbors_targets[i])
            target_label = "Approved" if target_val == 1 else "Denied"
            
            # Map encoded features back to strings for readable UI representation
            decoded_row = {}
            for col in row.index:
                if col in categorical_cols:
                    le = label_encoders[col]
                    decoded_row[col] = le.classes_[int(row[col])]
                else:
                    decoded_row[col] = float(row[col])
            
            neighbors_list.append({
                "id": f"LP-{1000 + int(idx)}",
                "distance": float(distances[i]),
                "status": target_label,
                "x": float(neighbors_coords[i][0]),
                "y": float(neighbors_coords[i][1]),
                "details": decoded_row
            })
            
        # 8. Compile response
        result = {
            "prediction": "Approved" if prediction_label == "Y" else "Denied",
            "confidence": confidence,
            "decision_vector_id": f"#LP-{np.random.randint(1000, 9999)}-XJ",
            "query_coord": {
                "x": float(query_coord[0]),
                "y": float(query_coord[1])
            },
            "neighbors": neighbors_list,
            "metrics": {
                "ApplicantIncome": float(request.ApplicantIncome),
                "LoanAmount": float(request.LoanAmount),
                "Credit_History": float(request.Credit_History)
            }
        }
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
