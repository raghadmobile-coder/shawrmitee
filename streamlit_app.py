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
st.set_page_config(page_title="مطعم الضيعة | عروض رمضان والعيلة", page_icon="🌙", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'gate'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل (البوابة + التوهج الأصفر + السلة العائمة) ---
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
        30% {{ transform: translate(0px, 3px) rotate(0deg); }}
        50% {{ transform: translate(-2px, 3px) rotate(-1deg); }}
        70% {{ transform: translate(3px, 2px) rotate(-1deg); }}
        100% {{ transform: translate(0, 0) rotate(0deg); }}
    }}

    * {{ font-family: 'Cairo', sans-serif; color: white !important; }}
    
    .stApp {{
        background: radial-gradient(circle at 15% 25%, rgba(255, 215, 0, 0.3), transparent 50%),
                    linear-gradient(135deg, #005F9E 0%, #0095F6 50%, #003F6B 100%);
        background-attachment: fixed;
    }}
    
    .main-7d-container {{ animation: strongVibration 0.5s linear infinite; }}

    .item-box {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 20px; border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }}
    .item-box:hover {{
        background: rgba(255, 215, 0, 0.3);
        border-color: #FFD700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
        transform: scale(1.03);
    }}

    /* السلة العائمة الملاحقة */
    [data-testid="stColumn"]:last-child {{
        position: sticky;
        top: 20px;
        z-index: 1000;
    }}

    .cart-section {{
        background: white !important; 
        padding: 25px; border-radius: 20px;
        border: 4px solid #FFD700;
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    }}
    .cart-section * {{ color: #003F6B !important; font-weight: bold; }}

    .stButton>button {{
        border-radius: 10px !important;
        transition: 0.3s;
    }}
    </style>
""", unsafe_allow_html=True)

# --- محتوى الصفحات ---

if st.session_state.page == 'gate':
    st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='text-align: center;'>
            <h1 style='font-size: 110px; text-shadow: 5px 5px 20px rgba(0,0,0,0.5);'>مطعم الضيعة</h1>
            <h2 style='color: #FFD700 !important; margin-bottom: 40px;'>🌙 رمضان كريم - عروضنا ما بتخلص 🌙</h2>
            <p style='font-size: 20px;'>للتواصل المباشر: {MY_PHONE}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        if st.button("تفضلوا على المنيو الأصيل", use_container_width=True):
            st.session_state.page = 'menu'
            st.rerun()

elif st.session_state.page == 'menu':
    st.markdown('<div class="main-7d-container">', unsafe_allow_html=True)
    
    # --- داتا المنيو الموسعة ---
    full_menu = {
        "🌙 عروض رمضان (فطورك عندنا)": [
            {"n": "وجبة إفطار الضيعة (ربع دجاجة + أرز + شوربة + تمر)", "p": 3.75},
            {"n": "عرض رمضان شاورما (3 وجبات عربي + لتر كولا)", "p": 8.99},
            {"n": "بوكس السعادة (بروستد + زنجر + بطاطا + مقبلات)", "p": 12.50}
        ],
        "👨‍👩‍👧‍👦 العروض العائلية (الجمعات الكبيرة)": [
            {"n": "سدر الضيعة الملكي (64 قطعة شاورما + سرفيس كامل)", "p": 14.50},
            {"n": "وليمة البروستد (12 قطعة + بطاطا + ثومية + كولا عائلي)", "p": 9.99},
            {"n": "بوكس التوفير (4 ساندويش سوبر + بطاطا عائلي)", "p": 7.50}
        ],
        "🌯 ركن الشاورما": [
            {"n": "ساندويش شاورما عادي", "p": 0.95},
            {"n": "شاورما سوبر الضيعة", "p": 1.95},
            {"n": "وجبة عربي صغير", "p": 2.25},
            {"n": "وجبة عربي دبل", "p": 3.50}
        ],
        "🍗 بروستد مقرمش": [
            {"n": "وجبة بروستد 4 قطع", "p": 3.25},
            {"n": "وجبة بروستد 8 قطع", "p": 6.25},
            {"n": "وجبة زنجر حار", "p": 2.25}
        ],
        "🍔 البرجر والفاهيتا": [
            {"n": "كلاسيك برجر لحم", "p": 2.50},
            {"n": "سوبر برجر دجاج", "p": 2.25},
            {"n": "ساندويش فاهيتا إيطالي", "p": 2.50}
        ]
    }

    col_items, col_cart = st.columns([2.2, 1])

    with col_items:
        st.markdown(f"<h1 style='text-align:right;'>منيو الضيعة 🍖</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#FFD700;'>خدمة التوصيل: {MY_PHONE}</p>", unsafe_allow_html=True)
        
        for category, items in full_menu.items():
            st.markdown(f"## {category}")
            for item in items:
                ci, cb = st.columns([5, 1])
                with ci:
                    st.markdown(f"""
                        <div class="item-box">
                            <div style="font-size: 1.3rem; font-weight: bold;">{item['n']}</div>
                            <div style="color: #FFD700 !important; font-size: 1.1rem;">{item['p']:.2f} JOD</div>
                        </div>
                    """, unsafe_allow_html=True)
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
            st.write("سلتك فارغة، بلش اختار عروضك!")
        else:
            for i in st.session_state.cart:
                st.write(f"• {i['n']} ({i['p']:.2f})")
            
            st.markdown(f"<hr><h3>المجموع: {st.session_state.total:.2f} JOD</h3>", unsafe_allow_html=True)
            
            pay_m = st.radio("طريقة الدفع المحببة:", ["كاش (عند الباب)", "فيزا / بطاقة"])
            
            name = st.text_input("الأسم الكريم")
            phone = st.text_input("رقم الهاتف")
            
            if st.button("تأكيد وطلب الآن", use_container_width=True):
                if name and phone:
                    order_list = "\n".join([f"- {x['n']}" for x in st.session_state.cart])
                    msg = f"🔔 طلب جديد من الضيعة!\n\nالاسم: {name}\nالهاتف: {phone}\nالدفع: {pay_m}\n\nالأصناف:\n{order_list}\n\nالمجموع الكلي: {st.session_state.total:.2f}"
                    send_telegram_notification(msg)
                    st.success("صحتين وعافية! طلبك صار عندنا.")
                    st.session_state.cart = []; st.session_state.total = 0.0; time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
