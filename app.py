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

# Premium CSS Injection
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>

<style>
    /* Reset and Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #0f172a;
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 4rem !important;
        max-width: 1200px !important;
    }

    /* Premium Border & Glassmorphism */
    .premium-border {
        position: relative;
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 1.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 1;
    }
    
    .premium-border::after {
        content: '';
        position: absolute;
        inset: -1px;
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.3), rgba(59, 130, 246, 0.3));
        z-index: -1;
        border-radius: inherit;
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .premium-border:hover {
        transform: translateY(-8px);
        background: rgba(30, 41, 59, 0.9);
        border-color: rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }
    
    .premium-border:hover::after {
        opacity: 1;
    }

    /* Hero Section */
    .hero-container {
        text-align: center;
        margin-bottom: 5rem;
    }

    .hero-brand {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .hero-logo-container {
        padding: 0.75rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 1.25rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .hero-logo {
        width: 48px;
        height: 48px;
        object-fit: contain;
    }

    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #f8fafc;
    }

    .hero-title span {
        color: #3b82f6;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #94a3b8;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    .hero-divider {
        height: 4px;
        width: 80px;
        background: linear-gradient(to right, #3b82f6, #fbbf24);
        margin: 2rem auto 0;
        border-radius: 2px;
        opacity: 0.8;
    }

    /* Card Specifics */
    .app-card {
        padding: 2.5rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        height: 100%;
        text-decoration: none !important;
        color: inherit !important;
    }

    .app-icon-container {
        padding: 1.25rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }

    .app-card:hover .app-icon-container {
        transform: scale(1.1);
    }

    .app-icon-container .material-symbols-outlined {
        font-size: 2.5rem;
    }

    .app-category {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        margin-bottom: 0.75rem;
        opacity: 0.8;
    }

    .app-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 2rem;
        color: #f1f5f9;
        line-height: 1.2;
    }

    .launch-btn {
        width: 100%;
        padding: 0.875rem;
        background: #3b82f6;
        color: white;
        border-radius: 0.75rem;
        font-weight: 600;
        font-size: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        transition: all 0.2s;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }

    .app-card:hover .launch-btn {
        background: #2563eb;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
    }

    /* Coming Soon Card */
    .coming-soon-card {
        background: rgba(255, 255, 255, 0.02);
        border: 2px dashed rgba(255, 255, 255, 0.1);
        border-radius: 1.5rem;
        padding: 2.5rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        height: 100%;
        color: #64748b;
    }

    .coming-soon-card .material-symbols-outlined {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }

    /* Footer */
    .footer {
        margin-top: 6rem;
        text-align: center;
        color: #475569;
        font-size: 0.875rem;
    }

    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper for Icon Mapping
def get_icon_for_app(title):
    mapping = {
        "Daily K-Stock": {"icon": "monitoring", "color": "#3b82f6"},
        "Global Market Pulse": {"icon": "public", "color": "#a855f7"},
        "KRX Market Monitor": {"icon": "account_balance", "color": "#10b981"},
        "Search DART": {"icon": "description", "color": "#f59e0b"},
        "Stock Performance": {"icon": "query_stats", "color": "#fbbf24"},
    }
    return mapping.get(title, {"icon": "apps", "color": "#3b82f6"})

# Hero Section
logo_b64 = get_base64_of_bin_file("valuehorizon.png")
logo_html = f'<div class="hero-logo-container"><img src="data:image/png;base64,{logo_b64}" class="hero-logo"></div>' if logo_b64 else ""

st.markdown(f"""
<div class="hero-container">
    <div class="hero-brand">
        {logo_html}
        <div class="hero-title">Value <span>Horizon</span></div>
    </div>
    <div class="hero-subtitle">{PORTAL_SUBTITLE}</div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# App Grid
cols_per_row = 4
rows = [APPS[i:i + cols_per_row] for i in range(0, len(APPS), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for idx, app in enumerate(row):
        with cols[idx]:
            app_meta = get_icon_for_app(app["title"])
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" class="premium-border app-card">
                <div class="app-icon-container">
                    <span class="material-symbols-outlined" style="color: {app_meta['color']}">
                        {app_meta['icon']}
                    </span>
                </div>
                <div class="app-category" style="color: {app_meta['color']}">{app['category']}</div>
                <div class="app-title">{app['title']}</div>
                <div class="launch-btn">
                    Launch App
                    <span class="material-symbols-outlined" style="font-size: 1rem;">arrow_forward</span>
                </div>
            </a>
            """, unsafe_allow_html=True)
    
    # Add "Coming Soon" card if the row is not full or at the end
    if len(row) < cols_per_row:
        for i in range(len(row), cols_per_row):
            with cols[i]:
                st.markdown("""
                <div class="coming-soon-card">
                    <span class="material-symbols-outlined">add_circle</span>
                    <p style="font-style: italic; font-weight: 500;">More modules coming soon</p>
                </div>
                """, unsafe_allow_html=True)
    elif row == rows[-1]: # If it's the last row and it was full, add a new row with Coming Soon
        cols = st.columns(cols_per_row)
        with cols[0]:
            st.markdown("""
            <div class="coming-soon-card">
                <span class="material-symbols-outlined">add_circle</span>
                <p style="font-style: italic; font-weight: 500;">More modules coming soon</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2024 Value Horizon. Professional Trading Ecosystem.
</div>
""", unsafe_allow_html=True)
