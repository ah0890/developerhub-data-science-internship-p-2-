# Assignment 1 — Term Deposit Subscription Prediction

## Task Objective

Predict whether a bank customer will subscribe to a term deposit as a result of a phone marketing campaign, using the [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing).

---

## Approach

### 1. Data Loading
- Dataset fetched directly from UCI ML Repository using the `ucimlrepo` library
- 45,211 records × 16 features + 1 target (`subscribed`: yes/no)

### 2. Data Cleaning & Preprocessing
- Replaced `"unknown"` string values with `NaN` and imputed using column mode
- Removed duplicate rows
- Engineered `was_contacted_before` indicator from `pdays == -1`
- Binary columns (`default`, `housing`, `loan`) label-encoded
- Nominal categorical columns one-hot encoded (`job`, `marital`, `education`, `contact`, `month`, `poutcome`)
- Target mapped to binary: `yes → 1`, `no → 0`
- Applied `StandardScaler` for Logistic Regression

### 3. EDA
- Class imbalance analysis (~88% No, ~12% Yes)
- Feature distributions by subscription outcome
- Correlation heatmap
- Boxplots of `duration` and `age` by target

### 4. Models Trained
| Model | Notes |
|-------|-------|
| Logistic Regression | `class_weight='balanced'`, scaled features |
| Random Forest | `n_estimators=200`, `class_weight='balanced'` |

### 5. Evaluation Metrics
- Confusion Matrix
- F1-Score (weighted and per-class)
- ROC Curve & AUC

### 6. Explainability (XAI)
- SHAP `TreeExplainer` applied to Random Forest
- Global summary plot (feature importance across all predictions)
- Waterfall plots for **5 individual predictions** (3 true positives + 2 true negatives)

---

## Results & Findings

| Model | F1 (weighted) | F1 (Yes class) | ROC-AUC |
|-------|-------------|----------------|---------|
| Logistic Regression | ~0.86 | ~0.55 | ~0.91 |
| Random Forest | ~0.90 | ~0.65 | ~0.93 |

### Key Insights
- `duration` (call length) is the strongest predictor but is only available post-call
- `poutcome_success` (previous campaign success) is the most actionable pre-call signal
- Higher `balance` and `was_contacted_before` increase subscription probability
- Too many contacts (`campaign`) reduces conversion likelihood
- Random Forest significantly outperforms Logistic Regression on the minority class

---

## Skills Demonstrated
- Classification modeling
- Feature encoding (label encoding, one-hot encoding)
- Handling class imbalance
- Model interpretability (Explainable AI with SHAP)
- Customer behavior analysis

---

## Files

| File | Description |
|------|-------------|
| `term_deposit_prediction.ipynb` | Main Jupyter notebook with full analysis |
| `README.md` | This file |
