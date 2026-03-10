import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | الإمبراطورية", page_icon="🌯", layout="wide")

# تهيئة حالة الجلسة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الملكي (بوابة + منيو ضخم) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1a0000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* البوكس العلوي للبوابة */
    .info-box {
        text-align: center;
        padding: 40px;
        background: rgba(0, 0, 0, 0.85);
        border: 2px solid #ff4b4b;
        border-radius: 25px;
        max-width: 800px;
        margin: 50px auto 20px auto;
        box-shadow: 0 0 30px rgba(255, 75, 75, 0.4);
    }
    .shop-title { font-size: clamp(40px, 5vw, 65px); font-weight: 900; color: #ff4b4b; margin-bottom: 10px; text-shadow: 0 0 15px #ff4b4b; }
    .shop-details { font-size: 20px; color: #ccc; margin-bottom: 20px; }

    /* أزرار اللغة */
    .lang-container { display: flex; flex-direction: column; align-items: center; max-width: 350px; margin: 0 auto; }
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        margin-bottom: 15px !important;
        border: none !important;
    }

    /* تصميم المنيو الراكز (بدون صور) */
    .menu-item {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #ff4b4b;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .menu-item:hover { background: rgba(255, 255, 255, 0.07); }
    .item-header { display: flex; justify-content: space-between; align-items: center; }
    .item-name { font-size: 24px; font-weight: bold; color: #fff; }
    .item-price { font-size: 22px; color: #ff4b4b; font-weight: 900; }
    .item-desc { color: #aaa; font-size: 16px; margin: 5px 0; }
    .nutrition { font-size: 14px; color: #00ffcc; font-weight: bold; }

    /* نظام السكرول */
    .scroll-container { max-height: 800px; overflow-y: auto; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: البوابة الملكية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                المذاق الإمبراطوري الأصيل 👑<br>
                📍 الأفرع: عمان | إربد | الزرقاء | العقبة<br>
                📞 الخط الساخن: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='lang-container'>", unsafe_allow_html=True)
    if st.button("الدخول للقائمة العربية 🇯🇴"):
        st.session_state.lang = 'Ar'; st.session_state.page = 'menu'; st.rerun()
    if st.button("Enter English Menu 🇺🇸"):
        st.session_state.lang = 'En'; st.session_state.page = 'menu'; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثانية: المنيو الإمبراطوري الضخم ---
elif st.session_state.page == 'menu':
    L = st.session_state.lang
    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{'القائمة الإمبراطورية الشاملة 👑' if L=='Ar' else 'Imperial Grand Menu 👑'}</h1>", unsafe_allow_html=True)
    
    col_menu, col_cart = st.columns([2.5, 1])

    with col_menu:
        tabs = st.tabs(["🌯 الشاورما والفرط", "🍔 الزنجر والتندر", "🍗 الأجنحة والبونليس", "🥗 الشيش طاووق", "🥤 المشروبات"])
        
        # --- 1. الشاورما والفرط ---
        with tabs[0]:
            st.markdown("<div class='scroll-container'>", unsafe_allow_html=True)
            items = [
                ("سدر العيلة الإمبراطوري", 18.50, "60 قطعة شاورما، بطاطا عائلية، 4 ثومية، لتر ونصف كولا", "بروتين: 180غ | دهون: 95غ"),
                ("وجبة شاورما فرط (250 غرام)", 5.50, "قطع شاورما صافية بدون خبز مع سرفيس كامل", "بروتين: 45غ | دهون: 22غ"),
                ("ساندويش شاورما صاج سوبر", 3.75, "خبز الصاج المقرمش، ثومية، مخلل", "بروتين: 32غ | دهون: 15غ"),
                ("وجبة عربي دبل", 5.50, "ساندويشين مقطعين، بطاطا، مقبلات", "بروتين: 55غ | دهون: 28غ")
            ]
            for n, p, d, nut in items:
                st.markdown(f"<div class='menu-item'><div class='item-header'><span class='item-name'>{n}</span><span class='item-price'>{p} JOD</span></div><div class='item-desc'>{d}</div><div class='nutrition'>📊 {nut}</div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n): st.session_state.cart.append({'n':n, 'p':p}); st.session_state.total += p; st.toast("✅")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- 2. الزنجر والتندر ---
        with tabs[1]:
            items = [
                ("ساندويش زنجر سوبريم", 3.50, "صدر دجاج حار، جبنة، خس، صوص خاص", "بروتين: 28غ | دهون: 18غ"),
                ("وجبة تندر (5 قطع)", 4.50, "قطع تندر ذهبية، بطاطا، صوص هني ماسترد", "بروتين: 35غ | دهون: 20غ"),
                ("وجبة زنجر عائلية", 14.00, "12 قطعة زنجر، بطاطا، لتر كولا، صوصات", "بروتين: 110غ | دهون: 65غ")
            ]
            for n, p, d, nut in items:
                st.markdown(f"<div class='menu-item'><div class='item-header'><span class='item-name'>{n}</span><span class='item-price'>{p} JOD</span></div><div class='item-desc'>{d}</div><div class='nutrition'>📊 {nut}</div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n): st.session_state.cart.append({'n':n, 'p':p}); st.session_state.total += p

        # --- 3. الأجنحة والبونليس ---
        with tabs[2]:
            items = [
                ("أجنحة دجاج بافلو (12 قطعة)", 5.50, "أجنحة مقلية مغطاة بصوص البافلو الحار", "بروتين: 40غ | دهون: 30غ"),
                ("بونليس دجاج (10 قطع)", 4.75, "قطع دجاج بدون عظم مع صوص باربيكيو", "بروتين: 38غ | دهون: 18غ"),
                ("وجبة أجنحة مقرمشة", 6.00, "أجنحة مع بطاطا وصوص ثوم", "بروتين: 42غ | دهون: 32غ")
            ]
            for n, p, d, nut in items:
                st.markdown(f"<div class='menu-item'><div class='item-header'><span class='item-name'>{n}</span><span class='item-price'>{p} JOD</span></div><div class='item-desc'>{d}</div><div class='nutrition'>📊 {nut}</div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n): st.session_state.cart.append({'n':n, 'p':p}); st.session_state.total += p

        # --- 4. الشيش طاووق ---
        with tabs[3]:
            items = [
                ("وجبة شيش طاووق ملكي", 5.25, "أسياخ شيش مشوية، أرز، بطاطا، ثومية", "بروتين: 48غ | دهون: 14غ"),
                ("ساندويش شيش طاووق صاج", 3.25, "قطع شيش، مخلل، ثومية، بطاطا داخلية", "بروتين: 28غ | دهون: 10غ")
            ]
            for n, p, d, nut in items:
                st.markdown(f"<div class='menu-item'><div class='item-header'><span class='item-name'>{n}</span><span class='item-price'>{p} JOD</span></div><div class='item-desc'>{d}</div><div class='nutrition'>📊 {nut}</div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n): st.session_state.cart.append({'n':n, 'p':p}); st.session_state.total += p

        # --- 5. المشروبات والعصائر ---
        with tabs[4]:
            items = [
                ("عصير برتقال طبيعي (فريش)", 1.75, "عصر يدوي طازج 100%", "بروتين: 1غ | دهون: 0غ"),
                ("مشروبات غازية (ماتريكس/كولا)", 0.60, "بارد منعش لتر/عبوة", "بروتين: 0غ | دهون: 0غ"),
                ("مياه معدنية", 0.35, "عبوة صغيرة", "بروتين: 0غ | دهون: 0غ")
            ]
            for n, p, d, nut in items:
                st.markdown(f"<div class='menu-item'><div class='item-header'><span class='item-name'>{n}</span><span class='item-price'>{p} JOD</span></div><div class='item-desc'>{d}</div><div class='nutrition'>📊 {nut}</div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {n}", key=n): st.session_state.cart.append({'n':n, 'p':p}); st.session_state.total += p

    # --- السلة والحساب (ثابتة في الجانب) ---
    with col_cart:
        st.markdown("<div style='background:rgba(255,75,75,0.1); padding:20px; border-radius:20px; border:1px solid #ff4b4b;'>", unsafe_allow_html=True)
        st.header("🛒 السلة الملكية")
        if not st.session_state.cart: st.write("سلتك فارغة..")
        for i, item in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {item['n']} - {item['p']:.2f} JOD")
        st.divider()
        st.subheader(f"الإجمالي: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            name = st.text_input("اسم العميل")
            phone = st.text_input("رقم الهاتف")
            method = st.radio("طريقة الدفع", ["كاش", "فيزا (تبرع بالبقشيش للكابتن)"])
            if st.button("تأكيد الطلب وإرسال الموقع 🚀"):
                if name and phone:
                    st.success(f"تم الاستلام يا {name}! سيتم التواصل معك فوراً."); st.balloons()
                else: st.error("يرجى إدخال البيانات")
        
        if st.button("🔄 تفريغ السلة"): st.session_state.cart=[]; st.session_state.total=0.0; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("⬅️ عودة للبوابة"): st.session_state.page = 'welcome'; st.rerun()

st.markdown("<center style='margin-top:50px; opacity:0.6;'>📍 شاورما ع الصاج - جميع الحقوق محفوظة 2026</center>", unsafe_allow_html=True)
