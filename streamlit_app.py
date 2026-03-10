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

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مطعم الضيعة | Al-Deera 7D", page_icon="🍖", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل المطور (الخلفية الـ 7D والحركة الاهتزازية) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* الحركة الاهتزازية اللطيفة (Floating & Vibration) */
    @keyframes subtleVibration {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        25% {{ transform: translate(1px, 1px) rotate(0.1deg); }}
        50% {{ transform: translate(-1px, 0px) rotate(-0.1deg); }}
        75% {{ transform: translate(1px, -1px) rotate(0deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    /* حركة تدرج الألوان الخلفية */
    @keyframes backgroundShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    * {{ font-family: 'Cairo', sans-serif; direction: rtl; color: white !important; }}
    
    .stApp {{
        /* خلفية زرقاء مع تهميش أصفر وأبيض (Radial Gradients لتعطي عمق 7D) */
        background: radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.15), transparent 40%),
                    radial-gradient(circle at 80% 70%, rgba(255, 255, 255, 0.1), transparent 40%),
                    linear-gradient(135deg, #0077B6 0%, #0095F6 50%, #005F9E 100%);
        background-size: 200% 200%;
        animation: backgroundShift 10s ease infinite;
        min-height: 100vh;
    }}
    
    /* تطبيق الاهتزاز على الحاوية الرئيسية */
    .main-container {{
        animation: subtleVibration 4s ease-in-out infinite;
    }}

    /* كرت الوجبة المحسن (Glassmorphism) */
    .item-box {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px; border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 15px; transition: 0.3s;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }}
    .item-box:hover {{ 
        background: rgba(255, 255, 255, 0.2); 
        transform: scale(1.02);
        border-color: #FFD700;
    }}
    
    .price-tag {{ color: #FFD700 !important; font-weight: 900; font-size: 1.4rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
    
    /* زر الواتساب */
    .whatsapp-float {{
        position: fixed; width: 65px; height: 65px; bottom: 40px; left: 40px;
        background-color: #25d366; border-radius: 50px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3); z-index: 100;
        display: flex; align-items: center; justify-content: center;
        animation: subtleVibration 3s infinite;
    }}

    .cart-section {{
        background: rgba(255, 255, 255, 0.95) !important; padding: 25px; border-radius: 25px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4); border: 2px solid #FFD700;
    }}
    .cart-section * {{ color: #005F9E !important; }}
    </style>
""", unsafe_allow_html=True)

# --- محتوى الموقع داخل حاوية مهتزة ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- الهيدر (Navigation) ---
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("🏠 الرئيسية", use_container_width=True): st.session_state.page = 'home'; st.rerun()
with col_n2:
    if st.button("📋 المنيو", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
with col_n3:
    if st.button("📧 تواصل معنا", use_container_width=True): st.session_state.page = 'contact'; st.rerun()

st.divider()

# --- البيانات المنظمة ---
menu_data = {
    "🌯 قسم الشاورما": [
        {"n": "ساندويش شاورما عادي", "p": 0.95},
        {"n": "شاورما سوبر الضيعة", "p": 1.95},
        {"n": "وجبة عربي صغير", "p": 2.25},
        {"n": "وجبة عربي دبل", "p": 3.50},
        {"n": "سدر الضيعة (64 قطعة)", "p": 14.50}
    ],
    "🍗 قسم البروستد": [
        {"n": "وجبة بروستد 4 قطع", "p": 3.25},
        {"n": "وجبة بروستد 8 قطع", "p": 6.25},
        {"n": "وليمة بروستد 12 قطعة", "p": 9.95}
    ],
    "🍔 قسم البرغر": [
        {"n": "كلاسيك برغر دجاج", "p": 2.50},
        {"n": "برغر لحم سوبر", "p": 3.00},
        {"n": "زنجر برغر حار", "p": 2.75}
    ]
}

if st.session_state.page == 'home':
    st.markdown(f"""
        <div style='text-align: center; padding: 80px 20px;'>
            <h1 style='font-size: 80px; font-weight: 900; text-shadow: 5px 5px 15px rgba(0,0,0,0.4);'>مطعم الضيعة</h1>
            <p style='font-size: 28px; color: #FFD700 !important; font-weight: 700;'>طعمٌ يتنفس.. وعمقٌ يتكلم</p>
            <div style='margin-top: 40px; background: rgba(255,255,255,0.1); display: inline-block; padding: 15px 45px; border-radius: 50px; border: 1px solid #FFD700;'>
                📞 0799633096
            </div>
        </div>
        <a href="https://wa.me/{MY_WHATSAPP}" class="whatsapp-float" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
        </a>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'menu':
    m_col, c_col = st.columns([2.5, 1])
    with m_col:
        for cat, items in menu_data.items():
            st.markdown(f"### ✨ {cat}")
            for item in items:
                col_i, col_b = st.columns([4, 1])
                with col_i:
                    st.markdown(f'<div class="item-box"><span style="font-size: 1.4rem; font-weight: bold;">{item["n"]}</span><br><span class="price-tag">{item["p"]:.2f} JOD</span></div>', unsafe_allow_html=True)
                with col_b:
                    st.write(" ")
                    if st.button("➕", key=f"add_{item['n']}", use_container_width=True):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()
    with c_col:
        st.markdown("<div class='cart-section'>", unsafe_allow_html=True)
        st.subheader("🛒 سلة المشتريات")
        for i in st.session_state.cart: st.write(f"• {i['n']}")
        st.markdown(f"**المجموع: {st.session_state.total:.2f} JOD**")
        n = st.text_input("الأسم")
        p = st.text_input("الهاتف")
        if st.button("تأكيد الطلب"):
            st.success("جاري الإرسال...")
            send_telegram_notification(f"طلب من {n}\n{p}\nالمجموع: {st.session_state.total}")
            st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
