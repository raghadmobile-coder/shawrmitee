import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | القمة", page_icon="🌯", layout="wide")

# 2. إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'lang' not in st.session_state: st.session_state.lang = 'Ar'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS المطور (نظام البلوكات الجانبية وتنسيق المحتوى) ---
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
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; margin-bottom: 10px; }

    /* تنسيق كروت الطعام - الكتابة من اليمين */
    .menu-item-card {
        background: rgba(255, 255, 255, 0.03);
        border-right: 5px solid #ff4b4b; /* الإشارة يمين */
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        text-align: right; /* المحاذاة لليمين */
        direction: rtl;
        transition: 0.3s;
    }
    .menu-item-card:hover { background: rgba(255, 255, 255, 0.08); transform: translateX(-5px); }
    .item-name { font-size: 24px; font-weight: bold; color: #fff; display: block; }
    .item-price { font-size: 22px; color: #ff4b4b; font-weight: 900; }
    .nutrition-label { font-size: 14px; color: #00ffcc; display: block; margin-top: 10px; }

    /* السلة المطورة */
    .cart-container {
        background: #000;
        border: 1px solid #333;
        border-radius: 20px;
        padding: 25px;
        position: sticky;
        top: 20px;
    }
    .cart-header { color: #ff4b4b; border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 20px; text-align: center; }

    /* زر تفريغ السلة (تصميم زجاجي) */
    .clear-btn {
        background: rgba(255, 75, 75, 0.1) !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
    }
    
    /* نظام البلوكات الجانبية للتحكم */
    .stRadio [data-testid="stWidgetLabel"] { display: none; }
    div[data-testid="stVerticalBlock"] > div:has(div.stRadio) {
        background: rgba(255,255,255,0.05);
        padding: 10px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- منطق الصفحات ---

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

    col_l, col_r = st.columns(2)
    with col_l:
        if st.button("القائمة العربية 🇯🇴", use_container_width=True):
            st.session_state.lang = 'Ar'; st.session_state.page = 'menu'; st.rerun()
    with col_r:
        if st.button("English Menu 🇺🇸", use_container_width=True):
            st.session_state.lang = 'En'; st.session_state.page = 'menu'; st.rerun()

elif st.session_state.page == 'menu':
    # --- تصميم المحتوي بنظام البلوكات الجانبية على اليسار ---
    col_sidebar, col_main, col_cart = st.columns([0.8, 2, 1.2])

    with col_sidebar:
        st.markdown("<h3 style='text-align:center;'>🗂️ الأصناف</h3>", unsafe_allow_html=True)
        category = st.radio("", ["🌯 شاورما وفرط", "🍔 زنجر وتندر", "🍗 بونليس وأجنحة", "🥗 شيش طاووق", "🥤 مشروبات"])

    with col_main:
        st.markdown(f"<h2 style='text-align:right;'>{category}</h2>", unsafe_allow_html=True)
        
        # داتا المنيو
        menu_data = {
            "🌯 شاورما وفرط": [
                ("سدر العيلة الإمبراطوري", 18.50, "60 قطعة شاورما، بطاطا، كولا"، "بروتين: 180غ | دهون: 95غ"),
                ("وجبة شاورما فرط (250غ)", 5.50, "شاورما صافية مع سرفيس كامل", "بروتين: 45غ | دهون: 22غ"),
                ("عربي صاج سوبر", 3.75, "ساندويش ضخم مقطع، بطاطا، ثومية", "بروتين: 32غ | دهون: 15غ")
            ],
            "🍔 زنجر وتندر": [
                ("زنجر سوبريم", 3.50, "صدر دجاج حار، جبنة، صوص خاص", "بروتين: 28غ | دهون: 18غ"),
                ("تندر بوكس (5 قطع)", 4.50, "قطع مقرمشة، بطاطا، هني ماسترد", "بروتين: 35غ | دهون: 20غ")
            ],
            "🍗 بونليس وأجنحة": [
                ("أجنحة بافلو (12 قطعة)", 5.50, "صوص حار، ثومية، بطاطا", "بروتين: 40غ | دهون: 30غ"),
                ("بونليس باربيكيو", 4.75, "قطع بدون عظم بصوص الباربيكيو", "بروتين: 38غ | دهون: 18غ")
            ],
            "🥗 شيش طاووق": [
                ("وجبة شيش ملكية", 5.25, "أسياخ مشوية، أرز، بطاطا", "بروتين: 48غ | دهون: 14غ")
            ],
            "🥤 مشروبات": [
                ("عصير برتقال فريش", 1.75, "طبيعي 100%", "بروتين: 1غ"),
                ("مشروب غازي", 0.60, "بارد ومنعش", "00")
            ]
        }

        for name, price, desc, nut in menu_data[category]:
            st.markdown(f"""
                <div class='menu-item-card'>
                    <div style='display:flex; justify-content:space-between; align-items:center; direction:ltr;'>
                        <span class='item-price'>{price} JOD</span>
                        <span class='item-name'>{name}</span>
                    </div>
                    <div class='item-desc'>{desc}</div>
                    <div class='nutrition-label'>📊 {nut}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"أضف {name}", key=name, use_container_width=True):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.toast(f"✅ تمت إضافة {name}")

    with col_cart:
        st.markdown("<div class='cart-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='cart-header'>🛒 طلباتك</h2>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.info("سلتك فارغة، بلش عبيها!")
        else:
            for i, item in enumerate(st.session_state.cart):
                col_i, col_p = st.columns([3, 1])
                col_i.write(f"{item['n']}")
                col_p.write(f"{item['p']:.2f}")
            
            st.divider()
            st.markdown(f"<h3 style='text-align:center;'>المجموع: {st.session_state.total:.2f} JOD</h3>", unsafe_allow_html=True)
            
            # قسم معلومات العميل (احترافي)
            st.markdown("---")
            st.markdown("#### 👤 تفاصيل المستلم")
            c_name = st.text_input("الاسم الكامل")
            c_phone = st.text_input("رقم الهاتف")
            c_loc = st.selectbox("المنطقة", ["عمان", "إربد", "الزرقاء", "العقبة", "أخرى"])
            
            if st.button("🚀 تأكيد الطلب الملكي", use_container_width=True):
                if c_name and c_phone:
                    st.success(f"تم إرسال الطلب للمطبخ! شكرًا {c_name}")
                    st.balloons()
                else:
                    st.warning("عبي بياناتك يا طيب")

            # زر تفريغ السلة بتصميم جديد
            if st.button("🗑️ مسح السلة", use_container_width=True, help="حذف كل العناصر"):
                st.session_state.cart = []; st.session_state.total = 0.0; st.rerun()

        if st.button("⬅️ البوابة", use_container_width=True):
            st.session_state.page = 'welcome'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<center style='margin-top:50px; opacity:0.3;'>Shawarma Al-Saj v3.0 | 2026</center>", unsafe_allow_html=True)
