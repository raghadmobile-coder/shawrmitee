import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | نظام الإدارة الملكي", page_icon="🌯", layout="wide")

# إدارة الحالة (الطلبات المخفية عن العميل)
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'confirmed_orders' not in st.session_state: st.session_state.confirmed_orders = [] # هاد اللي بشوفه الـ AI تبعك

# --- CSS (البوابة الأصلية 100% + تكبير المنيو) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية كما في الصورة */
    .info-box { 
        text-align: center; padding: 40px; background: rgba(0, 0, 0, 0.85); 
        border: 2px solid #ff4b4b; border-radius: 25px; max-width: 600px; 
        margin: 100px auto 20px auto; 
    }
    .shop-title { font-size: 45px; font-weight: 900; color: #ff4b4b; margin-bottom: 5px; }
    .shop-details { font-size: 16px; color: #ccc; }

    /* أزرار اللغة - يسار الشاشة تحت بعض */
    .lang-container { display: flex; flex-direction: column; width: 180px; margin-left: 10%; margin-top: 30px; }
    .stButton > button { width: 100% !important; border-radius: 10px !important; font-weight: bold !important; margin-bottom: 10px !important; }

    /* تكبير الأصناف الجانبية */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 24px !important; font-weight: 900 !important;
        border: 1px solid #ff4b4b !important; margin-bottom: 10px;
    }

    /* كروت الطعام الضخمة والواضحة */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; 
        padding: 45px; border-radius: 20px; margin-bottom: 30px; 
        text-align: right; direction: rtl; 
    }
    .item-name { font-size: 38px; font-weight: 900; color: #fff; }
    .item-price { font-size: 32px; color: #ff4b4b; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. البوابة الملكية (الرجوع للأصل) ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                👑 الطعم الأصيل.. الجودة الملكية<br>
                📍 فروعنا: عمان - إربد - الزرقاء<br>
                📞 للطلب والتوصيل: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_lang, _ = st.columns([1, 3])
    with col_lang:
        st.markdown("<div class='lang-container'>", unsafe_allow_html=True)
        if st.button("القائمة العربية 🇯🇴"): st.session_state.page = 'menu'; st.rerun()
        if st.button("English Menu 🇺🇸"): st.session_state.page = 'menu'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. المنيو الإمبراطوري (بدون تواصل مباشر مع واتساب العميل) ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

    with col_side:
        st.markdown("<h2 style='text-align:center;'>الأقسام</h2>", unsafe_allow_html=True)
        category = st.radio("", ["🌯 شاورما", "🍔 زنجر", "🍗 بونليس", "🥗 شيش", "🥤 مشروبات"])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        # داتا مبسطة للتجربة
        menu_items = {"🌯 شاورما": [("سدر عيلة", 18.50), ("عربي صاج", 3.75)], "🍔 زنجر": [("زنجر سوبريم", 3.50)], "🍗 بونليس": [("أجنحة", 5.50)], "🥗 شيش": [("وجبة شيش", 5.25)], "🥤 مشروبات": [("كولا", 0.60)]}

        for name, price in menu_items[category]:
            st.markdown(f"<div class='menu-item-card'><div style='display:flex; justify-content:space-between; direction:ltr;'><span class='item-price'>{price} JOD</span><span class='item-name'>{name}</span></div></div>", unsafe_allow_html=True)
            
            # خيارات التخصيص
            with st.expander("تخصيص الوجبة + ملاحظات"):
                extra_ch = st.checkbox("زيادة جبنة (+0.50)", key=f"ch_{name}")
                no_pk = st.checkbox("بدون مخلل", key=f"pk_{name}")
                comment = st.text_input("ملاحظاتك", key=f"c_{name}")
                
                if st.button(f"إضافة {name}", key=f"b_{name}", use_container_width=True):
                    p = price + (0.50 if extra_ch else 0)
                    st.session_state.cart.append({'n': name, 'p': p, 'notes': comment, 'extras': "جبنة" if extra_ch else ""})
                    st.session_state.total += p
                    st.toast("تمت الإضافة")

    with col_cart:
        st.markdown("<div style='background:#000; padding:20px; border-radius:20px; border:1px solid #333;'>", unsafe_allow_html=True)
        st.header("🛒 السلة")
        for item in st.session_state.cart:
            st.write(f"🔹 {item['n']} ({item['p']:.2f})")
        
        st.divider()
        st.subheader(f"الحساب: {st.session_state.total:.2f} JOD")
        
        u_name = st.text_input("الاسم")
        u_phone = st.text_input("رقم الهاتف")
        pay_method = st.selectbox("طريقة الدفع", ["كاش عند الاستلام", "محفظة إلكترونية"])

        if st.button("تأكيد الطلب نهائياً 🚀", use_container_width=True):
            if u_name and u_phone:
                # تخزين الطلب داخلياً للـ AI (بدون واتساب للعميل)
                order_data = {"customer": u_name, "phone": u_phone, "items": st.session_state.cart, "total": st.session_state.total}
                st.session_state.confirmed_orders.append(order_data)
                
                st.success("✅ تم استلام طلبك! سيقوم النظام بمعالجته فوراً.")
                st.session_state.cart = []; st.session_state.total = 0.0 # تصفير السلة
                st.balloons()
            else: st.error("عبي بياناتك")
        
        if st.button("تفريغ السلة"): st.session_state.cart=[]; st.session_state.total=0.0; st.rerun()
        if st.button("⬅️ البوابة"): st.session_state.page='welcome'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- قسم مخفي (لك أنت فقط) لرؤية الطلبات التي وصلت ---
if st.checkbox("لوحة تحكم الإدارة (مخفية)"):
    st.write("الطلبات الواردة للـ AI:", st.session_state.confirmed_orders)
