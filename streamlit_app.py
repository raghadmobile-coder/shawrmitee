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
st.set_page_config(page_title="مطعم الضيعة | Al-Deera", page_icon="🍖", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- الستايل المطور (أزرق ملكي بدون صور) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * {{ font-family: 'Cairo', sans-serif; direction: rtl; color: white !important; }}
    
    .stApp {{
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        min-height: 100vh;
    }}
    
    /* شريط التنقل العلوي المحسن */
    .nav-container {{
        display: flex; justify-content: center; gap: 20px; padding: 15px;
        background: rgba(255, 255, 255, 0.1); border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2); margin-bottom: 30px;
    }}
    
    /* كرت الوجبة الأنيق (بدون صورة) */
    .item-box {{
        background: rgba(255, 255, 255, 0.08);
        padding: 20px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 15px; transition: 0.3s; text-align: right;
    }}
    .item-box:hover {{ background: rgba(255, 255, 255, 0.15); border-color: white; }}
    
    .price-tag {{ color: #FFD700 !important; font-weight: bold; font-size: 1.2rem; }}
    
    .whatsapp-float {{
        position: fixed; width: 60px; height: 60px; bottom: 40px; left: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
        box-shadow: 2px 5px 15px rgba(0,0,0,0.3); z-index: 100;
        display: flex; align-items: center; justify-content: center;
    }}
    
    /* سلة المشتريات الجانبية */
    .cart-section {{
        background: white !important; padding: 20px; border-radius: 20px;
        border: none; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }}
    .cart-section * {{ color: #0077B6 !important; }}
    </style>
    
    <a href="https://wa.me/{MY_WHATSAPP}" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
    </a>
""", unsafe_allow_html=True)

# --- الهيدر (Navigation) ---
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("🏠 الرئيسية", use_container_width=True): st.session_state.page = 'home'; st.rerun()
with col_n2:
    if st.button("📋 المنيو", use_container_width=True): st.session_state.page = 'menu'; st.rerun()
with col_n3:
    if st.button("📧 تواصل معنا", use_container_width=True): st.session_state.page = 'contact'; st.rerun()

st.divider()

# --- البيانات المنظمة (بدون صور) ---
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
    ],
    "🍟 المقبلات والمشروبات": [
        {"n": "صحن بطاطا عائلي", "p": 1.50},
        {"n": "مثومة / شطة إضافية", "p": 0.25},
        {"n": "مشروب غازي", "p": 0.50}
    ]
}

# --- منطق الصفحات ---
if st.session_state.page == 'home':
    st.markdown("""
        <div style='text-align: center; padding: 60px 20px;'>
            <h1 style='font-size: 65px; font-weight: 900; margin-bottom: 10px;'>مطعم الضيعة</h1>
            <p style='font-size: 24px; opacity: 0.9;'>أشهى وجبات الشاورما والبروستد في الأردن</p>
            <div style='margin-top: 30px; border: 2px solid white; display: inline-block; padding: 10px 30px; border-radius: 50px;'>
                📞 0799633096
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'menu':
    m_col, c_col = st.columns([2.5, 1])
    
    with m_col:
        # عرض القوائم بشكل منفصل
        for cat, items in menu_data.items():
            st.markdown(f"### ✨ {cat}")
            for item in items:
                col_item, col_btn = st.columns([4, 1])
                with col_item:
                    st.markdown(f"""
                        <div class="item-box">
                            <span style="font-size: 1.3rem; font-weight: bold;">{item['n']}</span><br>
                            <span class="price-tag">{item['p']:.2f} JOD</span>
                        </div>
                    """, unsafe_allow_html=True)
                with col_btn:
                    st.write("") # موازنة المسافة
                    if st.button("➕", key=f"add_{item['n']}", use_container_width=True):
                        st.session_state.cart.append(item)
                        st.session_state.total += item['p']
                        st.rerun()

    with c_col:
        st.markdown("<div class='cart-section'>", unsafe_allow_html=True)
        st.subheader("🛒 طلباتك")
        if not st.session_state.cart:
            st.write("ابدأ بإضافة الوجبات")
        else:
            for item in st.session_state.cart:
                st.write(f"• {item['n']} ({item['p']:.2f})")
            st.markdown(f"**💰 المجموع: {st.session_state.total:.2f} JOD**")
            
            u_name = st.text_input("الأسم")
            u_phone = st.text_input("رقم الهاتف")
            
            if st.button("إرسال الطلب (تليجرام)", use_container_width=True):
                if u_name and u_phone:
                    items_list = "\n".join([f"- {i['n']}" for i in st.session_state.cart])
                    msg = f"📦 طلب جديد!\nالاسم: {u_name}\nالهاتف: {u_phone}\nالطلبات:\n{items_list}\nالمجموع: {st.session_state.total:.2f}"
                    send_telegram_notification(msg)
                    st.success("وصل الطلب!")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    time.sleep(1); st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    st.markdown("""
        <div style='text-align: center; padding: 40px;'>
            <h2>تواصل معنا مباشرة</h2>
            <p>نحن جاهزون لخدمتكم دائماً</p>
            <h1 style='color: #FFD700 !important;'>0799633096</h1>
            <p>📍 الموقع: عمّان - الأردن</p>
        </div>
    """, unsafe_allow_html=True)
