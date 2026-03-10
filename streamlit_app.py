import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

# 2. تهيئة حالة الجلسة (لضمان عمل التنقل بين الصفحات)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'lang' not in st.session_state:
    st.session_state.lang = 'Ar'
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'total' not in st.session_state:
    st.session_state.total = 0.0

# --- CSS التصميم (البوابة + المنيو) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #2d0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* تصميم البوكس العلوي للبوابة */
    .info-box {
        text-align: center;
        padding: 40px;
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #ff4b4b;
        border-radius: 25px;
        max-width: 800px;
        margin: 50px auto 20px auto;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.5);
    }

    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; margin-bottom: 5px; }
    .shop-details { font-size: 18px; color: #ddd; line-height: 1.6; }

    /* أزرار اللغة تحت بعض */
    .lang-container { display: flex; flex-direction: column; align-items: center; max-width: 300px; margin: 0 auto; }
    
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
    }

    /* تصميم كروت المنيو */
    .menu-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }
    .item-img { width: 100%; height: 200px; object-fit: cover; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- منطق الانتقال بين الصفحات ---

# الصفحة الأولى: بوابة الدخول
if st.session_state.page == 'welcome':
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

    st.markdown("<div class='lang-container'>", unsafe_allow_html=True)
    if st.button("القائمة العربية 🇯🇴"):
        st.session_state.lang = 'Ar'
        st.session_state.page = 'menu'
        st.rerun() # إعادة التشغيل لفتح المنيو فوراً
    
    if st.button("English Menu 🇺🇸"):
        st.session_state.lang = 'En'
        st.session_state.page = 'menu'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# الصفحة الثانية: المنيو (تفتح فقط بعد اختيار اللغة)
elif st.session_state.page == 'menu':
    L = st.session_state.lang
    title = "قائمة الطعام الملكية 👑" if L == 'Ar' else "Royal Food Menu 👑"
    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{title}</h1>", unsafe_allow_html=True)
    
    col_m, col_c = st.columns([2, 1])
    
    with col_m:
        # هنا تضع كل الوجبات (سدر، زنجر، بونليس...)
        st.subheader("🌟 الأصناف الأكثر طلباً")
        
        # مثال لوجبة (سدر العيلة)
        st.markdown(f"""
            <div class='menu-card'>
                <img src='https://images.unsplash.com/photo-1544124499-58912cbddaad?w=600' class='item-img'>
                <h3>{"سدر العيلة الملكي" if L=='Ar' else "Royal Family Tray"}</h3>
                <p>{"60 قطعة شاورما + بطاطا + كولا" if L=='Ar' else "60 pcs + Fries + Coke"}</p>
                <h4 style='color:#ff4b4b;'>18.50 JOD</h4>
            </div>
        """, unsafe_allow_html=True)
        if st.button("أضف للسلة 🛒", key="add_1"):
            st.session_state.cart.append("سدر ملكي")
            st.session_state.total += 18.50
            st.toast("تمت الإضافة!")

    with col_c:
        st.header("🛒 السلة")
        for item in st.session_state.cart:
            st.write(f"- {item}")
        st.divider()
        st.subheader(f"الحساب: {st.session_state.total:.2f} JOD")
        
        if st.button("⬅️ عودة للبوابة"):
            st.session_state.page = 'welcome'
            st.rerun()

st.markdown("<center style='opacity:0.5; margin-top:50px;'>© 2026 Shawarma Al-Saj</center>", unsafe_allow_html=True)
