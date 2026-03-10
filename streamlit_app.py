import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | القمة", page_icon="🌯", layout="wide")

# إدارة حالة الموقع
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'admin_orders' not in st.session_state: st.session_state.admin_orders = []

# --- CSS (تنسيق البوابة والأقسام الضخمة) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية كما في الصورة */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; box-shadow: 0 0 30px rgba(255, 75, 75, 0.6);
    }
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; }

    /* الأقسام الجانبية - بلوكات ضخمة مرتبة */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 24px !important; font-weight: 900 !important;
        border: 2px solid #ff4b4b !important; margin-bottom: 15px; color: white !important;
    }

    /* كروت الطعام الضخمة */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; 
        padding: 40px; border-radius: 20px; margin-bottom: 30px; 
        text-align: right; direction: rtl; 
    }
    .item-name { font-size: 38px; font-weight: 900; color: #fff; }
    .item-price { font-size: 32px; color: #ff4b4b; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. البوابة الملكية (كما في 1000064174.heic) ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                👑 شاورما وبروستد ع الصاج.. جودة ملكية<br>
                📍 عمان - إربد - الزرقاء<br>
                📞 الخط الساخن: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col_lang, _ = st.columns([1, 3])
    with col_lang:
        st.markdown("<div style='display:flex; flex-direction:column; width:200px; margin-left:10%; margin-top:30px;'>", unsafe_allow_html=True)
        if st.button("دخول للمنيو 🇯🇴"): st.session_state.page = 'menu'; st.rerun()
        if st.button("English Menu 🇺🇸"): st.session_state.page = 'menu'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. المنيو المرتب صح ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

    with col_side:
        st.markdown("<h2 style='text-align:center;'>الأقسام</h2>", unsafe_allow_html=True)
        # الترتيب الجديد حسب طلبك
        category = st.radio("", [
            "🔥 العروض القوية",
            "🌯 شاورما (أحجام)",
            "👨‍👩‍👧‍👦 وجبات العيلة",
            "🍗 بروستد مقرمش",
            "🍟 قائمة الإضافات (جانبي)",
            "🥤 مشروبات"
        ])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        menu_items = {
            "🔥 العروض القوية": [
                ("أوفر الصحاب (2 سوبر)", 6.50, "2 ساندويش سوبر + بطاطا لارج + كولا"),
                ("عرض الـ 3 وجبات", 8.00, "3 وجبات عربي عادي + سرفيس كامل")
            ],
            "🌯 شاورما (أحجام)": [
                ("شاورما عادي", 1.85, "صاج أصلي"),
                ("شاورما سوبر", 2.75, "حجم أكبر"),
                ("شاورما تربل (العملاق)", 4.25, "ثلاث أضعاف الدجاج")
            ],
            "👨‍👩‍👧‍👦 وجبات العيلة": [
                ("السدر الملكي (شاورما)", 18.50, "64 قطعة + بطاطا دبل + كولا عائلي")
            ],
            "🍗 بروستد مقرمش": [
                ("بروستد 4 قطع", 4.25, "4 قطع + بطاطا + ثومية + كولا"),
                ("وليمة بروستد 21 قطعة", 18.50, "21 قطعة + بطاطا عائلية دبل + كولا 2 لتر")
            ],
            "🍟 قائمة الإضافات (جانبي)": [
                ("علبة بطاطا - كبير", 2.25, "حجم عائلي"),
                ("علبة مثومة - كبير", 1.00, "ثومية المحل الأصلية"),
                ("خلطة المحل الخاصة", 0.50, "صوص الصاج السري")
            ],
            "🥤 مشروبات": [("كولا / ماتريكس", 0.60, "بارد"), ("برتقال فريش", 1.75, "طبيعي")]
        }

        for name, price, desc in menu_items[category]:
            st.markdown(f"""
                <div class='menu-item-card'>
                    <div style='display:flex; justify-content:space-between; direction:ltr;'>
                        <span class='item-price'>{price:.2f} JOD</span>
                        <span class='item-name'>{name}</span>
                    </div>
                    <div style='color:#bbb;'>{desc}</div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("✨ تخصيص / إضافة للسلة"):
                note = st.text_input("ملاحظات خاصة", key=f"n_{name}")
                if st.button(f"إضافة {name}", key=f"b_{name}", use_container_width=True):
                    st.session_state.cart.append({'n': name, 'p': price, 'note': note})
                    st.session_state.total += price
                    st.toast("تمت الإضافة ✅")

    with col_cart:
        st.markdown("<div style='background:#000; padding:20px; border-radius:20px; border:1px solid #333;'>", unsafe_allow_html=True)
        st.header("🛒 السلة")
        for item in st.session_state.cart:
            st.write(f"🔹 **{item['n']}** ({item['p']:.2f})")
        
        st.divider()
        st.subheader(f"الحساب: {st.session_state.total:.2f} JOD")
        u_name = st.text_input("الاسم")
        u_phone = st.text_input("رقم الهاتف")

        if st.button("تأكيد الطلب 🚀", use_container_width=True):
            if u_name and u_phone:
                st.session_state.admin_orders.append({"customer": u_name, "items": st.session_state.cart})
                st.success("✅ تم الاستلام! طلبك تحت المعالجة.")
                st.session_state.cart = []; st.session_state.total = 0.0
                st.balloons()
            else: st.error("عبي بياناتك")
        
        if st.button("⬅️ عودة"): st.session_state.page='welcome'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
