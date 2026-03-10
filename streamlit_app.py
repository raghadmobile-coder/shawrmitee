import streamlit as st
import requests
import time

# --- إعدادات الربط (تأكد من صحتها) ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# --- إعدادات الصفحة ---
st.set_page_config(page_title="الضيعة | Al-Deera Restaurant", page_icon="🍖", layout="wide")

# --- إدارة الحالة (Session State) ---
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'lang' not in st.session_state: st.session_state.lang = 'ar'
if 'order_status' not in st.session_state: st.session_state.order_status = None

# --- النصوص (عربي/إنجليزي) ---
texts = {
    'ar': {
        'title': 'مطعم الضيعة', 'home': 'الرئيسية', 'menu': 'القائمة', 'contact': 'تواصل معنا',
        'hero_sub': 'طعم أصيل | جودة عالية | أسعار منافسة', 'add': 'أضف للسلة', 'cart': 'سلة المشتريات',
        'send': 'إرسال الطلب عبر واتساب وتليجرام', 'name': 'الاسم الكامل', 'phone': 'رقم الهاتف',
        'location': 'رابط الموقع (Google Maps)', 'tracking': 'تتبع طلبك'
    },
    'en': {
        'title': 'Al-Deera Restaurant', 'home': 'Home', 'menu': 'Menu', 'contact': 'Contact Us',
        'hero_sub': 'Authentic Taste | High Quality | Best Prices', 'add': 'Add to Cart', 'cart': 'Your Cart',
        'send': 'Send Order (WhatsApp/Telegram)', 'name': 'Full Name', 'phone': 'Phone Number',
        'location': 'Location Link', 'tracking': 'Track Order'
    }
}
L = texts[st.session_state.lang]

# --- CSS المحسن (مع إضافة الزر العائم وتصميم القوائم) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp {{ font-family: 'Cairo', sans-serif; direction: {'rtl' if st.session_state.lang == 'ar' else 'ltr'}; }}
    
    .hero-container {{
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        padding: 50px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
    }}
    
    .menu-card {{
        background: white; border-radius: 15px; padding: 15px; margin-bottom: 15px;
        border: 1px solid #eee; transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    .menu-card:hover {{ transform: translateY(-5px); border-color: #0095F6; }}
    
    .whatsapp-float {{
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
        font-size: 30px; box-shadow: 2px 2px 3px #999; z-index: 100; display: flex; align-items: center; justify-content: center;
    }}
    
    .status-bar {{
        background: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 20px; border-right: 5px solid #0095F6;
    }}
    </style>
    
    <a href="https://wa.me/962790000000" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
    </a>
""", unsafe_allow_html=True)

# --- Header & Lang Switch ---
col_l, col_r = st.columns([1, 5])
with col_l:
    if st.button("🌐 English/عربي"):
        st.session_state.lang = 'en' if st.session_state.lang == 'ar' else 'ar'
        st.rerun()

# --- Navigation ---
nav_cols = st.columns(3)
if nav_cols[0].button(L['home'], use_container_width=True): st.session_state.page = 'home'; st.rerun()
if nav_cols[1].button(L['menu'], use_container_width=True): st.session_state.page = 'menu'; st.rerun()
if nav_cols[2].button(L['contact'], use_container_width=True): st.session_state.page = 'contact'; st.rerun()

# --- البيانات (Menu Data) ---
items_db = {
    "🌯 Shawarma | شاورما": [
        {"n": "سوبر الضيعة", "p": 2.50, "img": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=400"},
        {"n": "وجبة عربي دبل", "p": 4.50, "img": "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=400"}
    ],
    "🍗 Broasted | بروستد": [
        {"n": "وجبة 4 قطع", "p": 3.75, "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc45a?w=400"},
        {"n": "وليمة 12 قطعة", "p": 10.50, "img": "https://images.unsplash.com/photo-1569058242253-92a9c71f9867?w=400"}
    ]
}

# --- منطق الصفحات ---
if st.session_state.page == 'home':
    st.markdown(f"<div class='hero-container'><h1>{L['title']}</h1><p>{L['hero_sub']}</p></div>", unsafe_allow_html=True)
    if st.session_state.order_status:
        st.markdown(f"<div class='status-bar'><h3>📍 {L['tracking']}</h3><p>حالة الطلب: <b>{st.session_state.order_status}</b></p></div>", unsafe_allow_html=True)

elif st.session_state.page == 'menu':
    col_m, col_c = st.columns([3, 1.2])
    with col_m:
        for cat, items in items_db.items():
            st.subheader(cat)
            m_cols = st.columns(2)
            for idx, item in enumerate(items):
                with m_cols[idx % 2]:
                    st.markdown(f"""<div class='menu-card'>
                        <img src='{item['img']}' style='width:100%; border-radius:10px;'>
                        <h4>{item['n']}</h4><p>{item['p']:.2f} JOD</p></div>""", unsafe_allow_html=True)
                    if st.button(f"{L['add']} {item['n']}", key=f"btn_{item['n']}"):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()
    with col_c:
        st.header(L['cart'])
        for i, item in enumerate(st.session_state.cart):
            st.write(f"• {item['n']} ({item['p']:.2f})")
        st.write(f"**Total: {st.session_state.total:.2f} JOD**")
        
        name = st.text_input(L['name'])
        phone = st.text_input(L['phone'])
        loc = st.text_input(L['location'])
        
        if st.button(L['send']):
            if name and phone and st.session_state.cart:
                msg = f"طلب جديد من {name}\nالهاتف: {phone}\nالموقع: {loc}\nالمجموع: {st.session_state.total}"
                send_telegram_notification(msg)
                st.session_state.order_status = "جاري التحضير في المطبخ... 👨‍🍳"
                st.success("تم استلام طلبك!")
                time.sleep(2)
                st.session_state.page = 'home'; st.rerun()

elif st.session_state.page == 'contact':
    st.header(L['contact'])
    st.write("📍 عمّان - الأردن | 📞 0790000000")
    st.image("https://maps.googleapis.com/maps/api/staticmap?center=31.9454,35.9284&zoom=13&size=600x300&key=YOUR_KEY") # تجريبي
