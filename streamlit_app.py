import streamlit as st
import requests
import time

# --- إعدادات الربط ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مطعم الضيعة | القائمة الكاملة", page_icon="🍔", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'menu'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل (اليمين لليسار + السلة المثابتة + التوهج الأصفر) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: RTL !important;
        text-align: right !important;
    }

    /* الاهتزاز القوي 7D */
    @keyframes strongVibration {
        0% { transform: translate(0, 0) rotate(0deg); }
        10% { transform: translate(-2px, -1px) rotate(-0.5deg); }
        30% { transform: translate(0px, 2px) rotate(0deg); }
        50% { transform: translate(-1px, 2px) rotate(-0.5deg); }
        70% { transform: translate(2px, 1px) rotate(-0.5deg); }
        100% { transform: translate(0, 0) rotate(0deg); }
    }

    * { font-family: 'Cairo', sans-serif; color: white !important; }
    
    .stApp {
        background: linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
    }
    
    .main-7d-container { animation: strongVibration 0.6s linear infinite; }

    /* كرت الصنف مع التوهج الأصفر عند اللمس */
    .item-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 15px; border-radius: 12px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .item-box:hover {
        background: rgba(255, 215, 0, 0.2);
        border-color: #FFD700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
        transform: scale(1.02);
    }

    /* تثبيت السلة والمجموع (Sticky) */
    [data-testid="stColumn"]:last-child {
        position: sticky;
        top: 20px;
        height: fit-content;
    }

    .cart-section {
        background: white !important; 
        padding: 20px; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3); 
        border: 3px solid #FFD700;
        color: #003F6B !important;
    }
    .cart-section * { color: #003F6B !important; }

    /* تصغير زر الزائد */
    .stButton>button {
        min-width: 40px !important; height: 40px !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)

# --- القائمة الكاملة للأصناف ---
menu_data = {
    "قسم الشاورما": [
        {"n": "ساندويش شاورما عادي", "p": 0.95},
        {"n": "شاورما سوبر الضيعة", "p": 1.95},
        {"n": "وجبة عربي صغير", "p": 2.25},
        {"n": "وجبة عربي دبل", "p": 3.50},
        {"n": "سدر الضيعة (64 قطعة)", "p": 14.50}
    ],
    "الزنجر والبرجر": [
        {"n": "ساندويش زنجر حار", "p": 2.25},
        {"n": "وجبة زنجر عائلي", "p": 5.50},
        {"n": "برجر لحم كلاسيك", "p": 2.50},
        {"n": "برجر دجاج سوبر", "p": 2.25},
        {"n": "ساندويش فاهيتا", "p": 2.50}
    ],
    "البروستد والمقبلات": [
        {"n": "وجبة بروستد 4 قطع", "p": 3.25},
        {"n": "وجبة بروستد 8 قطع", "p": 6.25},
        {"n": "صحن بطاطا كبير", "p": 1.00},
        {"n": "مثومة / شطة إضافية", "p": 0.25}
    ]
}

col_menu, col_cart = st.columns([2.2, 1])

with col_menu:
    st.markdown("<h1 style='text-align:right;'>قائمة طعام الضيعة</h1>", unsafe_allow_html=True)
    for cat, items in menu_data.items():
        st.markdown(f"### {cat}")
        for item in items:
            c_info, c_btn = st.columns([5, 1])
            with c_info:
                st.markdown(f"""
                    <div class="item-box">
                        <div style="font-size: 1.2rem; font-weight: bold;">{item['n']}</div>
                        <div style="color: #FFD700 !important;">{item['p']:.2f} JOD</div>
                    </div>
                """, unsafe_allow_html=True)
            with c_btn:
                st.write(" ")
                if st.button("+", key=f"add_{item['n']}"):
                    st.session_state.cart.append(item)
                    st.session_state.total += item['p']
                    st.rerun()

with col_cart:
    st.markdown('<div class="cart-section">', unsafe_allow_html=True)
    st.markdown("<h3>🛒 سلة الطلبات</h3>", unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.write("السلة فارغة")
    else:
        for i in st.session_state.cart:
            st.write(f"• {i['n']} ({i['p']:.2f})")
        
        st.markdown(f"<hr><h4>المجموع: {st.session_state.total:.2f} JOD</h4>", unsafe_allow_html=True)
        
        name = st.text_input("الاسم")
        phone = st.text_input("الرقم")
        
        if st.button("تأكيد الطلب", use_container_width=True):
            if name and phone:
                send_telegram_notification(f"طلب جديد: {name}\nرقم: {phone}\nالمجموع: {st.session_state.total}")
                st.success("تم الإرسال!")
                st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
