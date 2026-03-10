import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

# تهيئة حالة الجلسة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الملكي المحدث (البوابة في المنتصف) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #2d0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* البوابة المخصصة */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 50px;
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff4b4b;
        border-radius: 30px;
        max-width: 600px;
        margin: 100px auto;
        box-shadow: 0 0 30px rgba(255, 75, 75, 0.4);
    }

    .shimmer-title {
        font-size: 60px;
        font-weight: 900;
        color: #ff4b4b;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(255, 75, 75, 0.6);
    }

    .sub-text {
        font-size: 20px;
        color: #ddd;
        margin-bottom: 30px;
    }

    /* تنسيق الأزرار فوق بعضها */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        margin-bottom: 15px !important;
    }
    
    /* المنيو Scroll Area */
    .scroll-menu {
        max-height: 85vh;
        overflow-y: auto;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: بوابة اللغة (الخيارين فوق بعض) ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='welcome-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='shimmer-title'>SHAWARMA AL-SAJ</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>الطعم الأصيل.. الجودة الملكية<br>The Authentic Taste.. Royal Quality</p>", unsafe_allow_html=True)
    
    # الأزرار فوق بعضها
    if st.button("القائمة العربية 🇯🇴"):
        st.session_state.lang = 'Ar'
        st.session_state.page = 'menu'
        st.rerun()
    
    if st.button("English Menu 🇺🇸"):
        st.session_state.lang = 'En'
        st.session_state.page = 'menu'
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثانية: المنيو الإمبراطوري المتكامل ---
elif st.session_state.page == 'menu':
    L = st.session_state.lang
    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{'قائمة الطعام الملكية 👑' if L=='Ar' else 'The Royal Food Menu 👑'}</h1>", unsafe_allow_html=True)
    
    col_menu, col_cart = st.columns([2.2, 1])

    with col_menu:
        tabs = st.tabs(["👑 العروض الملكية", "🌯 الشاورما العربي", "🍗 البروستد والزنجر", "🍗 الأجنحة والبونليس", "🥤 المشروبات"])
        
        # 1. سدر العيلة (صورة فخمة مكبرة)
        with tabs[0]:
            st.markdown(f"""
                <div style='background:#111; border-radius:20px; border:1px solid #ff4b4b; overflow:hidden; margin-bottom:20px;'>
                    <img src='https://images.unsplash.com/photo-1544124499-58912cbddaad?w=1000' style='width:100%; height:450px; object-fit:cover;'>
                    <div style='padding:25px; text-align:center;'>
                        <h2>{"سدر العيلة الإمبراطوري" if L=='Ar' else "Imperial Family Tray"}</h2>
                        <p style='color:#bbb;'>60 قطعة شاورما، بطاطا عائلية، 4 أنواع ثومية، مخللات، كولا لتر ونصف</p>
                        <h3 style='color:#ff4b4b;'>18.50 JOD</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("أضف السدر الإمبراطوري 🛒"):
                st.session_state.cart.append({'n': 'سدر إمبراطوري', 'p': 18.50})
                st.session_state.total += 18.50
                st.toast("✅ Added to Cart")

        # 2. الشاورما (فرط وبالغرام)
        with tabs[1]:
            st.markdown("<div class='scroll-menu'>", unsafe_allow_html=True)
            shaw_items = [
                ("وجبة سوبر صاج عربي", 3.75, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=500", "ساندويش ضخم مقطع مع بطاطا وثومية"),
                ("شاورما فرط (250 غم)", 5.50, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=500", "قطع شاورما صافية مع سرفيس كامل"),
                ("شيش طاووق وجبة", 5.25, "https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=500", "أسياخ مشوية مع أرز وبطاطا")
            ]
            for n, p, img, desc in shaw_items:
                st.markdown(f"<div style='background:#1a1a1a; padding:15px; border-radius:15px; margin-bottom:15px;'><img src='{img}' style='width:100%; height:200px; object-fit:cover; border-radius:10px;'><h4>{n}</h4><p style='color:#888;'>{desc}</p><h4 style='color:#ff4b4b;'>{p} JOD</h4></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n):
                    st.session_state.cart.append({'n': n, 'p': p}); st.session_state.total += p
            st.markdown("</div>", unsafe_allow_html=True)

        # 3. الزنجر والتندر
        with tabs[2]:
            crispy_items = [
                ("ساندويش زنجر سوبريم", 3.50, "https://images.unsplash.com/photo-1610614819513-58e34989848b?w=500", "صدر دجاج حار مقرمش مع جبنة شيدر"),
                ("وجبة تندر (5 قطع)", 4.50, "https://images.unsplash.com/photo-1562967914-608f82629710?w=500", "قطع تندر ذهبية مع بطاطا وصوص")
            ]
            for n, p, img, desc in crispy_items:
                st.markdown(f"<div style='background:#1a1a1a; padding:15px; border-radius:15px; margin-bottom:15px;'><img src='{img}' style='width:100%; height:200px; object-fit:cover; border-radius:10px;'><h4>{n}</h4><p style='color:#888;'>{desc}</p><h4 style='color:#ff4b4b;'>{p} JOD</h4></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n):
                    st.session_state.cart.append({'n': n, 'p': p}); st.session_state.total += p

    # --- السلة والحساب ---
    with col_cart:
        st.markdown("<div style='background:rgba(255,255,255,0.05); padding:20px; border-radius:20px; border:1px solid #ff4b4b;'>", unsafe_allow_html=True)
        st.header("🛒 السلة الملكية")
        for i, item in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {item['n']} - {item['p']} JOD")
        st.divider()
        st.subheader(f"الإجمالي: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            name = st.text_input("اسم العميل")
            phone = st.text_input("رقم الهاتف")
            if st.button("إرسال الطلب 🏎️"):
                st.success(f"تم استلام طلبك يا {name}! جاري التجهيز."); st.balloons()
        
        if st.button("🔄 تفريغ السلة"):
            st.session_state.cart = []; st.session_state.total = 0.0; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅️ عودة للبوابة"): st.session_state.page = 'welcome'; st.rerun()
