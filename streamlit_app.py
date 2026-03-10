import streamlit as st

# 1. إعدادات الصفحة والديزاين (الخلفية بصور الوجبات والحركة)
st.set_page_config(page_title="شاورما ع الصاج - VIP", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    /* خلفية بصور الوجبات مع تدرج أسود شفاف لإبراز النص */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(50, 0, 0, 0.85)), 
                    url('https://images.unsplash.com/photo-1594007654729-407eedc4be65?ixlib=rb-4.0.3&auto=format&fit=crop&w=1500&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .main-title {
        font-family: 'Cairo', sans-serif;
        font-size: 65px;
        text-align: center;
        color: #ff4b4b;
        text-shadow: 4px 4px 15px #000;
        margin-top: -50px;
    }
    .social-btns {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .social-icon {
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .insta { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
    .whats { background: #25d366; }
    
    /* تنسيق الكروت مع الصور */
    .menu-card {
        background: rgba(0, 0, 0, 0.7);
        padding: 0px;
        border-radius: 20px;
        border: 1px solid #ff4b4b;
        text-align: center;
        overflow: hidden; /* لإبقاء الصورة داخل القوس */
        transition: 0.3s;
    }
    .menu-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 10px 20px rgba(255, 75, 75, 0.3);
    }
    .card-image {
        width: 100%;
        height: 180px;
        object-fit: cover; /* لقص الصورة بشكل متناسب */
    }
    .card-content {
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. روابط التواصل الاجتماعي (أعلى الصفحة)
st.markdown("""
    <div class
