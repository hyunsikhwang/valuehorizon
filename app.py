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

    .main {
        background: transparent;
    }

    /* Header Styling */
    .hero-container {
        padding: 4rem 1rem;
        text-align: center;
        color: white;
    }

    .hero-title {
        font-size: 4.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #ffffff, #a5a5a5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        color: #cccccc;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Card Grid */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Glass Card Styling */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 1.5rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-decoration: none;
        color: white !important;
        display: flex;
        flex-direction: column;
        height: 100%;
        position: relative;
        overflow: hidden;
    }

    .glass-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }

    .card-image-container {
        width: 100%;
        aspect-ratio: 1;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 1.5rem;
    }

    .card-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }

    .glass-card:hover .card-image {
        transform: scale(1.1);
    }

    .card-category {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        color: #4facfe;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }

    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }

    .card-description {
        font-size: 0.95rem;
        font-weight: 300;
        color: #bbbbbb;
        line-height: 1.6;
        flex-grow: 1;
    }

    .card-footer {
        margin-top: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }

    .visit-btn {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .glass-card:hover .visit-btn {
        background: white;
        color: black;
    }

    /* Remove Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .fade-in {
        animation: fadeIn 0.8s ease-out forwards;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
<div class="hero-container fade-in">
    <h1 class="hero-title">{PORTAL_TITLE}</h1>
    <p class="hero-subtitle">{PORTAL_SUBTITLE}</p>
</div>
""", unsafe_allow_html=True)

# Display Apps in a Grid
cols = st.columns(3) # Creating a grid using columns to help with layout spacing
# But we will use custom HTML grid for better control

card_html = '<div class="card-grid">'

for app in APPS:
    # Converting image to base64 for embedding
    try:
        img_b64 = get_base64_of_bin_file(app["image"])
        img_src = f"data:image/png;base64,{img_b64}"
    except:
        img_src = "" # Fallback

    card_html += f"""
    <a href="{app['url']}" target="_blank" class="glass-card fade-in">
        <div class="card-image-container">
            <img src="{img_src}" class="card-image" alt="{app['title']}">
        </div>
        <div class="card-category">{app['category']}</div>
        <div class="card-title">{app['title']}</div>
        <div class="card-description">{app['description']}</div>
        <div class="card-footer">
            <div class="visit-btn">Visit App →</div>
        </div>
    </a>
    """

card_html += '</div>'

st.markdown(card_html, unsafe_allow_html=True)

# SEO and Meta (Hidden)
st.markdown("""
<title>Equity Bridge - Premium Stock Investment Portal</title>
<meta name="description" content="A centralized gateway for advanced stock market analysis and financial data monitoring tools.">
""", unsafe_allow_html=True)
