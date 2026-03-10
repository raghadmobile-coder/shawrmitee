import streamlit as st
import requests

# --- الإعدادات الصحيحة (مأخوذة من صورك) ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # التعديل هون: شلنا الأخطاء اللي بالصورة
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": order_details,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

# --- باقي الكود مع البرغرات والأقسام (التصميم الأصلي) ---
st.set_page_config(page_title="Shawarma Al-Saj", page_icon="🌯", layout="wide")

if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# تصميم البلوكات الضخمة (كما في الصورة 37038ee7)
st.markdown("""
    <style>
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 22px !important; font-weight: 900 !important;
        border: 2px solid #ff4b4b !important; margin-bottom: 15px; color: white !important;
    }
    .menu-item-card { background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; padding: 30px; border-radius: 20px; margin-bottom: 20px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

with col_side:
    st.markdown("### الأقسام")
    category = st.radio("", ["🔥 العروض الملكية", "🌯 شاورما (أحجام)", "🍔 برغرات الساحل", "🍗 بروستد مقرمش", "🍟 قائمة الإضافات", "🥤 مشروبات"])

with col_main:
    st.header(category)
    # وجبات البرغر (اللي طلبت ترجعها)
    if category == "🍔 برغرات الساحل":
        items = [("كلاسيك برغر دجاج", 2.50), ("كلاسيك برغر لحم", 2.95), ("وجبة برغر دبل", 3.95)]
        for name, price in items:
            st.markdown(f"<div class='menu-item-card'><b>{name}</b><br><span style='color:#ff4b4b;'>{price:.2f} JOD</span></div>", unsafe_allow_html=True)
            if st.button(f"إضافة {name}"):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.rerun()
    else:
        st.info("اختر الوجبات من الأقسام الأخرى")

with col_cart:
    st.markdown("## My Order")
    for i, item in enumerate(st.session_state.cart):
        st.write(f"📍 {item['n']} - {item['p']:.2f}")
    
    st.subheader(f"المجموع: {st.session_state.total:.2f} JOD")
    u_name = st.text_input("الاسم")
    u_phone = st.text_input("الهاتف")
    
    if st.button("إرسال الطلب 🚀"):
        if u_name and u_phone and st.session_state.cart:
            order_msg = f"<b>🔔 طلب جديد!</b>\n👤 الزبون: {u_name}\n📞 الهاتف: {u_phone}\n💰 المجموع: {st.session_state.total:.2f} JOD"
            send_telegram_notification(order_msg)
            st.success("تم الإرسال! شيك تليجرامك هسا")
