import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | القمة الملكية", page_icon="🌯", layout="wide")

# تهيئة حالة الجلسة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التصميم الفخم (Glassmorphism & Neon) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #330000 0%, #000000 100%);
        color: white;
        font-family: 'Cairo', sans-serif;
    }

    /* البوابة المطورة */
    .welcome-card {
        text-align: center;
        padding: 60px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 75, 75, 0.3);
        border-radius: 40px;
        backdrop-filter: blur(15px);
        margin-top: 50px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    .neon-title {
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        color: #fff;
        text-shadow: 0 0 10px #ff4b4b, 0 0 20px #ff4b4b, 0 0 40px #ff4b4b;
        margin-bottom: 10px;
    }

    /* أزرار اللغة */
    .lang-btn {
        background: linear-gradient(45deg, #ff4b4b, #a30000);
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        font-weight: bold !important;
        border: none !important;
        transition: 0.3s !important;
    }

    /* كروت المنيو الضخمة */
    .item-card {
        background: #111;
        border-radius: 25px;
        margin-bottom: 25px;
        border: 1px solid #222;
        overflow: hidden;
        transition: 0.4s;
    }
    .item-card:hover { border-color: #ff4b4b; transform: translateY(-10px); }
    .item-img { width: 100%; height: 280px; object-fit: cover; border-bottom: 3px solid #ff4b4b; }
    .price { color: #ff4b4b; font-size: 24px; font-weight: bold; }
    
    /* نظام السكرول */
    .scroll-area { max-height: 1000px; overflow-y: auto; padding-right: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: البوابة الملكية ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='neon-title'>SHAWARMA AL-SAJ</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='letter-spacing: 5px; color: #ddd;'>شاورما ع الصاج</h2>", unsafe_allow_html=True)
    st.write("📍 فروعنا تغطي المملكة | 📞 خدمة العملاء: 079-0000000")
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("القائمة العربية 🇯🇴", key="ar_btn", use_container_width=True):
            st.session_state.lang = 'Ar'; st.session_state.page = 'menu'; st.rerun()
    with c2:
        if st.button("English Menu 🇺🇸", key="en_btn", use_container_width=True):
            st.session_state.lang = 'En'; st.session_state.page = 'menu'; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثانية: المنيو الإمبراطوري ---
elif st.session_state.page == 'menu':
    L = st.session_state.lang
    st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{'القائمة الإمبراطورية 👑' if L=='Ar' else 'The Imperial Menu 👑'}</h1>", unsafe_allow_html=True)
    
    col_menu, col_cart = st.columns([2.5, 1])

    with col_menu:
        tabs = st.tabs(["🌯 الشاورما", "🍔 الزنجر والتندر", "🍗 الأجنحة والبونليس", "🥗 الشيش والفرط", "🥤 المشروبات"])
        
        # --- قسم الشاورما ---
        with tabs[0]:
            st.markdown("<div class='scroll-area'>", unsafe_allow_html=True)
            items = [
                ("سدر العيلة الملكي VIP", 18.50, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=800", "60 قطعة، بطاطا، 4 ثومية، كولا لتر ونص"),
                ("وجبة سوبر صاج عربي", 3.75, "https://images.unsplash.com/photo-1662145031215-9898246d60a5?w=500", "ساندويش ضخم مقطع، بطاطا، ثومية، مخلل"),
                ("شاورما صاج عائلي", 12.00, "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=500", "32 قطعة شاورما عربي مع كافة المقبلات")
            ]
            for name, price, img, desc in items:
                st.markdown(f"<div class='item-card'><img src='{img}' class='item-img'><div style='padding:20px;'><h3>{name}</h3><p style='color:#bbb;'>{desc}</p><span class='price'>{price} JOD</span></div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name): 
                    st.session_state.cart.append({'n': name, 'p': price}); st.session_state.total += price; st.toast("✅")

        # --- قسم الزنجر والتندر ---
        with tabs[1]:
            items = [
                ("ساندويش زنجر سوبريم", 3.50, "https://images.unsplash.com/photo-1610614819513-58e34989848b?w=500", "صدر دجاج حار، جبنة، خس، مايونيز سبيشال"),
                ("وجبة تندر 5 قطع", 4.50, "https://images.unsplash.com/photo-1562967914-608f82629710?w=500", "قطع تندر مقرمشة، بطاطا، صوص هني ماسترد"),
                ("برغر دجاج كريسبي", 3.25, "https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?w=500", "قطعة دجاج ضخمة، خبز بريوش، صوص الجبنة")
            ]
            for name, price, img, desc in items:
                st.markdown(f"<div class='item-card'><img src='{img}' class='item-img'><div style='padding:20px;'><h3>{name}</h3><p>{desc}</p><span class='price'>{price} JOD</span></div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name): st.session_state.cart.append({'n': name, 'p': price}); st.session_state.total += price

        # --- قسم الأجنحة والبونليس ---
        with tabs[2]:
            items = [
                ("أجنحة دجاج (12 قطعة)", 5.50, "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?w=500", "اختيارك من صوص (بافلو، باربيكيو، ثوم ولون)"),
                ("بونليس دجاج (بوكس)", 4.75, "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=500", "قطع دجاج بدون عظم مغطاة بالصوص الحار"),
            ]
            for name, price, img, desc in items:
                st.markdown(f"<div class='item-card'><img src='{img}' class='item-img'><div style='padding:20px;'><h3>{name}</h3><p>{desc}</p><span class='price'>{price} JOD</span></div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name): st.session_state.cart.append({'n': name, 'p': price}); st.session_state.total += price

        # --- قسم الشيش والفرط ---
        with tabs[3]:
            items = [
                ("وجبة شيش طاووق", 5.25, "https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=500", "أسياخ شيش مشوية على الصاج، أرز أو بطاطا، ثومية"),
                ("شاورما فرط (بالغرام)", 6.00, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=500", "250غم شاورما دجاج صافي مع سرفيس كامل")
            ]
            for name, price, img, desc in items:
                st.markdown(f"<div class='item-card'><img src='{img}' class='item-img'><div style='padding:20px;'><h3>{name}</h3><p>{desc}</p><span class='price'>{price} JOD</span></div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name): st.session_state.cart.append({'n': name, 'p': price}); st.session_state.total += price

        # --- قسم المشروبات ---
        with tabs[4]:
            items = [
                ("عصير برتقال فريش", 1.75, "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500", "طبيعي 100% بدون سكر مضاف"),
                ("ماتريكس كولا / مشروب غازي", 0.60, "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500", "بارد ومنعش")
            ]
            for name, price, img, desc in items:
                st.markdown(f"<div class='item-card'><img src='{img}' class='item-img'><div style='padding:20px;'><h3>{name}</h3><p>{desc}</p><span class='price'>{price} JOD</span></div></div>", unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name): st.session_state.cart.append({'n': name, 'p': price}); st.session_state.total += price
            
            st.markdown("</div>", unsafe_allow_html=True)

    # --- السلة والبيانات ---
    with col_cart:
        st.markdown("<div style='background:rgba(255,255,255,0.05); padding:20px; border-radius:20px;'>", unsafe_allow_html=True)
        st.header("🛒 السلة الملكية")
        for i, item in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {item['n']} - {item['p']} JOD")
        st.divider()
        st.subheader(f"الإجمالي: {st.session_state.total:.2f} JOD")
        
        if st.session_state.total > 0:
            name = st.text_input("اسم العميل")
            phone = st.text_input("رقم الهاتف")
            method = st.radio("طريقة الدفع", ["كاش", "فيزا (تبرع بالبقشيش للكابتن)"])
            if st.button("تأكيد الطلب وإرسال الموقع 🚀"):
                st.success(f"تم! شكرًا {name}، رح نتواصل معك فورًا."); st.balloons()
        
        if st.button("🔄 تفريغ السلة"): st.session_state.cart=[]; st.session_state.total=0.0; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅️ عودة للبوابة"): st.session_state.page = 'welcome'; st.rerun()

st.markdown("<center style='margin-top:50px; color:#666;'>📍 شاورما ع الصاج - الجودة شعارنا | 2026</center>", unsafe_allow_html=True)
