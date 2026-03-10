import streamlit as st
import urllib.parse

# إعدادات الصفحة والرقم
MY_PHONE = "+962799633096"
st.set_page_config(page_title="Shawarma Al-Saj | القمة", page_icon="🌯", layout="wide")

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التعديلات الكبيرة (تكبير الأصناف الجانبية والكروت) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #2d0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الأصلية (البوكس في المنتصف) */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; box-shadow: 0 0 30px rgba(255, 75, 75, 0.6); 
    }
    .shop-title { font-size: 45px; font-weight: 900; color: #ff4b4b; margin-bottom: 10px; }

    /* تكبير قائمة الأصناف الجانبية (البلوكات على اليسار) */
    [data-testid="stSidebar"] { background-color: rgba(0,0,0,0.5); }
    .stRadio div[role="radiogroup"] { gap: 15px; }
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        border: 1px solid #ff4b4b !important;
        padding: 20px !important;
        border-radius: 15px !important;
        font-size: 22px !important; /* تكبير حجم الخط للأصناف */
        font-weight: bold !important;
        transition: 0.3s;
        width: 100%;
    }
    .stRadio div[role="radiogroup"] label:hover { background: rgba(255, 75, 75, 0.3) !important; }

    /* كروت الطعام الضخمة */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 8px solid #ff4b4b; 
        padding: 40px; border-radius: 20px; margin-bottom: 25px; 
        text-align: right; direction: rtl; 
    }
    .item-name { font-size: 35px; font-weight: 900; color: #fff; }
    .item-price { font-size: 30px; color: #ff4b4b; font-weight: 900; }
    .item-desc { font-size: 20px; color: #bbb; margin-bottom: 15px; }

    /* تنسيق خيارات الإضافات */
    .stCheckbox label { font-size: 18px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- البوابة الملكية ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='info-box'><div class='shop-title'>SHAWARMA AL-SAJ</div><div class='shop-details'>👑 الطعم الأصيل.. الجودة الملكية<br>📍 عمان - إربد - الزرقاء<br>📞 رقم التلفون: 079-0000000</div></div>", unsafe_allow_html=True)
    col_l, _ = st.columns([1, 3])
    with col_l:
        st.markdown("<div style='margin-left:8%; margin-top:20px;'>", unsafe_allow_html=True)
        if st.button("القائمة العربية 🇯🇴", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
        if st.button("English Menu 🇺🇸", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- المنيو المطور مع الإضافات والتعليقات ---
elif st.session_state.page == 'menu':
    col_sidebar, col_main, col_cart = st.columns([0.8, 2, 1.2])

    with col_sidebar:
        st.markdown("<h2 style='text-align:center;'>الأصناف</h2>", unsafe_allow_html=True)
        category = st.radio("", ["🌯 شاورما", "🍔 زنجر وتندر", "🍗 بونليس", "🥗 شيش طاووق", "🥤 مشروبات"])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        # بيانات المنيو
        items = {
            "🌯 شاورما": [("سدر العيلة الملكي", 18.50, "60 قطعة + سرفيس كامل"), ("عربي صاج سوبر", 3.75, "ساندويش ضخم + بطاطا")],
            "🍔 زنجر وتندر": [("زنجر سوبريم", 3.50, "صدر دجاج حار + جبنة"), ("تندر بوكس", 4.50, "5 قطع + صوص")],
            "🍗 بونليس": [("أجنحة بافلو", 5.50, "12 قطعة حارة"), ("بونليس باربيكيو", 4.75, "قطع بدون عظم")],
            "🥗 شيش طاووق": [("وجبة شيش ملكية", 5.25, "سيخين + أرز + بطاطا")],
            "🥤 مشروبات": [("برتقال فريش", 1.75, "طبيعي 100%"), ("مشروب غازي", 0.60, "بارد جداً")]
        }

        for name, price, desc in items[category]:
            st.markdown(f"""<div class='menu-item-card'>
                <div style='display:flex; justify-content:space-between; align-items:center; direction:ltr;'>
                    <span class='item-price'>{price} JOD</span>
                    <span class='item-name'>{name}</span>
                </div>
                <div class='item-desc'>{desc}</div>
            </div>""", unsafe_allow_html=True)
            
            # قسم الإضافات لكل وجبة
            with st.expander(f"✨ تخصيص الوجبة (إضافات وملاحظات)"):
                col_ex1, col_ex2 = st.columns(2)
                with col_ex1:
                    extra_cheese = st.checkbox("زيادة جبنة (+0.50 JOD)", key=f"ch_{name}")
                    extra_sauce = st.checkbox("زيادة ثومية (+0.25 JOD)", key=f"sc_{name}")
                with col_ex2:
                    no_pickles = st.checkbox("بدون مخلل", key=f"pk_{name}")
                    no_tomato = st.checkbox("بدون بندورة", key=f"tm_{name}")
                
                user_comment = st.text_input("📝 أي ملاحظة ثانية؟", placeholder="مثلاً: الخبز محمر زيادة...", key=f"com_{name}")
                
                if st.button(f"أضف {name} للسلة 🛒", key=f"btn_{name}", use_container_width=True):
                    final_price = price
                    extras = []
                    if extra_cheese: final_price += 0.50; extras.append("زيادة جبنة")
                    if extra_sauce: final_price += 0.25; extras.append("زيادة ثومية")
                    if no_pickles: extras.append("بدون مخلل")
                    if no_tomato: extras.append("بدون بندورة")
                    
                    st.session_state.cart.append({
                        'n': name, 'p': final_price, 'ex': extras, 'com': user_comment
                    })
                    st.session_state.total += final_price
                    st.toast(f"✅ تمت إضافة {name}")

    with col_cart:
        st.markdown("<div style='background:#000; padding:20px; border-radius:20px; border:1px solid #333;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ff4b4b; text-align:center;'>🛒 طلبك</h2>", unsafe_allow_html=True)
        if not st.session_state.cart: st.info("السلة فارغة")
        else:
            for item in st.session_state.cart:
                st.write(f"🔹 **{item['n']}** - {item['p']:.2f}")
                if item['ex']: st.caption(f"إضافات: {', '.join(item['ex'])}")
                if item['com']: st.caption(f"ملاحظة: {item['com']}")
            
            st.divider()
            st.subheader(f"الحساب: {st.session_state.total:.2f} JOD")
            c_name = st.text_input("اسمك")
            c_phone = st.text_input("تلفونك")
            c_loc = st.text_input("العنوان")
            
            if st.button("🚀 تأكيد عبر WhatsApp", use_container_width=True):
                if c_name and c_phone:
                    details = ""
                    for i in st.session_state.cart:
                        details += f"- {i['n']} ({i['p']} JOD)\n"
                        if i['ex']: details += f"   إضافات: {', '.join(i['ex'])}\n"
                        if i['com']: details += f"   ملاحظة: {i['com']}\n"
                    
                    msg = f"طلب جديد 🌯\n\n*الاسم:* {c_name}\n*الهاتف:* {c_phone}\n*العنوان:* {c_loc}\n\n*الطلبات:*\n{details}\n\n*الإجمالي:* {st.session_state.total:.2f} JOD"
                    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{MY_PHONE}?text={urllib.parse.quote(msg)}\'">', unsafe_allow_html=True)
                else: st.error("عبي اسمك ورقمك")
            
            if st.button("🗑️ تفريغ السلة", use_container_width=True):
                st.session_state.cart=[]; st.session_state.total=0.0; st.rerun()

        if st.button("⬅️ البوابة", use_container_width=True): st.session_state.page='welcome'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
