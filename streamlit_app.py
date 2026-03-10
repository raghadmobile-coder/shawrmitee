import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | المنيو الشامل", page_icon="🌯", layout="wide")

# إدارة حالة الموقع
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'admin_orders' not in st.session_state: st.session_state.admin_orders = [] # مخزن الطلبات للـ AI

# --- CSS (البوابة الأصلية + تكبير الأقسام والكروت) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية كما في الصورة */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; 
    }
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; }

    /* أزرار اللغة - يسار الشاشة */
    .lang-container { display: flex; flex-direction: column; width: 200px; margin-left: 10%; margin-top: 30px; }
    .stButton > button { width: 100% !important; border-radius: 12px !important; font-weight: bold !important; padding: 12px !important; }

    /* الأصناف الجانبية - بلوكات ضخمة */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 7
    
