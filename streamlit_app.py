import streamlit as st
import requests
import time

# --- إعدادات الربط ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"
MY_PHONE = "0799633096"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مطعم الضيعة | القائمة الرسمية", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'gate'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل النهائي (بدون إيموجي + اهتزاز قوي + سلة عائمة) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        direction: RTL !important;
        text-align: right !important;
    }}

    @keyframes strongVibration {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        10% {{ transform: translate(-3px, -2px) rotate(-1deg); }}
        30% {{ transform: translate(0px, 4px) rotate(0.5deg); }}
        50% {{ transform: translate(-2px, 3px) rotate(-1deg); }}
        70% {{ transform: translate(3px, 2px) rotate(1deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    * {{ font-family: 'Cairo', sans-serif; color: white !important; }}
    
    .stApp {{
        background: radial-gradient(circle at 10% 20%, rgba(255, 215, 0, 0.35), transparent 45%),
                    linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
        background-attachment: fixed;
    }}
    
    .main-7d-container {{ animation: strongVibration 0.5s linear infinite; }}

    .item-box {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 20px; border-radius: 12px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 10px; transition: 0.3s;
    }}
    .item-box:hover {{
        background: rgba(255, 215, 0, 0.25);
        border-color: #FFD700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
    }}

    [data-testid="stColumn"]:last-child {{
        position: sticky;
        top: 20px;
        z-index: 1001;
    }}

    .cart-section {{
        background: white !important; padding: 25px; border-radius: 15px;
        border: 4px solid #FFD700; color: #003F6B !important;
        box-shadow: 0 15px 40px rgba(0,0,0,0.5);
    }}
    .cart-section * {{ color: #003F6B !important; font-weight: bold; }}

    .stButton>button {{
        border-radius: 8px !important;
        font-weight: bold !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- محتوى المنيو الضخم ---
full_menu = {
    "عروض رمضان": [
        {"n": "وجبة إفطار الضيعة الملكية", "p": 3.75},
        {"n": "عرض رمضان شاورما (3 وجبات عربي + لتر كولا)", "p": 8.99},
        {"n": "عرض العيلة الرمضاني بروستد مع شاورما", "p": 16.50}
    ],
    "العروض العائلية": [
        {"n": "سدر الضيعة شاورما 64 قطعة مع سرفيس", "p": 14.50},
        {"n": "بوكس التوفير العائلي شاورما وبرجر", "p": 11.00}
    ],
    "قسم الشاورما": [
        {"n": "ساندويش شاورما عادي", "p": 0.95},
        {"n": "ساندويش شاورما سوبر", "p": 1.95},
        {"n": "وجبة شاورما عادي", "p": 2.25},
        {"n": "وجبة شاورما دبل", "p": 3.50},
        {"n": "وجبة شاورما تربل", "p": 4.75}
    ],
    "الزنجر والبرجر": [
        {"n": "ساندويش زنجر", "p": 2.25},
        {"n": "وجبة زنجر", "p": 3.50},
        {"n": "برغر لحم كلاسيك", "p": 2.50},
        {"n": "برغر دجاج سوبر", "p": 2.25}
    ],
    "قسم البروستد": [
        {"n": "وجبة بروستد 4 قطع", "p": 3.25},
        {"n": "وجبة بروستد 6 قطع", "p": 4.75},
        {"n": "وجبة بروستد 12 قطعة", "p": 9.50},
        {"n": "وجبة بروستد 16 قطعة", "p": 12.50},
        {"n": "وجبة بروستد 21 قطعة عائلية", "p": 16.00}
    ],
    "وجبات الأطفال والإضافات": [
        {"n": "وجبة أطفال (برجر صغير + بطاطا + عصير)", "p": 1.95},
        {"n": "صحن بطاطا كبير", "p": 1.25},
        {"n": "مثومة إضافية", "p": 0.25},
        {"n": "شطة إضافية", "p": 0.25}
    ]
}

# --- 1. صفحة البوابة ---
if st.session_state.page == 'gate':
    st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <h1 style='font-size: 110px; margin-bottom: 0;'>مطعم الضيعة</h1>
            <h2 style='color: #FFD700 !important; font-size: 35px;'>رمضان كريم - أهلاً بكم</h2>
            <div style='margin: 30px 0; font-size: 22px; border: 1px solid #FFD700; padding: 10px 40px; border-radius: 50px;'>
                للتواصل: {MY_PHONE}
            </div>
    """, unsafe_allow_html=True)
    if st.button("الدخول إلى القائمة الكاملة", use_container_width=False):
        st.session_state.page = 'menu'
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- 2. صفحة المنيو ---
elif st.session_state.page == 'menu':
    st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)
    
    col_list, col_cart = st.columns([2.2, 1])

    with col_list:
        st.markdown(f"<h2>قائمة الطعام الرسمية - للتواصل: {MY_PHONE}</h2>", unsafe_allow_html=True)
        if st.button("العودة للرئيسية"):
            st.session_state.page = 'gate'; st.rerun()

        for cat, items in full_menu.items():
            st.markdown(f"### {cat}")
            for item in items:
                ci, cb = st.columns([5, 1])
                with ci:
                    st.markdown(f'<div class="item-box"><b>{item["n"]}</b><br><span style="color:#FFD700;">{item["p"]:.2f} JOD</span></div>', unsafe_allow_html=True)
                with cb:
                    st.write("##")
                    if st.button("+", key=f"add_{item['n']}"):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with col_cart:
        st.markdown('<div class="cart-section">', unsafe_allow_html=True)
        st.markdown("<h3>سلة الطلبات</h3>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.write("قم باختيار الوجبات")
        else:
            for i in st.session_state.cart:
                st.write(f"- {i['n']}")
            st.markdown(f"<hr><h4>المجموع: {st.session_state.total:.2f} JOD</h4>", unsafe_allow_html=True)
            
            pay_m = st.radio("طريقة الحساب", ["كاش عند الاستلام", "فيزا"])
            u_name = st.text_input("الاسم الشخصي")
            u_phone = st.text_input("رقم الهاتف")
            
            if st.button("تأكيد وإرسال الطلب", use_container_width=True):
                if u_name and u_phone:
                    msg = f"طلب جديد!\nالاسم: {u_name}\nالهاتف: {u_phone}\nالدفع: {pay_m}\nالمجموع: {st.session_state.total:.2f}"
                    send_telegram_notification(msg)
                    st.success("تم استلام طلبك بنجاح")
                    st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
