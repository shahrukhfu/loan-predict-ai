# LoanPredict AI 🤖✨

> Precision lending workflow powered by a hyperparameter-tuned K-Nearest Neighbors (KNN) architecture.

[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2015-c0c1ff?style=for-the-badge&logo=nextdotjs&logoColor=black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-4edea3?style=for-the-badge&logo=fastapi&logoColor=black)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-8083ff?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Tailwind CSS](https://img.shields.io/badge/Design-Tailwind%20v4-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

---

## 🌟 Key Features

*   **Real-time Risk Scoring:** Instantly calculates loan approval metrics (Approved/Denied) with confidence score dial.
*   **Explainable AI (XAI) Neighbors Map:** Projects multidimensional feature data into 2D coordinates using **Principal Component Analysis (PCA)**. Displays the 5 closest historical training samples with custom tooltip details.
*   **Harmonious Glassmorphic Interface:** Replicates a dark-mode command center layout with micro-interactions, responsive grids, and canvas neural-particle animations.
*   **Hyperparameter-Tuned Model:** Optimized classifier set to $k=16$ (imputed median/modes, standardized features, 80/20 stratified split) yielding **85.37%** validation accuracy.

---

## 📂 Project Architecture

```text
├── backend/                  # FastAPI Application
│   ├── main.py               # REST API endpoints & PCA projection
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Next.js Application
│   ├── src/
│   │   └── app/
│   │       ├── globals.css   # Custom styling & animations
│   │       ├── layout.tsx    # Layout definitions & Google Fonts
│   │       └── page.tsx      # Form, SVG Map, Dashboard logic
│   └── package.json          # Node dependencies
├── train.csv                 # Kaggle Loan Prediction Dataset
├── train_knn.py              # Initial training & evaluation script
├── save_model.py             # Pipeline serialization script
└── knn_model_assets.joblib   # Serialized model, scaler, and training data
```

---

## ⚡ Quick Start

### 1. Backend Server Setup

Ensure you have Python 3.10+ installed:

```bash
# Install backend dependencies
pip install -r backend/requirements.txt

# Run the final model serialization (creates knn_model_assets.joblib)
python save_model.py

# Start the FastAPI server (running on http://127.0.0.1:8000)
python -m uvicorn backend.main:app --reload --port 8000
```

### 2. Frontend Next.js Setup

Make sure you have Node.js installed:

```bash
# Navigate to the frontend folder
cd frontend

# Install packages
npm install

# Start the Next.js development server (running on http://localhost:3000)
npm run dev
```

---

## 📊 KNN Algorithm Metrics

*   **Accuracy (Default k=5):** 84.55%
*   **Accuracy (Tuned k=16):** **85.37%**
*   **False Negatives (Approved category):** Reduced to only $1$ instance out of $85$ test files (99% recall).

---

## 🔒 Security Configuration

*   **AES-256** mock encryption status indicators.
*   Secure cors middleware enabled for institutional frontend connection.
*   SOC2 Type II / GDPR compliance layouts included.
