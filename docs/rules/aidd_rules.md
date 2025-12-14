# AIDD — AI-Driven Development Rules  
**FPS — Fraud Prediction System**  
_Methodology for using AI safely, purposefully and transparently during development._

This document explains **how AI is used in FPS**, and—more importantly—**how it is controlled**.  
The goal is to ensure:
- code reliability  
- maintainability  
- clarity  
- ethical use of AI  
- human ownership of all technical decisions  

---

# 1. Principles

### **AIDD-1 — AI assists; it does not decide**
AI can:
- draft boilerplate  
- propose refactoring  
- generate documentation  
- suggest evaluation methods  

But humans decide:
- model choice  
- feature selection  
- metrics  
- architecture  
- validation  

---

### **AIDD-2 — No unreviewed AI-generated code**
All AI-generated code must be:
- reviewed  
- rewritten if necessary  
- documented  
- tested  

If you cannot explain it, you cannot keep it.

---

### **AIDD-3 — AI outputs must respect ML rules**
AI suggestions that violate `ml_rules.md` are rejected.  
ML rules > AI suggestions.

---

# 2. AI Usage in FPS

### **AIDD-4 — AI is used for structure, not logic**
AI may generate:
- file skeletons  
- function signatures  
- docstrings  
- dataset descriptions  
- test templates  

AI does **not** generate:
- modeling logic  
- feature engineering logic  
- business rules  
- fraud heuristics  

### **AIDD-4.1 — AI must preserve the external data ingestion pattern**
AI assistants must not:
- remove or bypass the parquet caching mechanism,
- replace filtered extractions with unbounded external calls,
- introduce direct API calls inside notebooks,
- remove temporal filters or LIMIT clauses.

The external ingestion pattern (fetch → validate → parquet → load) must be preserved at all times.

---

### **AIDD-5 — AI must never hide complexity**
Every AI-generated function must be readable and fully explainable by the human developer.

---

### **AIDD-6 — AI-generated notebooks must follow ML notebook rules**
No “magic blocks”, no unexplained metrics, no hidden transformations.

---

# 3. Code Quality & Testing

### **AIDD-7 — AI can assist writing tests, but cannot write them blindly**
Human validation is mandatory for:
- test objectives  
- expected outcomes  
- edge cases  
- negative tests  

---

### **AIDD-8 — AI is allowed to draft repetitive tests**
Example:
- testing pipeline shape  
- verifying feature presence  
- validating metric keys  

---

### **AIDD-9 — Every critical function must have a test**
Especially:
- dataset loading  
- preprocessing  
- model training pipeline  
- inference  

AI can help generate templates, not logic.

---

# 4. Documentation

### **AIDD-10 — AI can write documentation, but it must remain factual**
No hallucinations.  
No invented references.  
No overexplaining.

---

### **AIDD-11 — Every AI-generated doc must be reviewed**
Checklist:
- Is it true ?  
- Is it necessary ?  
- Is it clear ?  
- Is it consistent with the project ?

---

# 5. Safety & Governance

### **AIDD-12 — AI cannot introduce dependencies without approval**
Every dependency suggested by AI must be:
- known  
- justified  
- version-locked  
- security-checked  

### **AIDD-12bis — AI must not modify external data parameters without explicit justification**

AI-generated changes to any of the following require human validation:
- temporal ranges (start/end dates),
- row limits (LIMIT),
- SQL query structure,
- dataset schema,
- parquet paths or formats.

Uncontrolled modifications to data extraction parameters are prohibited.

---

### **AIDD-13 — AI cannot generate smart contract code without human supervision**
(For future on-chain extensions of FPS.)

---

### **AIDD-14 — Humans write the high-level design**
AI is only a tool for execution and acceleration.

---

# 6. Workflow Integration

### **AIDD-15 — Development follows this pipeline**
1. Human defines task  
2. AI drafts proposal  
3. Human reviews  
4. AI iterates only if asked  
5. Human integrates  
6. Human tests  
7. Commit & document  

---

### **AIDD-16 — AI cannot commit directly**
Only humans run:
`git add .`
`git commit`
`git push`

---

### **AIDD-17 — AI conversations related to FPS must remain archived**
FPS development must be explainable and auditable.

---

# 7. Final Rule

### **AIDD-18 — If AI accelerates you but makes you blind, stop and rethink**
The goal is to be **faster AND better**, not faster and confused.

### **AIDD-18bis — AI suggestions must remain dataset-safe**
AI must not propose changes that could:
- dramatically increase dataset size,
- trigger excessive external API usage,
- bypass caching logic,
- degrade reproducibility.

Any suggestion resulting in unsafe or unbounded datasets must be rejected.

---

**End of AIDD Rules**  
FPS — Fraud Prediction System
