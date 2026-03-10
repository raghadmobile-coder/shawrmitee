import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | الفخامة الملكية", page_icon="🌯", layout="wide")

# 2. إدارة الحالة (الترحيب ثم المنيو)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'lang' not in st.session_state:
    st.session_state.lang = None

# --- CSS التصميم الاحترافي 4K ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #2d0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* بوابة الترحيب */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
    }

    .shimmer-title {
        font-size: clamp(40px, 8vw, 100px);
        font-weight: 900;
        background: linear-gradient(to right, #ff4b4b 20%, #ffffff 50%, #ff4b4b 80%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        text-shadow: 0 0 20px rgba(255, 75, 75, 0.3);
    }

    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* كرت السدر الملكي (تصميم خاص) */
    .royal-card {
        background: rgba(30, 0, 0, 0.7);
        border: 3px solid #ff4b4b;
        border-radius: 40px;
        overflow: hidden;
        margin: 40px auto;
        max-width: 1000px;
        box-shadow: 0 0 50px rgba(255, 75, 75, 0.2);
    }
    .royal-img {
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-bottom: 5px solid #ff4b4b;
    }

    /* كروت المنيو العادية */
    .menu-card {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid rgba(255, 75, 75, 0.4);
        border-radius: 25px;
        overflow: hidden;
        transition: 0.4s;
        height: 100%;
    }
    .menu-card:hover {
        transform: translateY(-10px);
        border-color: #ff4b4b;
    }
    .item-img {
        width: 100%;
        height: 300px;
        object-fit: cover;
    }
    .card-body { padding: 25px; text-align: center; }
    .price-tag { 
        color: #ff4b4b; 
        font-size: 28px; 
        font-weight: bold; 
        background: rgba(255, 75, 75, 0.1);
        padding: 5px 20px;
        border-radius: 50px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- بوابة الترحيب واختيار اللغة ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class="welcome-container">
            <h1 class="shimmer-title">SHAWARMA AL-SAJ</h1>
            <p style="font-size: 24px; color: #ddd; letter-spacing: 2px;">مرحباً بك في عالم المذاق الأصيل</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("القائمة العربية 🇯🇴", use_container_width=True):
            st.session_state.lang = 'Ar'; st.session_state.page = 'menu'; st.rerun()
    with c2:
        if st.button("English Menu 🇺🇸", use_container_width=True):
            st.session_state.lang = 'En'; st.session_state.page = 'menu'; st.rerun()

# --- صفحة المنيو ---
elif st.session_state.page == 'menu':
    lang = st.session_state.lang
    
    # محتوى السدر الملكي (الصورة والوصف)
    royal_title = "سدر العيلة الإمبراطوري 👑" if lang == 'Ar' else "Imperial Family Tray 👑"
    # رابط صورة سدر احترافي جداً (شاورما عربي مرتبة)
    royal_img_url = "https://images.unsplash.com/photo-1561651823-34feb02250e4?q=80&w=1200" # صورة شاورما عربي دقيقة
    royal_desc = (
        "سدر ملكي ضخم يحتوي على 60 قطعة شاورما دجاج (صافي)، "
        "بطاطا عائلية كريسبي، 4 أنواع ثومية (عادية، حارة، مدخنة، كاري)، "
        "مخللات بيتية، ولتر ونصف كولا." 
        if lang == 'Ar' else 
        "Huge tray with 60 pcs of Shawarma, family fries, 4 types of garlic dip, pickles, and 1.5L Coke."
    )

    st.markdown(f"<h1 style='text-align:center; font-size:50px;'>{royal_title}</h1>", unsafe_allow_html=True)

    # عرض السدر الملكي بكرت ضخم
    st.markdown(f"""
        <div class="royal-card">
            <img src="{royal_img_url}" class="royal-img">
            <div class="card-body">
                <p style="font-size: 22px; color: #ddd; line-height: 1.8;">{royal_desc}</p>
                <div class="price-tag">18.50 JOD</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔥 اطلب السدر الملكي الآن / Order Now", use_container_width=True):
        st.balloons()
        st.toast("✅ تم إضافة طلب الملوك")

    # باقي المنيو (أقسام مرنة)
    st.markdown("---")
    tabs = st.tabs(["🌯 الوجبات", "🍔 البرغر", "🍗 البروستد", "🥤 المشروبات"])
    
    with tabs[0]: # الشاورما
        col1, col2 = st.columns(2)
        items = [
            ("وجبة دبل صاج", 5.50, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=800", "2 ساندويش صاج ضخم + بطاطا + مشروب"),
            ("وجبة سوبر كلاسيك", 3.75, "https://images.unsplash.com/photo-1644704078230-07e750f78937?w=800", "ساندويش صاج مقطع + ثومية ومخلل")
        ]
        for i, (name, price, img, dsc) in enumerate(items):
            with [col1, col2][i]:
                st.markdown(f"""<div class="menu-card"><img src="{img}" class="item-img"><div class="card-body"><h3>{name}</h3><p>{dsc}</p><div class="price-tag">{price:.2f} JOD</div></div></div>""", unsafe_allow_html=True)
                st.button(f"أضف {name}", key=name)

    if st.button("⬅️ تغيير اللغة / Change Language"):
        st.session_state.page = 'welcome'; st.rerun()

# --- الفوتر ---
st.markdown("<br><hr><center>📍 عمان - شارع المدينة | 📞 0790000000 | 📸 @Saj_Shawarma</center>", unsafe_allow_html=True)
