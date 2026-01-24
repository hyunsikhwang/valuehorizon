import streamlit as st
import base64
import os
from config import APPS, PORTAL_TITLE, PORTAL_SUBTITLE

# Page Configuration
st.set_page_config(
    page_title=PORTAL_TITLE,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_of_bin_file(bin_file):
    if not os.path.exists(bin_file):
        return ""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Custom CSS for Light Mode and Stability
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* Global Light Mode Styles */
    .stApp {
        background-color: #fcfcfc;
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0);
    }

    /* Hero Section */
    .hero-container {
        padding: 4rem 1rem 3rem 1rem;
        text-align: center;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #111111;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        font-weight: 400;
        color: #666666;
        margin-bottom: 3rem;
    }

    /* Card Styling */
    .app-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
        color: inherit !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    .app-card:hover {
        transform: translateY(-5px);
        border-color: #007aff;
        box-shadow: 0 12px 24px rgba(0,0,0,0.08);
    }

    /* Icon Styling - Small and Centered */
    .icon-container {
        width: 80px;
        height: 80px;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f8f9fa;
        border-radius: 16px;
    }

    .app-icon {
        max-width: 50px;
        max-height: 50px;
        object-fit: contain;
    }

    .app-category {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #007aff;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }

    .app-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #111111;
        margin-bottom: 0.75rem;
    }

    .app-desc {
        font-size: 0.95rem;
        color: #555555;
        line-height: 1.5;
        margin-bottom: 1.5rem;
        flex-grow: 1;
    }

    .launch-btn {
        background: #f0f0f0;
        color: #333333;
        padding: 0.5rem 1.2rem;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: 600;
        transition: background 0.2s;
    }

    .app-card:hover .launch-btn {
        background: #007aff;
        color: white;
    }

    /* Hide Streamlit components */
    #MainMenu, footer, header, .stDeployButton {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
<div class="hero-container">
    <div class="hero-title">{PORTAL_TITLE}</div>
    <div class="hero-subtitle">{PORTAL_SUBTITLE}</div>
</div>
""", unsafe_allow_html=True)

# Display Apps using Streamlit Columns for maximum stability
rows = [APPS[i:i + 3] for i in range(0, len(APPS), 3)]

for row in rows:
    cols = st.columns(3)
    for idx, app in enumerate(row):
        with cols[idx]:
            # Image Processing
            img_b64 = get_base64_of_bin_file(app["image"])
            img_html = f'<img src="data:image/png;base64,{img_b64}" class="app-icon">' if img_b64 else ""
            
            # Per-card Markdown to ensure stable rendering
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" class="app-card">
                <div class="icon-container">{img_html}</div>
                <div class="app-category">{app['category']}</div>
                <div class="app-title">{app['title']}</div>
                <div class="app-desc">{app['description']}</div>
                <div class="launch-btn">Launch App</div>
            </a>
            """, unsafe_allow_html=True)

# Optional padding at bottom
st.markdown("<div style='padding: 2rem;'></div>", unsafe_allow_html=True)
