import streamlit as st
import base64
import os
from config import APPS, PORTAL_TITLE, PORTAL_SUBTITLE

# Page Configuration
st.set_page_config(
    page_title=PORTAL_TITLE,
    page_icon="valuehorizon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_of_bin_file(bin_file):
    if not os.path.exists(bin_file):
        return ""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Custom CSS for Light Mode, Stability, and Refinement
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* Minimize Streamlit Padding and Margins */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 1000px !important;
    }
    
    [data-testid="stHeader"] {
        display: none;
    }

    /* Global Light Mode Styles */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }

    /* Hero Section - More Compact */
    .hero-container {
        padding: 1.5rem 0;
        text-align: center;
        border-bottom: 1px solid #f0f0f0;
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #111111;
        margin-bottom: 0.25rem;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 0.95rem;
        font-weight: 400;
        color: #888888;
    }

    .hero-logo-container {
        margin-bottom: 1rem;
        display: flex;
        justify-content: center;
    }

    .hero-logo {
        width: 80px;
        height: 80px;
        object-fit: contain;
    }

    /* Card Styling - Compact and Clean */
    .app-card {
        background: #ffffff;
        border: 1px solid #eaeaea;
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.25s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        height: 100%; /* Fill parent container */
        min-height: 180px; /* Base height */
        text-decoration: none !important;
        color: inherit !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 1rem;
    }

    /* Force Streamlit elements to allow height stretching */
    [data-testid="column"] > div, 
    [data-testid="stVerticalBlock"] > div,
    [data-testid="stMarkdownContainer"] {
        height: 100% !important;
        display: flex;
        flex-direction: column;
    }

    .app-card:hover {
        border-color: #007aff;
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
        background-color: #f9f9f9;
    }

    /* Icon Styling - Smaller and Centered */
    .icon-container {
        width: 60px;
        height: 60px;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #fdfdfd;
        border-radius: 12px;
    }

    .app-icon {
        max-width: 36px;
        max-height: 36px;
        object-fit: contain;
    }

    .app-category {
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #007aff;
        margin-bottom: 0.35rem;
        letter-spacing: 0.8px;
    }

    .app-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #111111;
        margin-bottom: 0.75rem;
        min-height: 2.8rem; /* Space for 2 lines */
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1.2;
    }

    .launch-btn {
        background: #f4f4f4;
        color: #555555;
        padding: 0.4rem 1rem;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        transition: all 0.2s;
        margin-top: auto; /* Push to bottom */
    }

    .app-card:hover .launch-btn {
        background: #007aff;
        color: #ffffff;
    }

    /* Hide Streamlit components */
    #MainMenu, footer, header, .stDeployButton {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
logo_b64 = get_base64_of_bin_file("valuehorizon.png")
logo_html = f'<div class="hero-logo-container"><img src="data:image/png;base64,{logo_b64}" class="hero-logo"></div>' if logo_b64 else ""

st.markdown(f"""
<div class="hero-container">
    {logo_html}
    <div class="hero-title">{PORTAL_TITLE}</div>
    <div class="hero-subtitle">{PORTAL_SUBTITLE}</div>
</div>
""", unsafe_allow_html=True)

# Layout Grid - Using native Streamlit for stability
cols_per_row = 4
rows = [APPS[i:i + cols_per_row] for i in range(0, len(APPS), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for idx, app in enumerate(row):
        with cols[idx]:
            # Image Processing
            img_b64 = get_base64_of_bin_file(app["image"])
            img_html = f'<img src="data:image/png;base64,{img_b64}" class="app-icon">' if img_b64 else ""
            
            # Application Card with Tooltip and minimized height
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" class="app-card" title="{app['description']}">
                <div class="icon-container">{img_html}</div>
                <div class="app-category">{app['category']}</div>
                <div class="app-title">{app['title']}</div>
                <div class="launch-btn">Launch App</div>
            </a>
            """, unsafe_allow_html=True)

# SEO and Meta (Hidden)
st.markdown("""
<title>Value Horizon</title>
""", unsafe_allow_html=True)
