import streamlit as st
import requests

# --- إعدادات التليجرام لإشعاراتك الخاصة ---
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN" 
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": order_details, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | القمة", page_icon="🌯", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS (العودة للتصميم الأصلي والبلوكات الضخمة) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الأصلية (كما في الصورة 1000064174.heic) */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; box-shadow: 0 0 30px rgba(255, 75, 75, 0.6); 
    }
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; margin-bottom: 5px; }

    /* الأقسام الجانبية - بلوكات ضخمة جداً (كما في الصورة 37038ee7) */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 24px !important; font-weight: 900 !important;
        border: 2px solid #ff4b4b !important; margin-bottom: 15px; color: white !important;
    }

    /* كروت الطعام الضخمة مع القيم الغذائية */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; 
        padding: 40px; border-radius: 20px; margin-bottom: 30px; text-align: right; 
    }
    .item-name { font-size: 34px; font-weight: 900; color: #fff; }
    .item-price { font-size: 30px; color: #ff4b4b; font-weight: 900; }
    .nutrition-tag { color: #00ffcc; font-size: 16px; font-weight: bold; margin-top: 10px; }
    
    /* عنوان My Order */
    .order-header { font-size: 35px; font-weight: 900; color: #ff4b4b; text-align: center; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. البوابة الملكية الأصلية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                👑 الطعم الأصيل.. الجودة الملكية<br>
                📍 فروعنا: عمان - إربد - الزرقاء<br>
                📞 الخط الساخن: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        st.markdown("<div style='margin-left:10%;'>", unsafe_allow_html=True)
        if st.button("دخول للمنيو 🇯🇴"): st.session_state.page = 'menu'; st.rerun()
        if st.button("English Menu 🇺🇸"): st.session_state.page = 'menu'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. المنيو بالبلوكات الكبيرة والترتيب الصحيح ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

    with col_side:
        st.markdown("<h2 style='text-align:center;'>الأقسام</h2>", unsafe_allow_html=True)
        category = st.radio("", [
            "🔥 العروض الملكية", 
            "🌯 شاورما (أحجام)", 
            "👨‍👩‍👧‍👦 وجبات العيلة", 
            "🍗 بروستد مقرمش", 
            "🍟 قائمة الإضافات (جانبي)",
            "🥤 مشروبات"
        ])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        menu_items = {
            "🔥 العروض الملكية": [
                ("أوفر الصحاب (2 سوبر)", 6.50, "2 ساندويش سوبر + بطاطا لارج + كولا", "65g Protein | 1200 Cal"),
                ("عرض الـ 3 وجبات", 8.00, "3 وجبات عربي عادي + سرفيس كامل", "90g Protein | 1800 Cal"),
                ("وجبة التوفير اليومية", 2.50, "ساندويش عادي + بطاطا + كولا علبة", "25g Protein | 600 Cal")
            ],
            "🌯 شاورما (أحجام)": [
                ("شاورما عادي", 1.85, "خبز صاج، ثومية، مخلل", "22g Protein | 450 Cal"),
                ("شاورما سوبر", 2.75, "دجاج إضافي وحجم أكبر", "32g Protein | 620 Cal"),
                ("شاورما دبل", 3.50, "دبل دجاج لعشاق الشاورما", "45g Protein | 800 Cal"),
                ("شاورما تربل (العملاق)", 4.25, "3 أضعاف الدجاج", "60g Protein | 950 Cal")
            ],
            "👨‍👩‍👧‍👦 وجبات العيلة": [
                ("سدر العيلة الملكي", 18.50, "64 قطعة + بطاطا دبل + كولا عائلي", "190g Protein | 4500 Cal")
            ],
            "🍗 بروستد مقرمش": [
                ("بروستد 4 قطع", 4.25, "مع بطاطا وثومية وكولا", "35g Protein | 800 Cal"),
                ("وليمة بروستد 21 قطعة", 18.50, "21 قطعة + بطاطا عائلية دبل + كولا 2 لتر", "190g Protein | 4200 Cal")
            ],
            "🍟 قائمة الإضافات (جانبي)": [
                ("علبة بطاطا - كبير", 2.25, "حجم عائلي مقرمش", "650 Cal"),
                ("علبة مثومة - كبير", 1.00, "ثومية المحل الأصلية", "150 Cal"),
                ("علبة جبنة شيدر", 0.75, "جبنة سائلة ساخنة", "200 Cal"),
                ("صوص المحل الخاص", 0.50, "خلطة الصاج السرية", "120 Cal")
            ],
            "🥤 مشروبات": [("كولا بارد", 0.60, "", "140 Cal")]
        }

        for name, price, desc, nut in menu_items[category]:
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
        st.markdown("<div class='order-header'>MY ORDER</div>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.info("سلتك فارغة")
        else:
            for index, item in enumerate(st.session_state.cart):
                col_item, col_del = st.columns([4, 1])
                col_item.write(f"📍 {item['n']} ({item['p']:.2f})")
                if col_del.button("🗑️", key=f"del_{index}"):
                    st.session_state.total -= st.session_state.cart[index]['p']
                    st.session_state.cart.pop(index)
                    st.rerun()
            
            st.divider()
            st.subheader(f"المجموع: {st.session_state.total:.2f} JOD")
            u_name = st.text_input("الاسم")
            u_phone = st.text_input("رقم الهاتف")

            if st.button("تأكيد وإرسال الطلب 🚀", use_container_width=True):
                if u_name and u_phone:
                    items_txt = "\n".join([f"• {i['n']}" for i in st.session_state.cart])
                    msg = f"<b>🔔 طلب جديد!</b>\n👤 الزبون: {u_name}\n📞 الهاتف: {u_phone}\n📦 الطلبات:\n{items_txt}\n💰 الإجمالي: {st.session_state.total:.2f} JOD"
                    send_telegram_notification(msg)
                    st.success("تم الإرسال!")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    st.balloons()
