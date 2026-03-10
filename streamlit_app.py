import streamlit as st
import requests
import time

# --- إعدادات الربط النهائية ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"
MY_PHONE = "0799633096"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مطعم الضيعة | البوابة الملكية", page_icon="🌙", layout="wide")

# إدارة الصفحات (البوابة هي الأصل)
if 'page' not in st.session_state: st.session_state.page = 'gate'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل (البوابة الـ 7D + الاهتزاز القوي + التوهج) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        direction: RTL !important;
        text-align: right !important;
    }}

    /* الاهتزاز الـ 7D القوي جداً */
    @keyframes strongVibration {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        10% {{ transform: translate(-3px, -2px) rotate(-1deg); }}
        30% {{ transform: translate(0px, 4px) rotate(0.5deg); }}
        50% {{ transform: translate(-2px, 3px) rotate(-1deg); }}
        70% {{ transform: translate(3px, 2px) rotate(1deg); }}
        90% {{ transform: translate(-1px, -1px) rotate(0deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    * {{ font-family: 'Cairo', sans-serif; color: white !important; }}
    
    .stApp {{
        background: radial-gradient(circle at 10% 20%, rgba(255, 215, 0, 0.35), transparent 45%),
                    radial-gradient(circle at 90% 80%, rgba(255, 255, 255, 0.2), transparent 45%),
                    linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
        background-attachment: fixed;
    }}
    
    .main-7d-container {{ animation: strongVibration 0.5s linear infinite; }}

    /* البوابة الزرقاء */
    .gate-overlay {{
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }}

    /* كروت المنيو مع التوهج الأصفر */
    .item-box {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 12px; transition: 0.3s;
    }}
    .item-box:hover {{
        background: rgba(255, 215, 0, 0.3);
        border-color: #FFD700;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
        transform: scale(1.02);
    }}

    /* السلة العائمة (Sticky) */
    [data-testid="stColumn"]:last-child {{
        position: sticky;
        top: 20px;
        z-index: 1001;
    }}

    .cart-section {{
        background: white !important; padding: 25px; border-radius: 20px;
        border: 4px solid #FFD700; color: #003F6B !important;
        box-shadow: 0 15px 40px rgba(0,0,0,0.5);
    }}
    .cart-section * {{ color: #003F6B !important; font-weight: bold; }}

    /* زر الدخول الملكي */
    .stButton>button {{
        border-radius: 50px !important;
        font-weight: 900 !important;
        transition: 0.4s !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- محتوى الصفحات ---

# 1. صفحة البوابة (The Gate)
if st.session_state.page == 'gate':
    st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="gate-overlay">
            <h1 style='font-size: 120px; text-shadow: 10px 10px 30px rgba(0,0,0,0.6); margin-bottom: 0;'>مطعم الضيعة</h1>
            <h2 style='color: #FFD700 !important; font-size: 40px; margin-top: 10px;'>🌙 رمضان كريم - فطورك وعشاك عندنا 🌙</h2>
            <div style='margin: 40px 0; font-size: 25px; background: rgba(0,0,0,0.2); padding: 10px 40px; border-radius: 50px; border: 1px solid #FFD700;'>
                📞 للتواصل المباشر: {MY_PHONE}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("تفضلوا بدخول المنيو والعروض", use_container_width=True):
            st.session_state.page = 'menu'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. صفحة المنيو (بعد ضغط الزر في البوابة)
elif st.session_state.page == 'menu':
    st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)
    
    full_menu = {
        "🌙 عروض رمضان": [
            {"n": "وجبة إفطار الضيعة الملكية", "p": 3.75},
            {"n": "عرض رمضان شاورما (3 وجبات عربي + لتر كولا)", "p": 8.99}
        ],
        "👨‍👩‍👧‍👦 عروض العيلة": [
            {"n": "سدر الضيعة (64 قطعة شاورما + سرفيس كامل)", "p": 14.50},
            {"n": "وليمة البروستد (12 قطعة + كولا عائلي)", "p": 9.99}
        ],
        "🌯 منيو الشاورما والزنجر": [
            {"n": "شاورما سوبر الضيعة", "p": 1.95},
            {"n": "ساندويش زنجر حار", "p": 2.25},
            {"n": "برجر لحم كلاسيك", "p": 2.50}
        ]
    }

    col_items, col_cart = st.columns([2.2, 1])

    with col_items:
        st.markdown(f"<h1 style='text-align:right;'>قائمة طعام الضيعة</h1>", unsafe_allow_html=True)
        if st.button("⬅ العودة للبوابة الرئيسي", use_container_width=False):
            st.session_state.page = 'gate'; st.rerun()

        for category, items in full_menu.items():
            st.markdown(f"## {category}")
            for item in items:
                ci, cb = st.columns([5, 1])
                with ci:
                    st.markdown(f'<div class="item-box"><b>{item["n"]}</b><br><span style="color:#FFD700; font-size:1.2rem;">{item["p"]:.2f} JOD</span></div>', unsafe_allow_html=True)
                with cb:
                    st.write("##")
                    if st.button("+", key=f"add_{item['n']}"):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with col_cart:
        st.markdown('<div class="cart-section">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>🛒 سلة الطلبات</h3>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.write("السلة فارغة")
        else:
            for i in st.session_state.cart:
                st.write(f"• {i['n']} ({i['p']:.2f})")
            st.markdown(f"<hr><h3>المجموع: {st.session_state.total:.2f} JOD</h3>", unsafe_allow_html=True)
            
            pay_m = st.radio("طريقة الحساب:", ["كاش (عند الاستلام)", "فيزا / بطاقة"])
            name = st.text_input("الأسم")
            phone = st.text_input("رقم الهاتف")
            
            if st.button("تأكيد الطلب الآن", use_container_width=True):
                send_telegram_notification(f"طلب جديد: {name}\nرقم: {phone}\nالدفع: {pay_m}\nالقيمة: {st.session_state.total}")
                st.success("تم الإرسال بنجاح!")
                st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
