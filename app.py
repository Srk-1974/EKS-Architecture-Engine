import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Set page configuration for professional enterprise look
st.set_page_config(
    page_title="Bhadradri Technologies | EKS Infrastructure Engine",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header/footer/padding for a full-screen premium feel
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
    iframe { border: none; }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Convert logo.png to base64 so it works in Streamlit Cloud ---
logo_base64 = ""
logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img_file:
        logo_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# --- Load the premium EKS Generator index.html ---
html_path = os.path.join(os.path.dirname(__file__), "index.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Replace all relative logo.png references with the embedded base64 data URI
    # This fixes the broken image issue on Streamlit Cloud
    if logo_base64:
        logo_data_uri = f"data:image/png;base64,{logo_base64}"
        html_content = html_content.replace('src="logo.png"', f'src="{logo_data_uri}"')
        html_content = html_content.replace("src='logo.png'", f"src='{logo_data_uri}'")

    # Render the full app inside Streamlit
    components.html(html_content, height=1600, scrolling=True)

else:
    st.error("❌ Infrastructure Portal file (index.html) not found.")
    st.info("Make sure `index.html` is in the same directory as `app.py`.")
