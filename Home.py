# 保存为 Home.py
# 这是 Streamlit 多页应用的首页
# 运行应用：streamlit run Home.py

import streamlit as st

st.set_page_config(
    page_title="California Housing Analysis",
    layout="wide",
)

st.title("California Housing Data (1990) Analysis")

st.markdown("""
    ## Welcome to the Housing App! 👋
    
    This is an interactive application for exploring California housing data from 1990.
    
    ### Features:
    - 📍 **Interactive Maps**: Visualize housing locations across California
    - 📊 **Data Filtering**: Filter by house value, location type, and income level
    - 📈 **Statistical Charts**: View distributions of median house values
    
    ### How to Use:
    1. Navigate to **App Houses** in the sidebar to explore the housing data
    2. Use the filters to find specific housing districts:
       - Set a minimum median house value with the slider
       - Select location types (e.g., <1H OCEAN, INLAND, etc.)
       - Choose income level (Low, Medium, High)
    3. View the interactive map and value distribution histogram
    
    ### Data Information:
    - **Dataset**: California Housing Data from 1990
    - **Features**: Price, location, income, household information
    - **Analysis Tool**: Built with Streamlit, Pandas, and Matplotlib
    
    ---
    
    Created by Xinyan Li
""")

st.info("👈 Use the sidebar to navigate to different pages and explore the housing data!")
