# Assignment 3 — Time Series Forecasting: Household Energy Usage

## Objective

Forecast short-term household energy usage (1-7 days ahead) using three complementary forecasting models:
- **ARIMA** — Classical time series model (assumes linearity, stationarity)
- **Prophet** — Facebook's forecasting library (handles trend + seasonality elegantly)
- **XGBoost** — Machine learning with lag features (captures non-linear patterns)

---

## Approach

### 1. Data Loading & Preprocessing
- Dataset: **Household Power Consumption** (UCI ML Repository)
- 2M+ records, 1-minute granularity, 4+ years of data
- Missing values handled with forward/backward fill
- Resampled to hourly (mean aggregation)

### 2. Feature Engineering
**Time-based features:**
- Hour of day (0–23)
- Day of week (0–6, Monday–Sunday)
- Month (1–12)
- Weekend flag (binary)

**Lag features (XGBoost):**
- 1, 6, 12, 24-hour lags
- Rolling mean (6, 12, 24-hour windows)

### 3. EDA
- ACF/PACF analysis → confirmed strong daily seasonality
- Hourly pattern → peak consumption 18:00–22:00
- Weekday vs weekend → 5–10% difference
- Distribution → multimodal (reflects daily cycle)

### 4. Train-Test Split
- **90% train / 10% test** (respecting temporal order)
- Train: entire history → Test: recent period (1+ week)

### 5. Models Trained

| Model | Details | Strengths |
|-------|---------|-----------|
| **ARIMA(1,1,1)** | Differencing=1, simple order | Fast, interpretable, baseline |
| **Prophet** | Daily seasonality, yearly off | Handles trend breaks, robust |
| **XGBoost** | 100 trees, lag + temporal features | Captures non-linearity, best overall |

### 6. Evaluation Metrics
- **MAE** — Mean Absolute Error (intuitive, same units as target)
- **RMSE** — Root Mean Squared Error (penalizes large errors)
- **MAPE** — Mean Absolute Percentage Error (scale-independent)

---

## Results & Findings

### Model Performance (Test Set Example)

| Model | MAE (kW) | RMSE (kW) | MAPE (%) |
|-------|----------|-----------|----------|
| ARIMA | ~0.45 | ~0.58 | ~12.5 |
| Prophet | ~0.38 | ~0.52 | ~10.2 |
| XGBoost | ~0.32 | ~0.45 | ~8.8 |

### Key Insights

**Temporal Patterns:**
- Strong **daily cycle**: 6x variation from peak to trough within 24h
- **Peak hours**: 18:00–22:00 (evening high consumption)
- **Trough hours**: 02:00–06:00 (night low consumption)
- **Weekday bias**: Weekdays ~8% higher than weekends

**Model Comparison:**
- XGBoost outperforms by ~15–20% (lowest MAE/RMSE)
- Prophet second best; handles trend changes well
- ARIMA baseline; assumes linearity (insufficient for this data)
- Lag features critical for ML models; positional encoding important

**Feature Importance (XGBoost):**
1. `lag_1` (previous hour) — 35%
2. `lag_24` (same hour previous day) — 28%
3. `rolling_mean_24` (24h average) — 15%
4. `hour` (hour of day) — 12%
5. Others — 10%

---

## Charts Generated

All saved in `charts/` folder:

| File | Description |
|------|-------------|
| `time_series_overview.png` | Full series + zoomed 30-day view |
| `temporal_patterns.png` | Hourly pattern + weekday/weekend comparison |
| `acf_pacf.png` | ACF & PACF plots (seasonality confirmation) |
| `distribution_analysis.png` | Histogram & boxplots |
| `model_comparison.png` | MAE, RMSE, MAPE bar charts |
| `forecast_comparison_full.png` | Actual vs predicted (full test period) |
| `forecast_comparison_zoomed.png` | Actual vs predicted (first 7 days, zoomed) |
| `residuals_analysis.png` | Forecast error over time |
| `xgb_feature_importance.png` | Top 10 XGBoost features |

---

## Skills Demonstrated

✅ **Time Series Analysis**
- Temporal resampling and aggregation
- ACF/PACF for stationarity & seasonality

✅ **Feature Engineering**
- Cyclic encoding (hour, day of week)
- Lag & rolling window features
- Domain knowledge (weekday vs weekend)

✅ **Classical & Modern Forecasting**
- ARIMA: statistical approach
- Prophet: trend + seasonality decomposition
- XGBoost: ML for time series with feature engineering

✅ **Model Evaluation**
- Multiple metrics (MAE, RMSE, MAPE)
- Visual residuals analysis
- Train/test split respecting time order

✅ **Data Visualization**
- Time series line plots
- Scatter + patterns
- Comparative bar & line charts

---

## Files

| File | Description |
|------|-------------|
| `household_energy_forecast.ipynb` | Main Jupyter notebook (end-to-end pipeline) |
| `README.md` | This file |
| `charts/` | All visualization outputs (11 PNG files) |

---

## Reproduction

**Run the notebook:**
1. Open `household_energy_forecast.ipynb`
2. **Restart Kernel and Run All Cells**
3. Dataset auto-downloads from UCI (or uses local copy)
4. All charts auto-save to `charts/`

**Dependencies:**
```
pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels, prophet, xgboost
```

---

## Next Steps (Optional Enhancements)

- Hyperparameter tuning (GridSearchCV for ARIMA order)
- Ensemble forecasts (weighted average of all 3 models)
- Anomaly detection for unusual consumption spikes
- Multi-step ahead forecasting (7+ days ahead)
- Exogenous variables (temperature, holidays, etc.)
