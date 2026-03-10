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
st.set_page_config(page_title="مطعم الضيعة | Al-Deera Luxury", page_icon="🍖", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل المطور (تركيز على التفاصيل، اهتزاز قوي، وبدون إيموجي) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* تقوية الحركة الاهتزازية (Vibration 7D) */
    @keyframes strongVibration {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        10% {{ transform: translate(-2px, -1px) rotate(-0.5deg); }}
        20% {{ transform: translate(-3px, 0px) rotate(0.5deg); }}
        30% {{ transform: translate(0px, 2px) rotate(0deg); }}
        40% {{ transform: translate(1px, -1px) rotate(0.5deg); }}
        50% {{ transform: translate(-1px, 2px) rotate(-0.5deg); }}
        60% {{ transform: translate(-3px, 1px) rotate(0deg); }}
        70% {{ transform: translate(2px, 1px) rotate(-0.5deg); }}
        80% {{ transform: translate(-1px, -1px) rotate(0.5deg); }}
        90% {{ transform: translate(2px, 2px) rotate(0deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    /* اتجاه الكتابة من اليمين للشمال */
    html, body, [data-testid="stAppViewContainer"] {{
        direction: RTL;
        text-align: right;
    }}

    * {{ font-family: 'Cairo', sans-serif; color: white !important; }}
    
    .stApp {{
        background: radial-gradient(circle at 10% 20%, rgba(255, 215, 0, 0.2), transparent 40%),
                    radial-gradient(circle at 90% 80%, rgba(255, 255, 255, 0.15), transparent 40%),
                    linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
        background-size: 400% 400%;
        animation: backgroundShift 12s ease infinite;
    }}
    
    /* تطبيق الاهتزاز القوي على الحاوية الرئيسية */
    .main-7d-container {{
        animation: strongVibration 0.5s linear infinite;
        animation-play-state: running;
    }}
    /* تهدئة الاهتزاز عند القراءة المركزة (اختياري: يمكن حذفه ليبقى يهتز دوماً) */
    .main-7d-container:hover {{ animation-duration: 2s; }}

    .item-box {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 25px; border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px; transition: 0.4s;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }}

    /* تصغير زر الزائد (+) وجعله أنيقاً */
    .stButton>button {{
        border-radius: 8px !important;
        padding: 2px 10px !important;
        font-size: 14px !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid white !important;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #FFD700 !important;
        color: #005F9E !important;
    }}
    
    .price-tag {{ color: #FFD700 !important; font-weight: 900; font-size: 1.5rem; }}

    .cart-section {{
        background: white !important; padding: 25px; border-radius: 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5); border: 3px solid #FFD700;
        direction: RTL;
    }}
    .cart-section * {{ color: #003F6B !important; }}
    </style>
""", unsafe_allow_html=True)

# --- بدء الحاوية الـ 7D ---
st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)

# --- الهيدر ---
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("الصفحة الرئيسية", use_container_width=True): st.session_state.page = 'home'; st.rerun()
with col_n2:
    if st.button("قائمة الطعام", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
with col_n3:
    if st.button("اتصل بنا", use_container_width=True): st.session_state.page = 'contact'; st.rerun()

st.divider()

# --- المنيو (بدون إيموجي وبترتيب دقيق) ---
menu_data = {
    "قسم الشاورما": [
        {"n": "ساندويش شاورما عادي", "p": 0.95},
        {"n": "شاورما سوبر الضيعة", "p": 1.95},
        {"n": "وجبة عربي صغير", "p": 2.25},
        {"n": "وجبة عربي دبل", "p": 3.50},
        {"n": "سدر الضيعة 64 قطعة", "p": 14.50}
    ],
    "قسم البروستد": [
        {"n": "وجبة بروستد 4 قطع", "p": 3.25},
        {"n": "وجبة بروستد 8 قطع", "p": 6.25},
        {"n": "وليمة بروستد 12 قطعة", "p": 9.95}
    ],
    "قسم البرغر": [
        {"n": "كلاسيك برغر دجاج", "p": 2.50},
        {"n": "برغر لحم سوبر", "p": 3.00},
        {"n": "زنجر برغر حار", "p": 2.75}
    ]
}

if st.session_state.page == 'home':
    st.markdown("""
        <div style='text-align: center; padding: 100px 20px;'>
            <h1 style='font-size: 90px; font-weight: 900; letter-spacing: -2px;'>مطعم الضيعة</h1>
            <p style='font-size: 30px; color: #FFD700 !important;'>الجودة العالية والسعر المنافس</p>
            <div style='margin-top: 50px; border-bottom: 2px solid #FFD700; display: inline-block; padding: 10px 50px;'>
                هاتف: 0799633096
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'menu':
    m_col, c_col = st.columns([2.5, 1])
    with m_col:
        for cat, items in menu_data.items():
            st.markdown(f"## {cat}")
            for item in items:
                col_i, col_b = st.columns([5, 1])
                with col_i:
                    st.markdown(f'<div class="item-box"><div style="font-size: 1.6rem; font-weight: bold;">{item["n"]}</div><div class="price-tag">{item["p"]:.2f} JOD</div></div>', unsafe_allow_html=True)
                with col_b:
                    st.write(" ") # موازنة
                    if st.button("+", key=f"btn_{item['n']}", use_container_width=False):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with c_col:
        st.markdown("<div class='cart-section'>", unsafe_allow_html=True)
        st.markdown("<h3>قائمة الطلبات</h3>", unsafe_allow_html=True)
        if not st.session_state.cart:
            st.write("السلة فارغة حالياً")
        else:
            for i in st.session_state.cart: st.write(f"- {i['n']}")
            st.markdown(f"<strong>المجموع الكلي: {st.session_state.total:.2f} JOD</strong>", unsafe_allow_html=True)
            u_name = st.text_input("الاسم الشخصي")
            u_phone = st.text_input("رقم التواصل")
            if st.button("تأكيد وإرسال الطلب", use_container_width=True):
                send_telegram_notification(f"طلب جديد من {u_name}\nرقم: {u_phone}\nالقيمة: {st.session_state.total}")
                st.success("تم إرسال طلبك بنجاح")
                st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    st.markdown("""
        <div style='text-align: center; padding: 50px;'>
            <h1>تواصل مباشرة مع الإدارة</h1>
            <div style='font-size: 50px; color: #FFD700 !important; margin: 30px 0;'>0799633096</div>
            <p>الموقع: عمان - الأردن</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # إغلاق حاوية الاهتزاز
