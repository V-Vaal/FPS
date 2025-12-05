# ML Development Checklist  
**FPS — Fraud Prediction System**  
_A practical checklist to ensure every ML step is controlled, explainable and reproducible._

This checklist must be followed for:
- dataset exploration  
- preprocessing  
- feature engineering  
- model training  
- evaluation  
- inference pipeline creation  

---

## 1. 💡 Problem Understanding
- [ ] The objective is clearly defined  
- [ ] Fraud categories are understood (legit / phishing / scam / exploit)  
- [ ] Constraints are identified (imbalanced classes, on-chain behavior)  
- [ ] Evaluation metrics are chosen (Macro F1, ROC-AUC, recall for fraud)

---

## 2. 📦 Dataset Handling
- [ ] Raw data is placed in `data/raw/`  
- [ ] Processed data goes to `data/processed/`  
- [ ] No transformation is applied directly on raw files  
- [ ] Dataset version is documented  
- [ ] Missing values strategy is defined  
- [ ] Outliers are identified and either justified or handled  

    ### External Sources (API / SQL / Dune / similar)
- [ ] A temporal range is defined for the extraction
- [ ] A LIMIT (or row boundary) is defined, configurable, or explicitly disabled
- [ ] The dataset is fetched once, validated, and written to data/processed/*.parquet
- [ ] The parquet file has been validated (shape, types, missing values)
- [ ] No external API is called from notebooks
- [ ] The dataset version and filters are documented in `src/config/datasets.py`
- [ ] The modeling pipeline always uses the parquet file as input

---

## 3. ⚙️ Preprocessing
- [ ] Train-test split with **stratification**  
- [ ] Scaling method explicitly chosen  
- [ ] Encoding method explicitly chosen  
- [ ] Preprocessing lives inside `src/data/`  
- [ ] No preprocessing logic exists inside notebooks  

---

## 4. 🧩 Feature Engineering
- [ ] All feature functions are declared in `src/features/`  
- [ ] No new features are created inside notebooks  
- [ ] Feature importance is extracted after training  
- [ ] Feature definitions are documented  
- [ ] Domain-specific logic is justified  

---

## 5. 🧠 Modeling
- [ ] Pipeline is used (preprocessing + model + postprocessing)  
- [ ] Hyperparameter search is incremental  
- [ ] All model parameters are logged  
- [ ] Seeds are fixed for reproducibility  
- [ ] Model weights include metadata (date, dataset version, metrics)  

---

## 6. 📊 Evaluation
- [ ] Confusion matrix is generated  
- [ ] Classification report is saved in `evaluation/`  
- [ ] Feature importances are saved  
- [ ] Metrics are compared across models  
- [ ] Fraud classes recall is monitored carefully  

---

## 7. 📓 Notebook Hygiene
- [ ] Notebook runs top-to-bottom without interruption  
- [ ] No hidden state  
- [ ] No irreversible transformations  
- [ ] No business logic (import functions instead)  
- [ ] Conclusions are written clearly  

---

## 8. 🔐 Final Validation
- [ ] Code reviewed (AI suggestions checked)  
- [ ] All rules from `ml_rules.md` respected  
- [ ] AIDD rules respected  
- [ ] README updated if needed  
- [ ] Results reproducible on another machine  

---

**End of ML Development Checklist**  
FPS — Fraud Prediction System
