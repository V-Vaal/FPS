# **FPS — Fraud Prediction System**

### **FPS (Fraud Prediction System)** is an AI-driven project designed to identify and classify Ethereum addresses based on their fraud risk level (legit, phishing, scam, exploit).

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
├── notebooks/          → exploration & prototyping notebooks
├── src/                → production-grade source code
│   ├── data/           → dataset loading & preprocessing
│   ├── features/       → feature engineering utilities
│   ├── models/         → training, evaluation & inference
│   ├── rules/          → ML rules & AIDD development rules
│   └── web3/           → on-chain data fetching & utilities
├── evaluation/         → reports, metrics & visualizations
└── requirements.txt    → Python dependencies
```

---

## 📦 **Dataset**

Primary dataset:

**Ethereum Fraud Dataset by Activity** (Kaggle)

It contains labeled Ethereum addresses across four categories:

-   phishing
-   scam
-   exploit
-   legit

Alongside more than 30 behavioral on-chain features.

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

### **V1 — Machine Learning (10 days)**

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