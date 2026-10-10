# 保存为 app.py
# 安装依赖：pip install streamlit pandas matplotlib
# 运行应用：streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="California Housing Data (1990) by Xinyan Li",
    layout="wide",
)

df = pd.read_csv('housing.csv')

st.title("California Housing Data (1990) by Xinyan Li")

min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
    step=1,
)

st.subheader("See more filters in the sidebar:")

location_types = sorted(df["ocean_proximity"].dropna().unique().tolist())

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types,
)

income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"],
)

filtered_df = df[
    (df["median_house_value"] >= min_value)
    & (df["ocean_proximity"].isin(selected_locations))
]

if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

if filtered_df.empty:
    st.info("No districts match the selected filters.")
else:
    st.map(filtered_df[["latitude", "longitude"]].dropna())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(
        filtered_df["median_house_value"].dropna(),
        bins=30,
        color="steelblue",
        edgecolor="white",
    )
    ax.set_title("Median House Value Distribution")
    ax.set_xlabel("Median House Value ($)")
    ax.set_ylabel("Number of Districts")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)