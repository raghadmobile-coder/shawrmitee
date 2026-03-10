import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج - القمة", page_icon="🌯", layout="wide")

# 2. إدارة الحالة (الترحيب، السلة، الإجمالي)
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الاحترافي والحركات ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* خلفية متحركة */
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

    /* هيدر الترحيب - المربع الأحمر الجديد مع اللمعة */
    .header-box {
        text-align: center;
        padding: 40px;
        background: rgba(10, 0, 0, 0.9);
        border-radius: 30px;
        border: 2px solid #ff4b4b;
        position: relative;
        overflow: hidden; /* ضروري لحركة اللمعة */
        box-shadow: 0 10px 30px rgba(255, 75, 75, 0.3);
    }
    
    /* حركة اللمعة الاهتزازية (Shimmer Effect) */
    .header-box::after {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(to right, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0) 100%);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    .shimmer-title {
        font-size: 80px;
        font-weight: 900;
        background: linear-gradient(to right, #ff4b4b 20%, #ffffff 50%, #ff4b4b 80%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        text-shadow: 0 0 20px rgba(255, 75, 75, 0.5);
    }
    @keyframes shine {
        to { background-position: 200% center; }
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
    
    /* أيقونات تواصل صغيرة */
    .social-icon { margin: 0 10px; font-size: 24px; text-decoration: none; color: white; }
    .contact-info { color: #ccc; font-size: 14px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: بوابة الدخول واللغة ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='header-box'>", unsafe_allow_html=True)
    
    # اسم المحل الوميض
    st.markdown("<h1 class='shimmer-title'>SHAWARMA AL-SAJ</h1>", unsafe_allow_html=True)
    
    # معلومات التواصل الفورية
    st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
    st.write("📞 الطلبات والتوصيل: 079-0000000")
    st.write("📍 الأفرع: عمان - شارع الجوعانين | إربد - دوار السعادة")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # أيقونات السوشيال ميديا
    st.markdown("<center><a href='#' class='social-icon'>📸 Instagram</a> <a href='#' class='social-icon'>💬 WhatsApp</a></center>", unsafe_allow_html=True)
    
    # بوابة اللغة
    st.divider()
    st.markdown("<h3 style='color:white;'>اختر لغة القائمة / Choose Menu Language</h3>", unsafe_allow_html=True)
    
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
        tabs = st.tabs(["🌟 العروض الملكية", "🌯 الشاورما العربي", "🥩 برغر الأنغوس البلدي", "🍗 البروستد كريسبي", "🥤 المشروبات"])
        
        # 1. العروض الملكية (صور دقيقة بحتة)
        with tabs[0]:
            st.markdown("""
                <div class='menu-card'>
                    <img src='https://images.unsplash.com/photo-1544124499-58912cbddaad?w=800' class='item-img' style='height:400px;'>
                    <div style='padding:20px;'>
                        <h2>سدر العيلة الإمبراطوري 👑</h2>
                        <p>60 قطعة شاورما دجاج صافي 100%، بطاطا عائلية كريسبي، سرفيس كامل (3 أنواع ثومية، مخلل مشكل، صوص حار)، لتر ونصف كولا.</p>
                        <h3 style='color:#ff4b4b;'>18.50 JOD</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("أضف السدر الإمبراطوري 🛒", key="king_offer"):
                st.session_state.cart.append({'name': 'سدر العيلة الإمبراطوري', 'price': 18.50})
                st.session_state.total += 18.50
                st.toast("✅ تم إضافة السدر")

        # 2. الشاورما العربي
        with tabs[1]:
            c1, c2 = st.columns(2)
            # داتا المنيو الدقيقة
            shaw_items = [
                ("ساندويش عربي سوبر", 3.75, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=500", "150غم دجاج في خبز عربي مقطع لـ 6 قطع"),
                ("وجبة دبل عربي (2 برغر)", 5.75, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=500", "2 ساندويش عربي عربي مع بطاطا")
            ]
            for i, (name, price, img, desc) in enumerate(shaw_items):
                with [c1, c2][i]:
                    st.markdown(f"""
                        <div class='menu-card'>
                            <img src='{img}' class='item-img'>
                            <div style='padding:10px;'>
                                <h4>{name}</h4>
                                <p style='color:#bbb; font-size:13px;'>{desc}</p>
                                <h4 style='color:#ff4b4b;'>{price} JOD</h4>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"أضف {name}", key=f"shaw_{i}"):
                        st.session_state.cart.append({'name': name, 'price': price})
                        st.session_state.total += price
                        st.toast(f"✅ تم إضافة {name}")

        # 3. برغر الأنغوس البلدي
        with tabs[2]:
            c1, c2 = st.columns(2)
            burger_items = [
                ("أنغوس تشيز ماستر", 4.75, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500", "180غم لحم أنغوس طازج، جبنة، صوص مدخن"),
                ("دبل تايتن برغر (300غم)", 6.50, "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500", "قطعتين لحم أنغوس (360غم) مضاعف الجبنة")
            ]
            for i, (name, price, img, desc) in enumerate(burger_items):
                with [c1, c2][i]:
                    st.markdown(f"""
                        <div class='menu-card'>
                            <img src='{img}' class='item-img'>
                            <div style='padding:10px;'>
                                <h4>{name}</h4>
                                <p style='color:#bbb; font-size:13px;'>{desc}</p>
                                <h4 style='color:#ff4b4b;'>{price} JOD</h4>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"أضف {name}", key=f"burger_{i}"):
                        st.session_state.cart.append({'name': name, 'price': price})
                        st.session_state.total += price
                        st.toast(f"✅ تم إضافة {name}")

        # 4. البروستد كريسبي (صورة الـ 4 قطع الدقيقة)
        with tabs[3]:
            st.markdown("""
                <div class='menu-card'>
                    <img src='https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=800' class='item-img' style='height:400px;'>
                    <div style='padding:20px;'>
                        <h2>وجبة بروستد (4 قطع)</h2>
                        <p>دجاج متبل بـ 11 بهار غير مجمد، يقدم مع بطاطا كريسبي، ثومية، وخبز طازج.</p>
                        <h3 style='color:#ff4b4b;'>4.95 JOD</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("أضف وجبة بروستد"):
                st.session_state.cart.append({'name': 'وجبة بروستد 4 قطع', 'price': 4.95})
                st.session_state.total += 4.95
                st.toast("✅ تم إضافة البروستد")

        # 5. المشروبات الثلجية (عصير طبيعي وماتريكس)
        with tabs[4]:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("<div class='menu-card'><img src='https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500' class='item-img'><h4>مشروب غازي (ماتريكس/كولا)</h4><h4>0.60 JOD</h4></div>", unsafe_allow_html=True)
                if st.button("أضف مشروب غازي"):
                    st.session_state.cart.append({'name': 'مشروب غازي', 'price': 0.60})
                    st.session_state.total += 0.60
                    st.toast("✅ تم إضافة مشروب غازي")
            with c2:
                st.markdown("<div class='menu-card'><img src='https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500' class='item-img'><h4>عصير برتقال طبيعي (فريش)</h4><h4>1.75 JOD</h4></div>", unsafe_allow_html=True)
                if st.button("أضف عصير طبيعي"):
                    st.session_state.cart.append({'name': 'عصير برتقال', 'price': 1.75})
                    st.session_state.total += 1.75
                    st.toast("✅ تم إضافة عصير طبيعي")

    # --- عمود السلة وإتمام الطلب ---
    with col_cart:
        st.markdown("<div class='cart-section'>", unsafe_allow_html=True)
        st.header("🛒 سلة الطلبات الملكية")
        if not st.session_state.cart:
            st.write("سلتك فارغة، أضف شيئاً يشهي!")
        for item in st.session_state.cart:
            st.write(f"- {item['name']} ({item['price']:.2f} JOD)")
        
        st.divider()
        st.subheader(f"الإجمالي: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            st.markdown("### 💳 طريقة الدفع وإتمام الطلب")
            pay_method = st.radio("اختر الوسيلة:", ["كاش (عند الاستلام)", "فيزا / بطاقة ائتمان"])
            
            # خيار البقشيش عند الفيزا
            tip = 0.0
            if pay_method == "فيزا / بطاقة ائتمان":
                tip = st.number_input("إضافة بقشيش للكابتن (اختياري):", min_value=0.0, step=0.5)
                st.write(f"المجموع النهائي: {st.session_state.total + tip:.2f} JOD")

            st.markdown("### 📍 معلومات العميل (للمصداقية)")
            st.write("يجب تزويدنا بالمعلومات التالية لإتمام التوصيل")
            
            # نموذج إرسال الموقع
            c_name = st.text_input("الاسم الكامل للعميل:")
            c_phone = st.text_input("رقم الهاتف الذكي (للتواصل معك):")
            st.markdown("**ملاحظة:** سنرسل لك رسالة لطلب 'موقعك المباشر' على الواتساب لضمان التوصيل الدقيق.")
            
            if st.button("تأكيد الطلب وإرسال للمطبخ 🏎️"):
                if c_name and c_phone:
                    st.success(f"شكراً {c_name}! تم تأكيد طلبك. الكابتن رح يتواصل معك على {c_phone} عشان ياخد الـ Access على موقعك.")
                    st.balloons()
                else:
                    st.error("يرجى تعبئة الاسم ورقم الهاتف للمصداقية.")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # تفريغ السلة
        if st.button("🔄 تفريغ السلة"):
            st.session_state.cart = []
            st.session_state.total = 0.0
            st.rerun()

st.markdown("<center>📍 جميع الحقوق محفوظة لـ شاورما ع الصاج 2024</center>", unsafe_allow_html=True)
