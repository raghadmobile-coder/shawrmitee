import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

# 2. نظام إدارة "الحالة" (للانتقال من الترحيب للمنيو)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'lang' not in st.session_state:
    st.session_state.lang = None

# --- CSS للتصميم الـ 3D والخلفية المتحركة ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #4b0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* تصميم بوابة الترحيب */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        text-align: center;
    }

    .shimmer-title {
        font-size: 100px;
        font-weight: 900;
        color: rgba(255, 255, 255, 0.1);
        background: linear-gradient(to right, #ff4b4b 0, white 10%, #ff4b4b 20%);
        background-position: 0;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s infinite linear;
        animation-fill-mode: forwards;
        text-shadow: 0 0 30px rgba(255, 75, 75, 0.5);
    }

    @keyframes shimmer {
        0% { background-position: -500px; }
        100% { background-position: 500px; }
    }

    .glass-btn {
        background: rgba(255, 75, 75, 0.2);
        border: 2px solid #ff4b4b;
        padding: 15px 40px;
        border-radius: 50px;
        color: white;
        font-size: 24px;
        cursor: pointer;
        transition: 0.4s;
        backdrop-filter: blur(10px);
        margin: 10px;
    }

    /* كروت المنيو الاحترافية */
    .menu-card {
        background: rgba(20, 20, 20, 0.85);
        border: 1px solid #ff4b4b;
        border-radius: 25px;
        overflow: hidden;
        transition: 0.5s;
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
    }
    .menu-card:hover { transform: scale(1.05) rotate(1deg); border-color: white; }
    .item-img { width: 100%; height: 280px; object-fit: cover; }
    .card-body { padding: 20px; text-align: center; }
    .price-tag { color: #ff4b4b; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: بوابة الدخول ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class="welcome-container">
            <h1 class="shimmer-title">SHAWARMA AL-SAJ</h1>
            <h2 style="color: #ccc; letter-spacing: 5px;">شاورما ع الصاج</h2>
            <p style="font-size: 20px; margin-top: 20px;">Choose Your Language | اختر لغتك</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("العربية 🇯🇴", use_container_width=True):
            st.session_state.lang = 'Ar'
            st.session_state.page = 'menu'
            st.rerun()
    with col2:
        if st.button("English 🇺🇸", use_container_width=True):
            st.session_state.lang = 'En'
            st.session_state.page = 'menu'
            st.rerun()

# --- الصفحة الثانية: المنيو العملاق ---
elif st.session_state.page == 'menu':
    if st.session_state.lang == 'Ar':
        title, sub = "القائمة الملكية 👑", "نقدم لك أفضل جودة في المملكة"
        cats = ["🌟 العروض الملكية", "🌯 الشاورما", "🥩 برغر اللحم", "🍗 برغر الدجاج", "🥤 المشروبات"]
    else:
        title, sub = "Royal Menu 👑", "The Best Quality in Jordan"
        cats = ["🌟 Royal Offers", "🌯 Shawarma", "🥩 Beef Burgers", "🍗 Chicken Burgers", "🥤 Drinks"]

    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#ccc;'>{sub}</p>", unsafe_allow_html=True)

    # بيانات المنيو مع أعلى دقة صور
    menu_data = {
        cats[0]: [("سدر العيلة الملكي VIP", 18.50, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?q=90&w=1200", "48 قطعة، ثومية، بطاطا عائلية، لتر ونصف كولا")],
        cats[1]: [("وجبة سوبر صاج", 3.75, "https://images.unsplash.com/photo-1662145031215-9898246d60a5?q=90&w=1000", "خبز صاج، ثومية، مخلل، دجاج بلدي")],
        cats[2]: [("أنغوس تشيز ماستر", 4.75, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=90&w=1000", "180غم لحم أنغوس، جبنة شيدر، خبز بريوش")],
        cats[3]: [("زنجر سوبريم جلاكسي", 3.95, "https://images.unsplash.com/photo-1610614819513-58e34989848b?q=90&w=1000", "صدر دجاج كريسبي، تركي مدخن، صوص سبيشال")],
        cats[4]: [("ماتريكس كولا", 0.60, "https://images.unsplash.com/photo-1527960471264-932f39eb5846?q=90&w=1000", "بارد ومنعش")]
    }

    tabs = st.tabs(cats)
    for i, cat in enumerate(cats):
        with tabs[i]:
            cols = st.columns(2 if len(menu_data[cat]) > 1 else 1)
            for idx, item in enumerate(menu_data[cat]):
                with cols[idx % 2]:
                    st.markdown(f"""
                        <div class="menu-card">
                            <img src="{item[2]}" class="item-img">
                            <div class="card-body">
                                <h3>{item[0]}</h3>
                                <p style="color:#bbb;">{item[3]}</p>
                                <div class="price-tag">{item[1]:.2f} JOD</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"أضف {item[0]}", key=item[0]):
                        st.toast(f"✅ Added {item[0]}")

    if st.button("⬅️ Back to Language | العودة للغة"):
        st.session_state.page = 'welcome'
        st.rerun()

# --- الفوتر ---
st.markdown("---")
st.write("📍 Amman, Jordan | 📞 079-0000000")
