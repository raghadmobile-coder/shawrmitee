import streamlit as st
import requests

# --- إعدادات التليجرام ---
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN" 
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | My Order", page_icon="🌯", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS التنسيق ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    .menu-item-card { background: rgba(255, 255, 255, 0.03); border-right: 8px solid #ff4b4b; padding: 20px; border-radius: 15px; margin-bottom: 15px; text-align: right; }
    .nutrition-tag { color: #00ffcc; font-size: 14px; font-weight: bold; }
    .order-header { font-size: 30px; font-weight: 900; color: #ff4b4b; text-align: center; margin-bottom: 20px; }
    /* تنسيق زر الحذف الصغير */
    .stButton > button[key^="del_"] { background-color: #ff4b4b !important; color: white !important; border-radius: 5px !important; padding: 0px 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- البوابة ---
if st.session_state.page == 'welcome':
    st.markdown("<div style='text-align:center; padding:50px;'><h1 style='color:#ff4b4b; font-size:50px;'>SHAWARMA AL-SAJ</h1><p>الطعم الملكي في انتظارك</p></div>", unsafe_allow_html=True)
    if st.button("دخول للمنيو 🇯🇴", use_container_width=True): st.session_state.page = 'menu'; st.rerun()

# --- المنيو ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.9, 2.1, 1.2])

    with col_side:
        st.markdown("<h3 style='text-align:center;'>الأقسام</h3>", unsafe_allow_html=True)
        category = st.radio("", ["🔥 العروض الملكية", "🌯 شاورما (أحجام)", "👨‍👩‍👧‍👦 وجبات العيلة", "🍗 بروستد مقرمش", "🍟 قائمة الإضافات (جانبي)", "🥤 مشروبات"])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        # بيانات المنيو مع القيم الغذائية
        menu_items = {
            "🔥 العروض الملكية": [("أوفر الصحاب (2 سوبر)", 6.50, "وجبتين كاملات + كولا", "65g Protein | 1200 Cal")],
            "🌯 شاورما (أحجام)": [("شاورما عادي", 1.85, "صاج أصلي", "22g Protein | 450 Cal"), ("شاورما سوبر", 2.75, "حجم أكبر", "32g Protein | 620 Cal")],
            "👨‍👩‍👧‍👦 وجبات العيلة": [("السدر الملكي", 18.50, "64 قطعة دجاج", "190g Protein | 4500 Cal")],
            "🍗 بروستد مقرمش": [("بروستد 4 قطع", 4.25, "4 قطع + بطاطا + كولا", "35g Protein | 800 Cal")],
            "🍟 قائمة الإضافات (جانبي)": [("بطاطا كبير", 2.25, "مقرمشة", "650 Cal"), ("مثومة كبير", 1.00, "ثومية أصلية", "150 Cal")],
            "🥤 مشروبات": [("كولا", 0.60, "بارد", "140 Cal")]
        }

        for name, price, desc, nut in menu_items[category]:
            st.markdown(f"<div class='menu-item-card'><div style='display:flex; justify-content:space-between; direction:ltr;'><span style='color:#ff4b4b; font-weight:900;'>{price:.2f} JOD</span><span style='font-weight:900;'>{name}</span></div><div style='color:#bbb;'>{desc}</div><div class='nutrition-tag'>📊 {nut}</div></div>", unsafe_allow_html=True)
            if st.button(f"أضف لـ My Order", key=f"add_{name}"):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.rerun()

    # --- قسم My Order المطور (مع خاصية الإلغاء) ---
    with col_cart:
        st.markdown("<div class='order-header'>MY ORDER</div>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.info("سلتك فارغة")
        else:
            # عرض العناصر مع زر حذف لكل عنصر
            for index, item in enumerate(st.session_state.cart):
                c1, c2 = st.columns([4, 1])
                c1.write(f"📍 {item['n']} ({item['p']:.2f})")
                if c2.button("🗑️", key=f"del_{index}"):
                    # عملية الإلغاء قبل التأكيد
                    st.session_state.total -= st.session_state.cart[index]['p']
                    st.session_state.cart.pop(index)
                    st.rerun()
            
            st.divider()
            st.subheader(f"المجموع: {st.session_state.total:.2f} JOD")
            
            u_name = st.text_input("الاسم")
            u_phone = st.text_input("الهاتف")

            if st.button("إرسال الطلب 🚀", use_container_width=True):
                if u_name and u_phone:
                    items_msg = "\n".join([f"• {x['n']}" for x in st.session_state.cart])
                    full_msg = f"<b>🔔 طلب جديد!</b>\n👤 الزبون: {u_name}\n📞 الهاتف: {u_phone}\n📦 الأصناف:\n{items_msg}\n💰 الإجمالي: {st.session_state.total:.2f} JOD"
                    send_telegram_notification(full_msg)
                    st.success("تم الإرسال!")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    st.balloons()
