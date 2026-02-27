import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration for professional enterprise look
st.set_page_config(
    page_title="Bhadradri Technologies | EKS Infrastructure Engine",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header/footer for premium feel
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load the premium EKS Generator index.html
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Inject the HTML content into the Streamlit app
    # Using full screen height
    components.html(html_content, height=1500, scrolling=True)
else:
    st.error("❌ Infrastructure Portal file (index.html) not found in the current directory.")
