import streamlit as st

# Set page config
st.set_page_config(
    page_title="World Cities MIS",
    page_icon="🌍",
    layout="centered"
)

# Title and welcome section
st.title("🌍 World Cities Management System")

st.markdown("""
    ---
    ### Welcome to World Cities MIS
    
    This is your comprehensive platform for exploring and managing world cities data.
    Navigate through different sections to access various features and analytics.
    
    ---
""")

# Display welcome message
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        #### 📍 Get Started
        
        Click the button below to explore the main application and access all features.
    """)

with col2:
    st.markdown("")  # Spacing

# Navigation button to app.py
if st.button("Go to Application →", key="nav_button", use_container_width=True):
    st.switch_page("pages/app.py")

# Footer with additional info
st.markdown("""
    ---
    #### About This App
    
    This Streamlit application provides tools and insights for world cities management.
    Use the sidebar navigation to move between pages.
    
    **Version:** 1.0.0  
    **Last Updated:** 2026
""")
