"""
Global Superstore Sales Performance Dashboard
Interactive Streamlit application.

Run with:
    streamlit run app.py
"""

import os
import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="📊",
    layout="wide",
)


# ---------------------------------------------------------------------------
# Data loading and cleaning (cached so it only runs once)
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    path = os.path.join("data", "Global_Superstore2.csv")
    df = pd.read_csv(path, encoding="latin-1")

    # Parse dates (DD-MM-YYYY format)
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y", errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d-%m-%Y", errors="coerce")

    # Drop mostly-empty Postal Code column, remove duplicates
    if "Postal Code" in df.columns:
        df = df.drop(columns=["Postal Code"])
    df = df.drop_duplicates()

    # Derived time columns
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df


df = load_data()

# ---------------------------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------------------------
st.sidebar.header("🔎 Filters")

regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
region = st.sidebar.selectbox("Region", regions)

categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
category = st.sidebar.selectbox("Category", categories)

# Sub-Category options depend on the chosen category
if category != "All":
    sub_options = df[df["Category"] == category]["Sub-Category"].dropna().unique()
else:
    sub_options = df["Sub-Category"].dropna().unique()
sub_category = st.sidebar.selectbox("Sub-Category", ["All"] + sorted(sub_options.tolist()))

# Apply filters
filtered = df.copy()
if region != "All":
    filtered = filtered[filtered["Region"] == region]
if category != "All":
    filtered = filtered[filtered["Category"] == category]
if sub_category != "All":
    filtered = filtered[filtered["Sub-Category"] == sub_category]

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("📊 Global Superstore Sales Performance Dashboard")
st.markdown("Analyze **sales, profit, and segment-wise performance** interactively.")

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# ---------------------------------------------------------------------------
# KPI cards
# ---------------------------------------------------------------------------
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
margin = (total_profit / total_sales * 100) if total_sales else 0
total_orders = filtered["Order ID"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"${total_sales:,.0f}")
c2.metric("Total Profit", f"${total_profit:,.0f}")
c3.metric("Profit Margin", f"{margin:.1f}%")
c4.metric("Total Orders", f"{total_orders:,}")

st.divider()

# ---------------------------------------------------------------------------
# Charts row 1
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    cat = filtered.groupby("Category")["Sales"].sum().reset_index()
    fig = px.bar(cat, x="Category", y="Sales", color="Category", text_auto=".2s")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Sales by Region")
    reg = filtered.groupby("Region")["Sales"].sum().sort_values(ascending=True).reset_index()
    fig = px.bar(reg, x="Sales", y="Region", orientation="h", color="Sales",
                 color_continuous_scale="Viridis")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Charts row 2
# ---------------------------------------------------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 5 Customers by Sales")
    top5 = (filtered.groupby("Customer Name")["Sales"].sum()
            .sort_values(ascending=False).head(5).reset_index())
    fig = px.bar(top5, x="Sales", y="Customer Name", orientation="h",
                 color="Sales", color_continuous_scale="Reds")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("Sales & Profit by Segment")
    seg = filtered.groupby("Segment")[["Sales", "Profit"]].sum().reset_index()
    fig = px.bar(seg, x="Segment", y=["Sales", "Profit"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Monthly trend (full width)
# ---------------------------------------------------------------------------
st.subheader("Monthly Sales Trend")
monthly = filtered.groupby("Order Month")["Sales"].sum().reset_index()
monthly["Order Month"] = pd.to_datetime(monthly["Order Month"])
monthly = monthly.sort_values("Order Month")
fig = px.line(monthly, x="Order Month", y="Sales", markers=True)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Data preview
# ---------------------------------------------------------------------------
with st.expander("🔍 View filtered data"):
    st.dataframe(filtered.head(200), use_container_width=True)

st.caption("Global Superstore BI Dashboard • Built with Streamlit")
