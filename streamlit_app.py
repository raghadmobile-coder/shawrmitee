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

# --- الستايل المطور (تأثير الإضاءة الصفراء + السلة العائمة) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        direction: RTL !important;
        text-align: right !important;
    }}

    @keyframes strongVibration {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        10% {{ transform: translate(-2px, -1px) rotate(-0.5deg); }}
        30% {{ transform: translate(0px, 2px) rotate(0deg); }}
        50% {{ transform: translate(-1px, 2px) rotate(-0.5deg); }}
        70% {{ transform: translate(2px, 1px) rotate(-0.5deg); }}
        90% {{ transform: translate(2px, 2px) rotate(0deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    * {{ font-family: 'Cairo', sans-serif; color: white !important; }}
    
    .stApp {{
        background: radial-gradient(circle at 15% 25%, rgba(255, 215, 0, 0.25), transparent 45%),
                    radial-gradient(circle at 85% 75%, rgba(255, 255, 255, 0.15), transparent 45%),
                    linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
        background-size: 400% 400%;
    }}
    
    .main-7d-container {{
        animation: strongVibration 0.6s linear infinite;
    }}

    /* تأثير الإضاءة الصفراء عند وضع المؤشر */
    .item-box {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 20px; border-radius: 12px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 15px;
        text-align: right;
        transition: all 0.4s ease;
        cursor: pointer;
    }}

    .item-box:hover {{
        background: rgba(255, 215, 0, 0.2); /* خلفية صفراء خفيفة */
        border-color: #FFD700; /* حدود صفراء تلمع */
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6); /* توهج أصفر */
        transform: translateY(-5px);
    }}

    /* السلة العائمة */
    [data-testid="stVerticalBlock"] > div:last-child .cart-section-container {{
        position: sticky;
        top: 20px;
        z-index: 99;
    }}

    .cart-section {{
        background: white !important; 
        padding: 20px; 
        border-radius: 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5); 
        border: 3px solid #FFD700;
        direction: RTL;
        color: #003F6B !important;
    }}
    
    .cart-section * {{ color: #003F6B !important; text-align: right; }}

    /* أزرار التنقل مع تأثير التوهج */
    .stButton>button {{
        transition: all 0.3s ease !important;
    }}
    .stButton>button:hover {{
        border-color: #FFD700 !important;
        box-shadow: 0 0 15px #FFD700 !important;
        color: #FFD700 !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)

col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("الصفحة الرئيسية", use_container_width=True): st.session_state.page = 'home'; st.rerun()
with col_n2:
    if st.button("قائمة الطعام", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
with col_n3:
    if st.button("اتصل بنا", use_container_width=True): st.session_state.page = 'contact'; st.rerun()

st.divider()

menu_data = {
    "قسم الشاورما": [
        {"n": "ساندويش شاورما عادي", "p": 0.95},
        {"n": "شاورما سوبر الضيعة", "p": 1.95},
        {"n": "وجبة عربي صغير", "p": 2.25},
        {"n": "وجبة عربي دبل", "p": 3.50}
    ],
    "قسم البروستد": [
        {"n": "وجبة بروستد 4 قطع", "p": 3.25},
        {"n": "وليمة بروستد 12 قطعة", "p": 9.95}
    ]
}

if st.session_state.page == 'home':
    st.markdown("<div style='text-align: center; padding: 80px 0;'><h1 style='font-size: 80px;'>مطعم الضيعة</h1><p style='font-size: 25px; color:#FFD700 !important;'>أهلاً بكم في عالم المذاق الأصيل</p></div>", unsafe_allow_html=True)

elif st.session_state.page == 'menu':
    col_menu, col_cart = st.columns([2.5, 1])
    
    with col_menu:
        for cat, items in menu_data.items():
            st.markdown(f"## {cat}")
            for item in items:
                c_text, c_btn = st.columns([5, 1])
                with c_text:
                    st.markdown(f"""
                        <div class="item-box">
                            <div style="font-size: 1.4rem; font-weight: bold;">{item['n']}</div>
                            <div style="color: #FFD700 !important; font-weight: 900;">{item['p']:.2f} JOD</div>
                        </div>
                    """, unsafe_allow_html=True)
                with c_btn:
                    st.write("##")
                    if st.button("+", key=f"add_{item['n']}"):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with col_cart:
        st.markdown('<div class="cart-section-container">', unsafe_allow_html=True)
        st.markdown('<div class="cart-section">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-bottom:20px;'>🛒 سلة طلباتك</h3>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.write("أضف أصنافك المفضلة")
        else:
            for i in st.session_state.cart:
                st.write(f"• {i['n']} - {i['p']:.2f}")
            st.markdown(f"<hr><h4 style='color:#003F6B;'>المجموع: {st.session_state.total:.2f} JOD</h4>", unsafe_allow_html=True)
            
            u_name = st.text_input("اسمك الكريم")
            u_phone = st.text_input("رقم موبايلك")
            
            if st.button("إتمام الطلب الآن", use_container_width=True):
                if u_name and u_phone:
                    st.success("تم إرسال الطلب!")
                    send_telegram_notification(f"طلب جديد: {u_name}\nالهاتف: {u_phone}\nالمجموع: {st.session_state.total}")
                    st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
