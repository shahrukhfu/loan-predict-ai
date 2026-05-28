import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():
    print("--- 1. Data Preprocessing ---")
    # Load dataset
    df = pd.read_csv("train.csv")
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Check for missing values
    print("\nMissing values before imputation:")
    print(df.isnull().sum())

    # Separate numerical and categorical columns
    # Excluding Loan_ID as it is just an identifier, and Loan_Status as it is target
    feature_cols = [col for col in df.columns if col not in ['Loan_ID', 'Loan_Status']]
    
    numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

    print(f"\nNumerical columns identified: {numerical_cols}")
    print(f"Categorical columns identified: {categorical_cols}")

    # Impute missing values
    # Numerical: median
    for col in numerical_cols:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
    
    # Categorical: mode
    for col in categorical_cols:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)

    print("\nMissing values after imputation:")
    print(df.isnull().sum())

    # Encode categorical variables into numerical values
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
        print(f"Encoded '{col}': {dict(zip(le.classes_, le.transform(le.classes_)))}")

    # Encode target column Loan_Status
    le_target = LabelEncoder()
    df['Loan_Status'] = le_target.fit_transform(df['Loan_Status'])
    print(f"Encoded target 'Loan_Status': {dict(zip(le_target.classes_, le_target.transform(le_target.classes_)))}")

    # Split dataset into X and y
    X = df[numerical_cols + categorical_cols]
    y = df['Loan_Status']

    # Split into 80% train and 20% test
    # Using stratify=y to preserve class distributions
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\nTrain set shape: {X_train.shape}, Test set shape: {X_test.shape}")

    # Standardize features using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\n--- 2. Train Default KNN Model ---")
    # Train default KNN model (default n_neighbors is 5 in scikit-learn)
    knn_default = KNeighborsClassifier()
    knn_default.fit(X_train_scaled, y_train)
    y_pred_default = knn_default.predict(X_test_scaled)
    
    acc_default = accuracy_score(y_test, y_pred_default)
    cm_default = confusion_matrix(y_test, y_pred_default)
    
    print(f"Default KNN (k=5) Accuracy: {acc_default:.4f}")
    print("Default KNN Confusion Matrix:")
    print(cm_default)

    print("\n--- 3. Experiment with Different values of K ---")
    for k in [3, 5, 7]:
        knn_temp = KNeighborsClassifier(n_neighbors=k)
        knn_temp.fit(X_train_scaled, y_train)
        y_pred_temp = knn_temp.predict(X_test_scaled)
        acc_temp = accuracy_score(y_test, y_pred_temp)
        print(f"Accuracy for k={k}: {acc_temp:.4f}")

    print("\n--- 4. Hyperparameter Tuning ---")
    # Hyperparameter tuning for n_neighbors
    param_grid = {'n_neighbors': list(range(1, 31))}
    grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train_scaled, y_train)
    
    best_k = grid_search.best_params_['n_neighbors']
    print(f"Best parameter for n_neighbors: {best_k}")
    
    knn_tuned = grid_search.best_estimator_
    y_pred_tuned = knn_tuned.predict(X_test_scaled)
    
    acc_tuned = accuracy_score(y_test, y_pred_tuned)
    cm_tuned = confusion_matrix(y_test, y_pred_tuned)

    print(f"Tuned KNN (k={best_k}) Accuracy: {acc_tuned:.4f}")
    print("Tuned KNN Confusion Matrix:")
    print(cm_tuned)

    print("\n--- 5. Model Evaluation Metrics Summary ---")
    print(f"{'Metric':<25} | {'Default KNN (k=5)':<20} | {f'Tuned KNN (k={best_k})':<20}")
    print("-" * 73)
    print(f"{'Accuracy':<25} | {acc_default:<20.4f} | {acc_tuned:<20.4f}")
    print(f"{'Confusion Matrix':<25} | {str(cm_default.tolist()):<20} | {str(cm_tuned.tolist()):<20}")

    print("\nClassification Report (Default):")
    print(classification_report(y_test, y_pred_default, target_names=le_target.classes_))
    print("Classification Report (Tuned):")
    print(classification_report(y_test, y_pred_tuned, target_names=le_target.classes_))

    print("\n--- 6. Visualization ---")
    # Plot the Confusion Matrix for both models side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Default KNN heatmap
    sns.heatmap(cm_default, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=le_target.classes_, yticklabels=le_target.classes_)
    axes[0].set_title(f'Default KNN (k=5)\nAccuracy: {acc_default:.4f}', fontsize=14)
    axes[0].set_xlabel('Predicted Label', fontsize=12)
    axes[0].set_ylabel('True Label', fontsize=12)

    # Tuned KNN heatmap
    sns.heatmap(cm_tuned, annot=True, fmt='d', cmap='Greens', ax=axes[1],
                xticklabels=le_target.classes_, yticklabels=le_target.classes_)
    axes[1].set_title(f'Tuned KNN (k={best_k})\nAccuracy: {acc_tuned:.4f}', fontsize=14)
    axes[1].set_xlabel('Predicted Label', fontsize=12)
    axes[1].set_ylabel('True Label', fontsize=12)

    plt.tight_layout()
    output_image = "confusion_matrices.png"
    plt.savefig(output_image, dpi=300)
    print(f"Confusion matrix plot saved as: {output_image}")

if __name__ == "__main__":
    main()
