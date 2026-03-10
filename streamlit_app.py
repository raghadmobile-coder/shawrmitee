import streamlit as st
import requests
import time

# --- إعدادات الربط ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"
MY_WHATSAPP = "962799633096"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# --- إعدادات الصفحة الأصلية ---
st.set_page_config(page_title="الضيعة | مطعم شاورما وبروستد", page_icon="🍖", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'order_status' not in st.session_state: st.session_state.order_status = None

# --- الستايل الأصلي المطور (الأزرق الملكي) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * {{ font-family: 'Cairo', sans-serif; direction: rtl; }}
    .stApp {{ background: #f8f9fa; }}
    
    /* الهيرو سكشن الأصلي */
    .hero-container {{
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        padding: 50px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 149, 246, 0.2);
    }}

    /* أزرار التنقل زي أول */
    .nav-btn-container {{ display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; }}
    
    /* كروت المنيو المطورة */
    .menu-item-card {{
        background: white; border-radius: 16px; padding: 15px; margin-bottom: 20px;
        border: 1px solid #E8ECEF; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: 0.3s;
    }}
    .menu-item-card:hover {{ transform: translateY(-5px); border-color: #0095F6; }}
    
    /* زر الواتساب العائم الخاص بك */
    .whatsapp-float {{
        position: fixed; width: 60px; height: 60px; bottom: 40px; left: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
        font-size: 30px; box-shadow: 2px 5px 15px rgba(0,0,0,0.3); z-index: 100;
        display: flex; align-items: center; justify-content: center; text-decoration: none;
    }}
    
    .status-msg {{
        background: #e3f2fd; color: #0d47a1; padding: 15px; border-radius: 12px;
        border-right: 5px solid #0095F6; margin-bottom: 20px; font-weight: bold;
    }}
    </style>
    
    <a href="https://wa.me/{MY_WHATSAPP}" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
    </a>
""", unsafe_allow_html=True)

# --- نظام الصفحات الأصلي ---
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("🏠 الرئيسية", use_container_width=True): st.session_state.page = 'home'; st.rerun()
with col_n2:
    if st.button("📋 المنيو", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
with col_n3:
    if st.button("📧 تواصل معنا", use_container_width=True): st.session_state.page = 'contact'; st.rerun()

st.divider()

# --- محتوى الصفحات ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class='hero-container'>
            <div style='font-size: 45px; font-weight: 900;'>🍖 مطعم الضيعة 🍖</div>
            <div style='font-size: 20px; opacity: 0.9;'>طعم أصيل | جودة عالية | أسعار منافسة</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.order_status:
        st.markdown(f"<div class='status-msg'>📍 حالة طلبك الحالي: {st.session_state.order_status}</div>", unsafe_allow_html=True)
    
    st.info("نرحب بكم في مطعم الضيعة، اختر من القائمة بالأعلى لتبدأ الطلب!")

elif st.session_state.page == 'menu':
    st.markdown("<h2 style='text-align:center; color:#0077B6;'>📋 قائمة الطعام</h2>", unsafe_allow_html=True)
    
    # تحديث أصناف المنيو (شاورما وبروستد وبرغر)
    items_db = {
        "🌯 قسم الشاورما": [
            {"n": "شاورما سوبر الضيعة", "p": 1.95, "img": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=400"},
            {"n": "وجبة عربي دبل", "p": 3.50, "img": "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=400"},
            {"n": "سدر العيلة (64 قطعة)", "p": 14.50, "img": "https://images.unsplash.com/photo-1609501676725-7186f017a4b5?w=400"}
        ],
        "🍗 قسم البروستد": [
            {"n": "وجبة بروستد 4 قطع", "p": 3.25, "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc45a?w=400"},
            {"n": "وليمة بروستد 12 قطعة", "p": 9.95, "img": "https://images.unsplash.com/photo-1569058242253-92a9c71f9867?w=400"}
        ],
        "🍔 قسم البرغر": [
            {"n": "كلاسيك برغر دجاج", "p": 2.50, "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400"},
            {"n": "برغر لحم سوبر", "p": 3.00, "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"}
        ]
    }

    m_col, c_col = st.columns([2.5, 1])
    
    with m_col:
        for cat, items in items_db.items():
            st.markdown(f"### {cat}")
            cols = st.columns(2)
            for idx, item in enumerate(items):
                with cols[idx % 2]:
                    st.markdown(f"""
                        <div class='menu-item-card'>
                            <img src='{item['img']}' style='width:100%; border-radius:12px; height:150px; object-fit:cover;'>
                            <h4 style='color:#0077B6; margin-top:10px;'>{item['n']}</h4>
                            <p style='font-weight:bold; color:#0095F6;'>السعر: {item['p']:.2f} د.أ</p>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"أضف {item['n']}", key=f"add_{item['n']}"):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with c_col:
        st.markdown("<div style='background:white; padding:20px; border-radius:15px; border:2px solid #0095F6;'>", unsafe_allow_html=True)
        st.subheader("🛒 سلتك")
        if not st.session_state.cart:
            st.write("السلة فارغة")
        else:
            for i, item in enumerate(st.session_state.cart):
                st.write(f"• {item['n']} ({item['p']:.2f} د.أ)")
            st.markdown(f"**💰 المجموع: {st.session_state.total:.2f} د.أ**")
            
            u_name = st.text_input("الأسم")
            u_phone = st.text_input("رقم الموبايل")
            u_loc = st.text_input("موقع التوصيل (رابط)")
            
            if st.button("🚀 إرسال الطلب الآن", use_container_width=True):
                if u_name and u_phone:
                    order_text = "\n".join([f"- {x['n']}" for x in st.session_state.cart])
                    full_msg = f"🔔 طلب جديد!\nالاسم: {u_name}\nالهاتف: {u_phone}\nالطلبات:\n{order_text}\nالمجموع: {st.session_state.total:.2f}"
                    send_telegram_notification(full_msg)
                    st.session_state.order_status = "جاري تحضير طلبك الساخن.. 🔥"
                    st.success("تم الإرسال!")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    time.sleep(2); st.session_state.page = 'home'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    st.markdown("<h2 style='text-align:center;'>📧 تواصل معنا</h2>", unsafe_allow_html=True)
    st.info(f"يمكنك التواصل معنا مباشرة عبر الهاتف: 0799633096 أو عبر الواتساب بالضغط على الزر الأخضر بالأسفل.")
