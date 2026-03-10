import streamlit as st
import requests

# --- إعدادات إشعارات التليجرام (الحل الجذري للمسجات) ---
# ملاحظة: للحصول على التوكن، ابحث عن @BotFather في تليجرام وأنشئ بوت جديد.
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

# --- CSS التنسيق المطور ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية */
    .info-box { 
        text-align: center; padding: 40px; background: rgba(0, 0, 0, 0.85); 
        border: 2px solid #ff4b4b; border-radius: 25px; margin: 40px auto; 
    }
    
    /* أزرار الأقسام الضخمة */
    .stRadio div[role="radiogroup"] label {
        background: #111 !important; padding: 20px !important; border-radius: 12px !important;
        font-size: 22px !important; font-weight: 700 !important;
        border: 1px solid #ff4b4b !important; margin-bottom: 12px; color: white !important;
    }

    /* كروت المنيو مع القيم الغذائية */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.03); border-right: 8px solid #ff4b4b; 
        padding: 30px; border-radius: 15px; margin-bottom: 20px; text-align: right; 
    }
    .nutrition-tag { color: #00ffcc; font-size: 14px; font-weight: bold; margin-top: 8px; }
    
    /* عنوان السلة الجديد */
    .order-header { font-size: 32px; font-weight: 900; color: #ff4b4b; margin-bottom: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. صفحة الترحيب ---
if st.session_state.page == 'welcome':
    st.markdown("<div class='info-box'><h1 style='color:#ff4b4b;'>SHAWARMA AL-SAJ</h1><p>الطعم الأصيل.. الجودة الملكية</p></div>", unsafe_allow_html=True)
    col_l, _ = st.columns([1, 2])
    with col_l:
        if st.button("دخول للمنيو / Enter Menu 🇯🇴", use_container_width=True): 
            st.session_state.page = 'menu'; st.rerun()

# --- 2. صفحة المنيو الرئيسي ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.9, 2.1, 1.2])

    # --- الأقسام (الترتيب اللي طلبته) ---
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

    # --- عرض الوجبات مع القيم الغذائية ---
    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        menu_db = {
            "🔥 العروض الملكية": [
                ("أوفر الصحاب (2 سوبر)", 6.50, "وجبتين كاملات مع كولا لتر", "65g Protein | 1200 Cal"),
                ("بوكس التوفير", 3.00, "وجبة عربي عادي + كولا علبة", "25g Protein | 600 Cal")
            ],
            "🌯 شاورما (أحجام)": [
                ("شاورما عادي", 1.85, "خبز صاج، ثومية، مخلل", "22g Protein | 450 Cal"),
                ("شاورما سوبر", 2.75, "دجاج إضافي وحجم أكبر", "32g Protein | 620 Cal"),
                ("شاورما تربل", 4.25, "العملاق - 3 أضعاف الدجاج", "60g Protein | 950 Cal")
            ],
            "👨‍👩‍👧‍👦 وجبات العيلة": [
                ("السدر الملكي (شاورما)", 18.50, "64 قطعة + بطاطا دبل + كولا عائلي", "190g Protein | 4500 Cal")
            ],
            "🍗 بروستد مقرمش": [
                ("بروستد 4 قطع", 4.25, "مع بطاطا وثومية وكولا", "35g Protein | 800 Cal"),
                ("بروستد 12 قطعة", 11.50, "حجم عائلي", "110g Protein | 2400 Cal"),
                ("سدر بروستد 21 قطعة", 18.50, "وليمة ضخمة", "190g Protein | 4200 Cal")
            ],
            "🍟 قائمة الإضافات (جانبي)": [
                ("بطاطا (صغير)", 1.25, "مقرمشة", "300 Cal"),
                ("بطاطا (كبير)", 2.25, "حجم عائلي", "650 Cal"),
                ("مثومة (3 أحجام)", 0.35, "ثومية المحل الأصلية", "150 Cal"),
                ("علبة جبنة شيدر", 0.75, "جبنة سائلة ساخنة", "200 Cal"),
                ("صوص المحل الخاص", 0.50, "خلطة الصاج السرية", "120 Cal")
            ],
            "🥤 مشروبات": [("كولا بارد", 0.60, "", "140 Cal")]
        }

        for name, price, desc, nut in menu_db[category]:
            st.markdown(f"""
                <div class='menu-item-card'>
                    <div style='display:flex; justify-content:space-between; direction:ltr;'>
                        <span style='font-size:24px; color:#ff4b4b; font-weight:900;'>{price:.2f} JOD</span>
                        <span style='font-size:26px; font-weight:900;'>{name}</span>
                    </div>
                    <div style='color:#bbb;'>{desc}</div>
                    <div class='nutrition-tag'>📊 {nut}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"أضف لـ My Order", key=name):
                st.session_state.cart.append({'n': name, 'p': price})
                st.session_state.total += price
                st.toast(f"تم إضافة {name}")

    # --- قسم السلة المطور (My Order) ---
    with col_cart:
        st.markdown("<div class='order-header'>MY ORDER</div>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.info("سلتك فارغة.. جرب عروضنا!")
        else:
            for i, item in enumerate(st.session_state.cart):
                st.write(f"✅ {item['n']} - {item['p']:.2f} JOD")
            
            st.divider()
            st.subheader(f"المجموع: {st.session_state.total:.2f} JOD")
            
            u_name = st.text_input("الاسم الشخصي")
            u_phone = st.text_input("رقم التواصل")

            if st.button("إرسال الطلب للمطعم 🚀", use_container_width=True):
                if u_name and u_phone:
                    # تحضير رسالة التليجرام
                    items_list = "\n".join([f"• {x['n']}" for x in st.session_state.cart])
                    msg = f"<b>🔔 طلب جديد من الموقع!</b>\n\n👤 <b>الزبون:</b> {u_name}\n📞 <b>الهاتف:</b> {u_phone}\n\n📦 <b>الأصناف:</b>\n{items_list}\n\n💰 <b>الإجمالي:</b> {st.session_state.total:.2f} JOD"
                    
                    # إرسال الإشعار
                    send_telegram_notification(msg)
                    
                    st.success(f"تم استلام طلبك يا {u_name}! سيتم الاتصال بك.")
                    st.session_state.cart = []; st.session_state.total = 0.0
                    st.balloons()
                else:
                    st.error("يرجى إدخال الاسم والرقم")
        
        if st.button("⬅️ عودة للبوابة"): st.session_state.page='welcome'; st.rerun()
