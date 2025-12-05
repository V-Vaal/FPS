# Machine Learning Rules
**FPS — Fraud Prediction System**  
_A curated set of ML rules guiding data exploration, preprocessing, feature engineering and model development._

These rules ensure that all ML work done in FPS is:
- reproducible  
- explainable  
- robust  
- aligned with industry best practices  

---

# 1. Foundations

### **ML-R1 — Always understand the problem before touching the data**
FPS is not a “pure dataset exercise”.  
It is a fraud-classification problem rooted in **on-chain behavior**.  
All preprocessing, modeling and evaluation must reflect that.

---

### **ML-R2 — Prioritize clarity over sophistication**
Simple models with clear assumptions are preferred in V1:
- Logistic Regression  
- RandomForest  
- XGBoost  

Deep Learning and GNNs come later (V2) once clarity is achieved.

---

### **ML-R3 — Maintain a strict separation of concerns**
- `src/data/` → loading, cleaning  
- `src/features/` → feature engineering  
- `src/models/` → training & inference  
- `notebooks/` → experimentation only  

Notebooks must never contain business logic or reusable code.

---

# 2. Data Rules

### **ML-R4 — Keep raw data immutable**
Anything inside `data/raw/` must remain untouched.  
All transformations go to `data/processed/`.

### **ML-R4.1 — External data must be materialized locally**
When data originates from an external API or remote service (e.g., blockchain analytics, SQL endpoints, HTTP/HTTPS data feeds), it must be materialized locally before any modeling step.
Local materialization requirements:
- Load external data into a pandas DataFrame
- Validate structure and types
- Persist the result in a parquet file under data/processed/
- Use the parquet file as the only official training input

This ensures reproducibility, debuggability, independence from network conditions, and full control over dataset versioning.

### **ML-R4.2 — External data must be filtered and bounded**

Every external extraction must enforce:
- a well-defined temporal range (start date and end date),
- a LIMIT or equivalent row boundary (configurable and optionally disabled),
- documentation of these filters inside datasets.py.

This prevents uncontrolled dataset growth and guarantees consistent training conditions.

---

### **ML-R5 — Always document the dataset lineage**
Every dataset used in training or inference must be traceable:
- source  
- version  
- preprocessing steps  
- feature list  

---

### **ML-R6 — Handle missing values explicitly**
Never rely on library defaults.  
Declare the strategy explicitly:
- drop?  
- impute?  
- replace with domain-specific values?  

---

# 3. Preprocessing Rules

### **ML-R7 — Normalize consistently**
Models requiring scaling (LogReg, MLP…) must use:
- `StandardScaler` for normal distributions  
- `MinMaxScaler` if features vary widely  

Scaler must be fit **only on the training set**.

---

### **ML-R8 — Encode categorical data deterministically**
Use either:
- `OneHotEncoder(handle_unknown="ignore")`  
or  
- label encoding *only for ordinal semantics*

Never mix encoders across pipeline runs.

---

### **ML-R9 — Train-test split must reflect the fraud context**
Since fraud frequency is imbalanced:
- use stratification  
- keep the same split across experiments  
- consider cross-validation for robustness  

---

# 4. Feature Engineering Rules

### **ML-R10 — Favor interpretability for V1**
Prefer features that:
- reflect economic intuition  
- represent address activity patterns  
- are easy to explain to non-technical stakeholders  

Deep embeddings come later.

---

### **ML-R11 — Never engineer features inside a notebook**
All feature logic must live in:
`src/features/extract_features.py`
`src/features/select_features.py`

Notebooks may *call* feature functions, but never define them.

---

### **ML-R12 — Log feature importance systematically**
After each training run:
- extract feature importances  
- save plots in `/evaluation/`  
- record values in `evaluation/metrics.txt`

---

# 5. Modeling Rules

### **ML-R13 — Use pipelines for all models**
Every model must be defined as a full pipeline:
`preprocessing → feature_selection → model → postprocessing`

This ensures reproducibility and prevents leakage.

---

### **ML-R14 — Tune models incrementally**
Hyperparameter search follows this order:
1. sanity check with defaults  
2. coarse grid  
3. refined search  
4. cross-validation  

Never jump directly to exhaustive search.

---

### **ML-R15 — Favor robust evaluation over high scores**
Fraud detection requires reliability, not leaderboard tricks.
Metrics to track:
- Macro F1  
- ROC-AUC  
- Recall (fraud classes)  
- Confusion matrix  

---

# 6. Notebook Rules

### **ML-R16 — Notebooks are for exploration, not production**
Every notebook must:
- load functions from `src/`  
- keep code blocks short  
- document assumptions clearly  

A notebook = a story, not spaghetti.

---

### **ML-R17 — Notebooks must be reproducible**
Mandatory elements:
- fixed random seeds  
- clear installation instructions  
- input/output versioning  

### **ML-R17.1 — Notebooks must never call external APIs**

Notebooks must not:
- call external APIs,
- fetch remote data directly,
- trigger costly or repeated external queries.

All notebooks must load data exclusively through: `df = load_raw_dataset("<dataset_key>")`

This isolates the training logic from data ingestion, ensures reproducibility and avoids accidental overuse of external services.

---

# 7. Versioning & Reproducibility Rules

### **ML-R18 — No model weights without metadata**
Every model file must include:
- training date  
- parameters  
- dataset version  
- metrics  

---

### **ML-R19 — Use deterministic seeds**
Set seeds for:
- numpy  
- random  
- sklearn  
- xgboost  
- torch (in V2)

---

### **ML-R20 — All decisions must be explainable**
If a feature, model, metric or transformation is selected:
➡️ the reason must appear either in a notebook or in this document.

---

**End of ML Rules**  
FPS — Fraud Prediction System

