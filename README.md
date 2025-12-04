![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-in_progress-orange)
![License](https://img.shields.io/badge/license-MIT-green)

# **FPS — Fraud Prediction System**

### **FPS (Fraud Prediction System)** is an AI-driven project designed to identify and classify addresses based on their fraud risk level (legit, phishing, scam, exploit).

The system relies on:

-   on-chain data analysis
-   behavioral feature extraction
-   classical Machine Learning models
-   an AI-Driven Development (AIDD) methodology
-   a modular architecture designed to evolve toward Deep Learning (GNN)

---

## 🎯 **Project Goal**

Provide an end-to-end pipeline able to:

1.  load and preprocess on-chain datasets
2.  extract and select relevant behavioral features
3.  train multiple ML models
4.  evaluate their performance
5.  predict the fraud category of any Ethereum address

---

## 🧱 **Repository Structure**

```
fps/
├── data/               → raw & processed datasets
│ ├── raw/
│ └── processed/
├── notebooks/          → exploration & prototyping notebooks
├── src/                → production-grade source code
│ ├── config/           → dataset registry & project configuration
│ │ └── datasets.py     → dataset declarations (paths/URLs + formats)
│ ├── data/             → generic dataset loader & preprocessing utilities
│ ├── features/         → feature engineering utilities
│ ├── models/           → training, evaluation & inference
│ ├── rules/            → ML rules & AIDD development rules
│ └── web3/             → on-chain data fetching & utilities
├── evaluation/         → reports, plots & metrics
└── requirements.txt    → Python dependencies
```

---

## 📦 **Dataset**

The project is dataset-agnostic: no dataset is bundled or automatically downloaded. You can plug in any tabular fraud dataset that describes entities (wallets, addresses, accounts) and their labels.

Data must live locally or be reachable from an HTTP/HTTPS URL (CSV, Parquet or JSON) and then be declared through the configuration described below.

---

## 🗂️ **Dataset configuration and loading**

Declare your datasets inside `src/config/datasets.py`. Example:

```
DATASETS = {
    "demo_fraud": DatasetConfig(
        key="demo_fraud",
        source="data/raw/demo_fraud.csv", # placeholder path
        file_format="csv",
        description="Example dataset configuration. Replace with your own dataset file.",
    ),
}
```
Note: `data/raw/demo_fraud.csv` is not included. Replace this path with your own dataset file.

Then use the generic loader:

```
from src.data.loader import load_raw_dataset

# Default dataset (DEFAULT_DATASET_KEY)
df = load_raw_dataset()

# Named dataset
df = load_raw_dataset("demo_fraud")

# Ad-hoc dataset (bypassing the registry)
df = load_raw_dataset(
    source="https://example.com/my_fraud_dataset.parquet",
    file_format="parquet",
)
```

Datasets are not versioned with the repository. Make sure the files exist locally following the configured paths or provide a reachable URL.

---

## 🧠 **Models Included**

### **V1 — Machine Learning**

-   Logistic Regression
-   Random Forest
-   XGBoost

### **V2 — Deep Learning (upcoming)**

-   MLP classifier
-   temporal embeddings
-   Graph Neural Networks (GNN)

---

## 🧰 **AIDD — AI-Driven Development Methodology**

This project is built using a structured AI-Driven Development approach:

-   ML rule families (`src/rules/ml_rules.md`)
-   AI orchestration rules (`src/rules/aidd_rules.md`)
-   documented decision-making
-   CI-style automated verification steps

AI is used as an assistant — not as an uncontrolled code generator.

All modeling choices, architecture, validations and tests remain **human-driven and explainable**.

---

## 📈 **Results (placeholder)**

Metrics will be added as the project progresses:

-   Macro F1 score: _TBA_
-   ROC-AUC: _TBA_
-   Confusion matrix → `evaluation/confusion_matrix.png`
-   Feature importance → `evaluation/feature_importance.png`

---

## 🚀 **Roadmap**

### **V1 — Machine Learning**

-   dataset exploration
-   feature engineering
-   ML pipeline with multiple models
-   address-level prediction script
-   public README
-   LinkedIn project announcement

### **V2 — Deep Learning**

-   MLP baseline
-   temporal embeddings
-   first GNN implementation (GraphSAGE)

### **V3 — On-chain Integration**

-   live on-chain data fetching
-   dynamic feature extraction
-   dashboard (Streamlit)

---

## 📜 **License**

MIT License

---