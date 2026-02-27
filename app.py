import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(
    page_title="Bhadradri Technologies | EKS Infrastructure Engine",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide ALL Streamlit chrome so the iframe is full-viewport
st.markdown("""
    <style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }
    iframe {
        border: none !important;
        display: block !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encode logo as base64 so it works inside the iframe sandbox
logo_base64 = ""
logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode("utf-8")

# Load the HTML portal
html_path = os.path.join(os.path.dirname(__file__), "index.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace logo.png with base64 data URI so it renders on Streamlit Cloud
    if logo_base64:
        data_uri = f"data:image/png;base64,{logo_base64}"
        html = html.replace('src="logo.png"', f'src="{data_uri}"')
        html = html.replace("src='logo.png'", f"src='{data_uri}'")

    # Render with scrolling=True so content scrolls INSIDE the iframe.
    # This makes position:fixed work correctly (fixed to iframe viewport).
    components.html(html, height=900, scrolling=True)

else:
    st.error("❌ index.html not found. Make sure it is in the same folder as app.py.")
