import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | نظام الطلب الملكي", page_icon="🌯", layout="wide")

# 2. تهيئة حالة الجلسة (Session State)
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الاحترافي والحركات ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* خلفية متحركة واهتزازية خفيفة */
    .stApp {
        background: linear-gradient(45deg, #1a0000, #000000, #2d0000);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
        font-family: 'Cairo', sans-serif;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* بوابة اللغة */
    .welcome-box {
        text-align: center;
        padding: 100px 20px;
        background: rgba(0,0,0,0.6);
        border-radius: 30px;
        border: 2px solid #ff4b4b;
    }

    /* كروت المنيو */
    .menu-card {
        background: rgba(20, 20, 20, 0.95);
        border: 1px solid #ff4b4b;
        border-radius: 20px;
        margin-bottom: 20px;
        transition: 0.3s;
        text-align: center;
    }
    .menu-card:hover { transform: scale(1.02); box-shadow: 0 0 20px #ff4b4b; }
    .item-img { width: 100%; height: 200px; object-fit: cover; border-radius: 20px 20px 0 0; }
    
    /* السلة */
    .cart-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- وظائف المساعدة ---
def add_to_cart(name, price):
    st.session_state.cart.append({'name': name, 'price': price})
    st.session_state.total += price
    st.toast(f"✅ تمت إضافة {name} للسلة")

# --- الصفحة الأولى: بوابة اللغة ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:60px; color:#ff4b4b;'>SHAWARMA AL-SAJ</h1>", unsafe_allow_html=True)
    st.markdown("<h3>اختر لغة القائمة / Choose Menu Language</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("العربية 🇯🇴", use_container_width=True):
            st.session_state.page = 'menu'
            st.rerun()
    with col2:
        if st.button("English 🇺🇸", use_container_width=True):
            st.session_state.page = 'menu'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثانية: المنيو والسلة ---
elif st.session_state.page == 'menu':
    st.title("🌯 منيو شاورما ع الصاج الملكي")
    
    col_menu, col_cart = st.columns([2, 1])

    with col_menu:
        tabs = st.tabs(["👑 السدر الملكي", "🌯 الشاورما العربي", "🍗 البروستد", "🥤 المشروبات"])
        
        # 1. السدر الملكي (صورة جديدة فخمة)
        with tabs[0]:
            st.markdown("""
                <div class='menu-card'>
                    <img src='https://images.unsplash.com/photo-1544124499-58912cbddaad?w=800' class='item-img' style='height:400px;'>
                    <div style='padding:20px;'>
                        <h2>سدر العيلة الإمبراطوري 👑</h2>
                        <p>60 قطعة شاورما + 4 أنواع ثومية + بطاطا عائلية + لتر ونصف كولا</p>
                        <h3 style='color:#ff4b4b;'>18.50 JOD</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("إضافة السدر للملكي 🛒"): add_to_cart("سدر العيلة الإمبراطوري", 18.50)

        # 2. الشاورما العربي
        with tabs[1]:
            c1, c2 = st.columns(2)
            items = [
                ("وجبة عربي سوبر", 3.75, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=500"),
                ("وجبة دبل صاج", 5.50, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=500")
            ]
            for i, (name, price, img) in enumerate(items):
                with [c1, c2][i]:
                    st.markdown(f"<div class='menu-card'><img src='{img}' class='item-img'><h4>{name}</h4><h4 style='color:#ff4b4b;'>{price} JOD</h4></div>", unsafe_allow_html=True)
                    if st.button(f"أضف {name}", key=name): add_to_cart(name, price)

        # 3. البروستد (صورة 4 قطع)
        with tabs[2]:
            st.markdown("""
                <div class='menu-card'>
                    <img src='https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=500' class='item-img'>
                    <h4>وجبة بروستد 4 قطع كريسبي</h4>
                    <h4 style='color:#ff4b4b;'>4.95 JOD</h4>
                </div>
            """, unsafe_allow_html=True)
            if st.button("أضف وجبة بروستد"): add_to_cart("وجبة بروستد 4 قطع", 4.95)

        # 4. المشروبات (ماتريكس وعصير برتقال)
        with tabs[3]:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("<div class='menu-card'><img src='https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500' class='item-img'><h4>مشروب غازي (ماتريكس/كولا)</h4><h4>0.60 JOD</h4></div>", unsafe_allow_html=True)
                if st.button("أضف مشروب غازي"): add_to_cart("مشروب غازي", 0.60)
            with c2:
                st.markdown("<div class='menu-card'><img src='https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500' class='item-img'><h4>عصير برتقال طبيعي</h4><h4>1.75 JOD</h4></div>", unsafe_allow_html=True)
                if st.button("أضف عصير طبيعي"): add_to_cart("عصير برتقال", 1.75)

    # --- عمود السلة وإتمام الطلب ---
    with col_cart:
        st.markdown("<div class='cart-section'>", unsafe_allow_html=True)
        st.header("🛒 سلة الطلبات")
        for item in st.session_state.cart:
            st.write(f"- {item['name']} ({item['price']} JOD)")
        
        st.divider()
        st.subheader(f"الإجمالي: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            st.markdown("### 💳 طريقة الدفع")
            pay_method = st.radio("اختر الوسيلة:", ["كاش (عند الاستلام)", "فيزا / بطاقة ائتمان"])
            
            tip = 0.0
            if pay_method == "فيزا / بطاقة ائتمان":
                tip = st.number_input("إضافة بقشيش للكابتن (اختياري):", min_value=0.0, step=0.5)
                st.write(f"المجموع النهائي: {st.session_state.total + tip:.2f} JOD")

            st.markdown("### 📍 معلومات التوصيل")
            name = st.text_input("الاسم الكامل:")
            phone = st.text_input("رقم الهاتف (للمصداقية):")
            address = st.text_area("تفاصيل الموقع (الشارع، البناء):")
            
            if st.button("تأكيد الطلب وإرسال الموقع 🚀"):
                if name and phone and address:
                    st.success(f"شكراً {name}! تم استلام طلبك وسيتم التواصل معك على {phone}")
                    st.balloons()
                else:
                    st.error("يرجى تعبئة كافة البيانات لإتمام الطلب.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🔄 تفريغ السلة"):
            st.session_state.cart = []
            st.session_state.total = 0.0
            st.rerun()

st.markdown("<center>📍 جميع الحقوق محفوظة لـ شاورما ع الصاج 2024</center>", unsafe_allow_html=True)
