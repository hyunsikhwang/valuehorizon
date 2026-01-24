import streamlit as st
import base64
from config import APPS, PORTAL_TITLE, PORTAL_SUBTITLE

# Page Configuration
st.set_page_config(
    page_title=PORTAL_TITLE,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = '''
    <style>
    .stApp {
      background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/png;base64,%s");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Custom CSS for Premium Glassmorphism Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Set solid background for stability */
    .stApp {
        background: #0e1117;
    }

    .main {
        background: transparent !important;
    }

    /* Header Styling */
    .hero-container {
        padding: 6rem 1rem 4rem 1rem;
        text-align: center;
        color: white;
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #ffffff, #888888);
        -webkit-background-clip: text;
        -webkit-fill-color: transparent;
        letter-spacing: -1.5px;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 300;
        color: #aaaaaa;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Card Grid - Improved Layout */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2.5rem;
        padding: 0 2rem 4rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Glass Card Styling */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 28px;
        padding: 2.5rem 2rem;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        text-decoration: none;
        color: white !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        height: 100%;
        position: relative;
    }

    .glass-card:hover {
        transform: translateY(-8px);
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }

    /* Icon Container - Fixed Size and Centering */
    .card-image-container {
        width: 120px;
        height: 120px;
        border-radius: 20%;
        overflow: hidden;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.05);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .card-image {
        width: 80% !important;
        height: 80% !important;
        object-fit: contain !important;
        transition: transform 0.5s ease;
    }

    .glass-card:hover .card-image {
        transform: scale(1.1);
    }

    .card-category {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        color: #00d2ff;
        margin-bottom: 0.75rem;
        letter-spacing: 1.5px;
    }

    .card-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 1rem;
        line-height: 1.2;
    }

    .card-description {
        font-size: 1rem;
        font-weight: 300;
        color: #999999;
        line-height: 1.6;
        flex-grow: 1;
        margin-bottom: 2rem;
    }

    .visit-btn {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        padding: 0.6rem 1.4rem;
        border-radius: 14px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
        margin-top: auto;
    }

    .glass-card:hover .visit-btn {
        background: white;
        color: black;
        border-color: white;
    }

    /* Hide redundant elements */
    #MainMenu, footer, header, .stDeployButton {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
<div class="hero-container">
    <h1 class="hero-title">{PORTAL_TITLE}</h1>
    <p class="hero-subtitle">{PORTAL_SUBTITLE}</p>
</div>
""", unsafe_allow_html=True)

# Layout Grid
card_html = '<div class="card-grid">'

import os

for app in APPS:
    # Converting image to base64 for embedding
    try:
        img_b64 = get_base64_of_bin_file(app["image"])
        img_src = f"data:image/png;base64,{img_b64}"
    except:
        img_src = ""

    card_html += f"""
    <a href="{app['url']}" target="_blank" class="glass-card">
        <div class="card-image-container">
            <img src="{img_src}" class="card-image" alt="{app['title']}">
        </div>
        <div class="card-category">{app['category']}</div>
        <div class="card-title">{app['title']}</div>
        <div class="card-description">{app['description']}</div>
        <div class="visit-btn">Visit App</div>
    </a>
    """

card_html += '</div>'

# Main UI Injection
st.markdown(card_html, unsafe_allow_html=True)
