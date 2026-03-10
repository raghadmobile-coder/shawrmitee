import streamlit as st
import requests

# --- إعدادات الربط النهائية (جاهزة للعمل) ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | نظام الطلبات", page_icon="🌯", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS (التصميم الأصلي: بلوكات ضخمة وبوابة ملكية) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية الأصلية */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; box-shadow: 0 0 30px rgba(255, 75, 75, 0.6); 
    }
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; margin-bottom: 5px; }

    /* الأقسام الجانبية - بلوكات ضخمة جداً */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 24px !important; font-weight: 900 !important;
        border: 2px solid #ff4b4b !important; margin-bottom: 15px; color: white !important;
    }

    /* كروت الطعام الضخمة */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; 
        padding: 40px; border-radius: 20px; margin-bottom: 30px; text-align: right; 
    }
    .item-name { font-size: 34px; font-weight: 900; color: #fff; }
    .item-price { font-size: 30px; color: #ff4b4b; font-weight: 900; }
    .nutrition-tag { color: #00ffcc; font-size: 16px; font-weight: bold; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- البوابة الملكية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                👑 الطعم الملكي الأصيل ع الصاج<br>
                📍 فروعنا بخدمتكم في كل مكان<br>
                📞 الخط الساخن: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("دخول للمنيو 🇯🇴", use_container_width=True):
        st.session_state.page = 'menu'
        st.rerun()

# --- صفحة المنيو الرئيسي ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

    with col_side:
        category = st.radio("الأقسام", [
            "🔥 العروض الملكية", 
            "🌯 شاورما (أحجام)", 
            "🍔 برغرات الساحل", 
            "👨‍👩‍👧‍👦 وجبات العيلة", 
            "🍗 بروستد مقرمش", 
            "🍟 قائمة الإضافات (جانبي)",
            "🥤 مشروبات"
        ])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        items_db = {
            "🔥 العروض الملكية": [
                ("أوفر الصحاب (2 سوبر)", 4.95, "2 ساندويش سوبر + بطاطا + كولا", "65g Protein | 1200 Cal"),
                ("عرض الـ 3 وجبات", 6.50, "3 وجبات عربي عادي + سرفيس كامل", "90g Protein | 1800 Cal")
            ],
            "🌯 شاورما (أحجام)": [
                ("شاورما عادي", 1.25, "خبز صاج، ثومية، مخلل", "22g Protein | 450 Cal"),
                ("شاورما سوبر", 1.95, "دجاج إضافي وحجم أكبر", "32g Protein | 620 Cal")
            ],
            "🍔 برغرات الساحل": [
                ("كلاسيك برغر دجاج", 2.50, "صدر دجاج، جبنة، خس، صوص", "28g Protein | 550 Cal"),
                ("كلاسيك برغر لحم", 2.95, "لحم بقري، جبنة، مخلل، صوص", "26g Protein | 600 Cal"),
                ("وجبة برغر دبل", 3.95, "2 شريحة جبنة + بطاطا + كولا", "45g Protein | 850 Cal")
            ],
            "👨‍👩‍👧‍👦 وجبات العيلة": [
                ("سدر العيلة الملكي", 14.95, "64 قطعة + بطاطا دبل + كولا عائلي", "190g Protein | 4500 Cal")
            ],
            "🍗 بروستد مقرمش": [
                ("بروستد 4 قطع", 3.25, "مع بطاطا وثومية وكولا", "35g Protein | 800 Cal")
            ],
            "🍟 قائمة الإضافات (جانبي)": [
                ("علبة بطاطا - كبير", 1.50, "حجم عائلي مقرمش", "650 Cal"),
                ("علبة مثومة - كبير", 0.75, "ثومية المحل الأصلية", "150 Cal")
            ],
            "🥤 مشروبات": [("كولا بارد", 0.45, "", "140 Cal")]
        }

        for name, price, desc, nut in items_db[category]:
            st.markdown(f"""
                <div class='menu-item-card'>
                    <div style='display:flex; justify-content:space-between; direction:ltr;'>
                        <span class='item-price'>{price:.2f} JOD</span>
                        <span class='item-name'>{name}</span>
                    </div>
                    <div style='color:#bbb;'>{desc}</div>
                    <div class='nutrition-tag'>📊 {nut}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"إضافة لـ My Order", key=f"add_{name}"):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.rerun()

    # --- قسم My Order (مع خيار الحذف) ---
    with col_cart:
        st.markdown("<h2 style='text-align:center; color:#ff4b4b;'>MY ORDER</h2>", unsafe_allow_html=True)
        if not st.session_state.cart:
            st.info("سلتك فاضية يا غالي!")
        else:
            for index, item in enumerate(st.session_state.cart):
                c_item, c_del = st.columns([4, 1])
                c_item.write(f"📍 {item['n']} ({item['p']:.2f})")
                if c_del.button("🗑️", key=f"del_{index}"):
                    st.session_state.total -= st.session_state.cart[index]['p']
                    st.session_state.cart.pop(index)
                    st.rerun()
            
            st.divider()
            st.subheader(f"المجموع: {st.session_state.total:.2f} JOD")
            u_name = st.text_input("الاسم")
            u_phone = st.text_input("الهاتف")

            if st.button("إرسال الطلب للمطعم 🚀", use_container_width=True):
                if u_name and u_phone:
                    items_txt = "\n".join([f"• {x['n']}" for x in st.session_state.cart])
                    full_msg = f"<b>🔔 طلب جديد!</b>\n👤 الزبون: {u_name}\n📞 الهاتف: {u_phone}\n📦 الطلبات:\n{items_txt}\n💰 الإجمالي: {st.session_state.total:.2f} JOD"
                    send_telegram_notification(full_msg)
                    st.success("تم الإرسال!")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    st.balloons()
