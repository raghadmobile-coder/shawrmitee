import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

# تهيئة حالة الجلسة (Session State) لضمان تفعيل اللغة والتنقل
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الاحترافي (Scroll & Shimmer) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: #0e1117;
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* الهيدر الوميض */
    .header-box {
        text-align: center;
        padding: 30px;
        background: rgba(255, 75, 75, 0.1);
        border: 2px solid #ff4b4b;
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.2);
    }
    
    .shimmer-text {
        font-size: 50px;
        font-weight: 900;
        color: #ff4b4b;
        text-shadow: 0 0 10px rgba(255, 75, 75, 0.5);
    }

    /* نظام الـ Scroll للمنيو */
    .menu-container {
        max-height: 800px;
        overflow-y: auto;
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.02);
    }

    .menu-card {
        background: #1c1f26;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #333;
        transition: 0.3s;
    }
    .menu-card:hover { border-color: #ff4b4b; transform: translateY(-5px); }
    
    .item-img {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 15px 15px 0 0;
    }
    
    .price-tag {
        color: #ff4b4b;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: بوابة اللغة (مفعلة بالكامل) ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='header-box'>", unsafe_allow_html=True)
    st.markdown("<h1 class='shimmer-text'>SHAWARMA AL-SAJ</h1>", unsafe_allow_html=True)
    st.write("📍 عمان - إربد - الزرقاء | 📞 079-0000000")
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("القائمة العربية 🇯🇴", use_container_width=True):
            st.session_state.lang = 'Ar'
            st.session_state.page = 'menu'
            st.rerun()
    with col2:
        if st.button("English Menu 🇺🇸", use_container_width=True):
            st.session_state.lang = 'En'
            st.session_state.page = 'menu'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثانية: المنيو المتكامل ---
elif st.session_state.page == 'menu':
    L = st.session_state.lang
    
    # نصوص اللغة
    txt = {
        'Ar': {'title': 'منيو شاورما ع الصاج الملكي', 'cart': 'سلة الطلبات', 'total': 'الإجمالي', 'checkout': 'تأكيد الطلب'},
        'En': {'title': 'Royal Shawarma Al-Saj Menu', 'cart': 'Your Cart', 'total': 'Total', 'checkout': 'Checkout'}
    }

    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{txt[L]['title']}</h1>", unsafe_allow_html=True)
    
    col_menu, col_cart = st.columns([2.5, 1])

    with col_menu:
        st.markdown("<div class='menu-container'>", unsafe_allow_html=True)
        
        # 🌟 سدر العيلة الملكي (الصورة الجديدة الاحترافية)
        st.markdown("### 👑 العروض الملكية")
        st.markdown(f"""
            <div class='menu-card'>
                <img src='https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=800' class='item-img'>
                <div style='padding:20px;'>
                    <h3>{"سدر العيلة الإمبراطوري" if L=='Ar' else "Imperial Family Tray"}</h3>
                    <p>{"60 قطعة شاورما عربي دجاج، بطاطا عائلية، 4 أنواع ثومية، مخلل، ولتر ونصف كولا." if L=='Ar' else "60 pcs Shawarma, Family Fries, 4 Dips, Pickles, & 1.5L Coke."}</p>
                    <span class='price-tag'>18.50 JOD</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("أضف السدر الملكي 🛒", key="king"):
            st.session_state.cart.append({'n': 'سدر ملكي', 'p': 18.50})
            st.session_state.total += 18.50
            st.toast("✅ Added!")

        # 🌯 الأصناف الأخرى (Scrollable)
        items = [
            ("وجبة صاج سوبر", 3.75, "https://images.unsplash.com/photo-1662145031215-9898246d60a5?w=500"),
            ("بروستد 4 قطع", 4.95, "https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=500"),
            ("عصير برتقال فريش", 1.75, "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500")
        ]
        
        for name, price, img in items:
            st.markdown(f"""
                <div class='menu-card'>
                    <img src='{img}' class='item-img'>
                    <div style='padding:15px;'>
                        <h4>{name}</h4>
                        <span class='price-tag'>{price} JOD</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"أضف {name}", key=name):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.toast("✅")
        
        st.markdown("</div>", unsafe_allow_html=True)

    with col_cart:
        st.markdown(f"### 🛒 {txt[L]['cart']}")
        for item in st.session_state.cart:
            st.write(f"- {item['n']} ({item['p']} JOD)")
        st.divider()
        st.subheader(f"{txt[L]['total']}: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            name = st.text_input("الاسم / Name")
            phone = st.text_input("الهاتف / Phone")
            if st.button(txt[L]['checkout']):
                st.success("تم استلام طلبك بنجاح!")
                st.balloons()

    if st.button("⬅️ Back / عودة"):
        st.session_state.page = 'welcome'
        st.rerun()
