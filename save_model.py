import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

def main():
    print("Preprocessing and training the final KNN model...")
    # Load dataset
    df = pd.read_csv("train.csv")
    
    numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

    # Impute missing values
    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Encode categorical variables
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    le_target = LabelEncoder()
    df['Loan_Status'] = le_target.fit_transform(df['Loan_Status'])

    # Split dataset into X and y
    X = df[numerical_cols + categorical_cols]
    y = df['Loan_Status']

    # Split into 80% train and 20% test (same split as train_knn.py for reproducibility)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train tuned KNN (k=16)
    knn = KNeighborsClassifier(n_neighbors=16)
    knn.fit(X_train_scaled, y_train)
    
    # Check accuracy
    train_acc = knn.score(X_train_scaled, y_train)
    test_acc = knn.score(X_test_scaled, y_test)
    print(f"Train Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")

    # Save components using joblib
    artifacts = {
        'knn': knn,
        'scaler': scaler,
        'label_encoders': label_encoders,
        'le_target': le_target,
        'X_train_scaled': X_train_scaled,
        'X_train_original': X_train.copy(),  # unscaled features to display in UI
        'y_train': y_train.values,
        'numerical_cols': numerical_cols,
        'categorical_cols': categorical_cols
    }
    
    joblib.dump(artifacts, 'knn_model_assets.joblib')
    print("Successfully saved all model assets to 'knn_model_assets.joblib'.")

if __name__ == "__main__":
    main()
