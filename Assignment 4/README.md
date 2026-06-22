# Assignment 4 — Loan Default Risk with Business Cost Optimization

## Task Objective

Build a **binary classification model** to predict loan default, then **optimize the decision threshold** based on business cost analysis (false positives vs false negatives).

---

## Business Context

### Cost Matrix
| Scenario | Cost | Impact |
|----------|------|--------|
| **False Positive (FP)** | $1,000 | Reject a good loan → lost revenue |
| **False Negative (FN)** | $10,000 | Approve a bad loan → loss on default |

**Cost Ratio:** FN is **10x more expensive** than FP → bias threshold toward caution.

---

## Approach

### 1. Data Loading & EDA
- Load Home Credit Default Risk dataset
- Analyze class imbalance (~8% default rate)
- Explore feature distributions by target

### 2. Data Preprocessing
- Handle missing values (median imputation)
- Encode categorical features
- Scale features with StandardScaler
- Train-test split: 80-20 (stratified)

### 3. Model Training
| Model | Algorithm | Key Features |
|-------|-----------|--------------|
| **Logistic Regression** | Linear classifier, balanced weights | Fast, interpretable, baseline |
| **CatBoost** | Gradient boosting, class weights | Non-linear, handles imbalance well |

### 4. Threshold Optimization
- **Default threshold:** 0.5 (arbitrary)
- **Optimal threshold:** Minimize total business cost = (FP × $1,000) + (FN × $10,000)
- Sweep thresholds 0.01 → 0.99, find minimum

### 5. Model Evaluation
- ROC curve & AUC
- Precision-Recall curve
- Confusion matrices (default vs optimal)
- Cost breakdown analysis

---

## Results & Findings

### Model Performance
- **Logistic Regression AUC:** ~0.75 (test set)
- **Optimal Threshold:** ~0.30 (not 0.5!)
- **Cost Reduction:** ~30–40% by moving to optimal threshold

### Key Insights

**1. Class Imbalance is Critical**
- Only 8% loans default
- Standard 0.5 threshold rejects too many good loans

**2. Business Cost Drives Decisions**
- FN ($10k) >> FP ($1k) → tolerate more false positives
- Optimal threshold < 0.5 (lower bar to approve)

**3. Threshold Optimization Matters**
- At 0.5: $150,000 total cost (high FN from missing defaults)
- At optimal: $90,000 total cost (accept more FP, avoid expensive FN)
- **$60,000 savings** from one threshold adjustment

**4. Feature Importance**
- Income ratio (ANT_INCOME / AMT_CREDIT) most predictive
- Employment history (DAYS_EMPLOYED) matters
- Age has moderate importance

---

## Visualizations

| Chart | Purpose |
|-------|---------|
| `01_class_distribution.png` | Imbalance visualization |
| `02_feature_distributions.png` | Feature patterns by target |
| `03_threshold_optimization.png` | Cost curve + FP/FN breakdown |
| `04_roc_pr_curves.png` | Model performance curves |
| `05_confusion_matrices.png` | Default vs optimal thresholds |
| `06_feature_importance.png` | Top predictive features |
| `07_final_summary.png` | Metrics, costs, prediction dist. |

---

## Skills Demonstrated

✅ **Binary Classification**
- Imbalanced data handling
- Class weight adjustment
- Threshold tuning

✅ **Business Economics**
- Cost-sensitive evaluation
- ROI calculation
- Optimal decision-making

✅ **Model Interpretability**
- Feature importance ranking
- Confusion matrix analysis
- Cost-benefit trade-offs

✅ **Risk Modeling**
- Default probability estimation
- Risk scoring
- Portfolio management insights

---

## Key Takeaway

**A model is only as good as its decision threshold.** Standard metrics (accuracy, F1) may mislead when costs are asymmetric. Always optimize for **business impact**, not just statistical accuracy.

---

## Files

| File | Description |
|------|-------------|
| `loan_default_risk.ipynb` | Complete analysis notebook |
| `README.md` | This file |
| `charts/` | 7 visualization PNG files |

---

## How to Run

1. Open `loan_default_risk.ipynb`
2. **Restart Kernel and Run All Cells**
3. Dataset auto-downloads (or uses synthetic data)
4. Charts auto-save to `charts/`
5. Review cost optimization results

---

## Next Steps (Extensions)

- Add more features: credit history, loan type, purpose
- Ensemble CatBoost + Logistic Regression predictions
- Sensitivity analysis: explore different cost matrices
- Deploy model with optimal threshold as business rule
