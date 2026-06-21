# Assignment 2 — Customer Segmentation Using Unsupervised Learning

## Task Objective

Cluster mall customers based on spending habits and annual income, then propose targeted marketing strategies for each identified segment using the Mall Customers Dataset.

---

## Approach

### 1. Data Loading
- Dataset downloaded automatically from a public URL (200 customers × 5 features)
- Features: Age, Annual Income (k$), Spending Score (1–100)

### 2. Data Cleaning & Preprocessing
- No missing values or duplicates found
- Gender label-encoded for correlation analysis
- Features scaled with `StandardScaler` before clustering

### 3. EDA
- Gender distribution (bar + pie chart)
- Feature distributions with mean lines
- Income vs Spending Score scatter by gender
- Correlation heatmap
- Boxplots by gender

### 4. K-Means Clustering
- Elbow Method (WCSS) + Silhouette Score used to find optimal K=5
- K-Means fitted on scaled Age, Income, SpendingScore
- Cluster centroids plotted on original scale

### 5. Dimensionality Reduction
| Method | Purpose |
|--------|---------|
| **PCA** | Fast linear reduction + scree plot for variance explained |
| **t-SNE** | Non-linear 2D visualization to confirm cluster separation |

### 6. Segment Labeling & Marketing Strategies
Clusters labelled based on Income/Spending profile and actionable strategies proposed per segment.

---

## Results & Findings

| Segment | Income | Spending | Strategy |
|---------|--------|----------|----------|
| Premium Loyalists | High | High | Loyalty rewards, exclusive memberships |
| Untapped Potential | High | Low | Personalized outreach, value showcase |
| Impulse Buyers | Low | High | Flash sales, EMI options |
| Price-Sensitive | Low | Low | Bundle deals, referral incentives |
| Average Customer | Medium | Medium | Upsell mid-range, engagement campaigns |

### Key Insights
- 5 distinct customer segments identified using K-Means
- Income and Spending Score are the primary clustering drivers
- t-SNE confirms clusters are well-separated and meaningful
- Female customers (~56%) tend to have slightly higher spending scores

---

## Charts

All charts saved in `charts/` folder:

| File | Description |
|------|-------------|
| `gender_distribution.png` | Gender breakdown bar + pie |
| `feature_distributions.png` | Histograms of Age, Income, Score |
| `scatter_relationships.png` | Income vs Score, Age vs Score by gender |
| `correlation_heatmap.png` | Feature correlation matrix |
| `boxplots_by_gender.png` | Feature boxplots split by gender |
| `elbow_silhouette.png` | Elbow + Silhouette for optimal K |
| `kmeans_clusters.png` | K-Means clusters with centroids |
| `cluster_profiles.png` | Mean feature values per cluster |
| `pca_visualization.png` | PCA scatter + scree plot |
| `tsne_visualization.png` | t-SNE cluster visualization |
| `segment_overview.png` | Segment count + labeled scatter |

---

## Skills Demonstrated
- Unsupervised learning (K-Means)
- Dimensionality reduction (PCA, t-SNE)
- Customer segmentation
- Strategy development based on data insights

---

## Files

| File | Description |
|------|-------------|
| `customer_segmentation.ipynb` | Main Jupyter notebook |
| `README.md` | This file |
