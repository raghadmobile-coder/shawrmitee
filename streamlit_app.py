import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

# تهيئة حالة الجلسة للتنقل واللغة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'

# تصميم CSS مخصص لواجهة البوابة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #2d0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* تنسيق البوكس العلوي الذي كان فارغاً */
    .info-box {
        text-align: center;
        padding: 40px;
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #ff4b4b; /* الإطار الأحمر المضيء */
        border-radius: 25px;
        max-width: 800px;
        margin: 50px auto 20px auto;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.5);
    }

    .shop-title {
        font-size: 50px;
        font-weight: 900;
        color: #ff4b4b;
        margin-bottom: 5px;
        text-shadow: 2px 2px 10px rgba(255, 75, 75, 0.8);
    }

    .shop-details {
        font-size: 18px;
        color: #ddd;
        line-height: 1.6;
    }

    /* حاوية أزرار اللغة أسفل البوكس */
    .lang-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 300px;
        margin: 0 auto;
    }

    /* تنسيق الأزرار لتكون فوق بعضها */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        margin-bottom: 10px !important;
        transition: 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# عرض بوابة الدخول
if st.session_state.page == 'welcome':
    # البوكس العلوي الذي يحتوي على الاسم والتفاصيل
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                الطعم الأصيل.. الجودة الملكية 👑<br>
                📍 فروعنا: عمان - إربد - الزرقاء<br>
                📞 للطلب والتوصيل: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)

    # حاوية أزرار اللغة (فوق بعضها)
    st.markdown("<div class='lang-container'>", unsafe_allow_html=True)
    
    if st.button("القائمة العربية 🇯🇴"):
        st.session_state.lang = 'Ar'
        st.session_state.page = 'menu'
        st.rerun()
    
    if st.button("English Menu 🇺🇸"):
        st.session_state.lang = 'En'
        st.session_state.page = 'menu'
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)

# بقية الكود الخاص بالمنيو يوضع هنا...
