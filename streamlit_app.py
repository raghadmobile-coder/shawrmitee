import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shawarma Al-Saj | القمة", page_icon="🌯", layout="wide")

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0
if 'confirmed_orders' not in st.session_state: st.session_state.confirmed_orders = []

# --- CSS (البوابة الأصلية + المنيو الضخم) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at center, #1a0000 0%, #000000 100%); color: white; font-family: 'Cairo', sans-serif; }
    
    /* البوابة الملكية كما في الصورة */
    .info-box { 
        text-align: center; padding: 45px; background: rgba(0, 0, 0, 0.85); 
        border: 3px solid #ff4b4b; border-radius: 30px; max-width: 650px; 
        margin: 80px auto 20px auto; box-shadow: 0 0 30px rgba(255, 75, 75, 0.6); 
    }
    .shop-title { font-size: 50px; font-weight: 900; color: #ff4b4b; margin-bottom: 5px; }

    /* أزرار اللغة - يسار الشاشة */
    .lang-container { display: flex; flex-direction: column; width: 200px; margin-left: 10%; margin-top: 30px; }
    .stButton > button { width: 100% !important; border-radius: 12px !important; font-weight: bold !important; padding: 12px !important; }

    /* الأصناف الجانبية - بلوكات ضخمة */
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 75, 75, 0.1) !important;
        padding: 25px !important; border-radius: 15px !important;
        font-size: 24px !important; font-weight: 900 !important;
        border: 2px solid #ff4b4b !important; margin-bottom: 15px;
        color: white !important;
    }

    /* كروت الطعام الضخمة */
    .menu-item-card { 
        background: rgba(255, 255, 255, 0.04); border-right: 10px solid #ff4b4b; 
        padding: 40px; border-radius: 20px; margin-bottom: 30px; 
        text-align: right; direction: rtl; 
    }
    .item-name { font-size: 38px; font-weight: 900; color: #fff; }
    .item-price { font-size: 32px; color: #ff4b4b; font-weight: 900; }
    .item-desc { font-size: 20px; color: #bbb; margin-top: 10px; }
    .nutrition { font-size: 16px; color: #00ffcc; font-weight: bold; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. البوابة الملكية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div class='info-box'>
            <div class='shop-title'>SHAWARMA AL-SAJ</div>
            <div class='shop-details'>
                👑 شاورما ع الصاج.. أصل الطعم والريادة<br>
                📍 فروعنا تخدمكم في كل مكان<br>
                📞 الخط الساخن: 079-0000000
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_lang, _ = st.columns([1, 3])
    with col_lang:
        st.markdown("<div class='lang-container'>", unsafe_allow_html=True)
        if st.button("تفضل للمنيو 🇯🇴"): st.session_state.page = 'menu'; st.rerun()
        if st.button("English Menu 🇺🇸"): st.session_state.page = 'menu'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. المنيو الشامل ---
elif st.session_state.page == 'menu':
    col_side, col_main, col_cart = st.columns([0.8, 2.2, 1.2])

    with col_side:
        st.markdown("<h2 style='text-align:center;'>الأقسام</h2>", unsafe_allow_html=True)
        category = st.radio("", ["🔥 العروض والأوفرات", "🌯 ساندويشات الشاورما", "🍱 وجبات الشاورما", "👨‍👩‍👧‍👦 وجبات العيلة", "🍔 الزنجر والتندر", "🥤 مشروبات"])

    with col_main:
        st.markdown(f"<h1 style='text-align:right; color:#ff4b4b;'>{category}</h1>", unsafe_allow_html=True)
        
        # بيانات المنيو الضخم
        menu_items = {
            "🔥 العروض والأوفرات": [
                ("أوفر الصحاب (2 سوبر)", 6.50, "2 ساندويش سوبر + بطاطا لارج + كولا لتر", "بروتين: 65غ | دهون: 30غ"),
                ("عرض الـ 3 وجبات عادي", 8.00, "3 وجبات عربي عادي + مخللات وثومية", "بروتين: 90غ | دهون: 45غ"),
                ("وجبة التوفير اليومية", 2.50, "ساندويش عادي + بطاطا + كولا علبة", "بروتين: 25غ | دهون: 12غ")
            ],
            "🌯 ساندويشات الشاورما": [
                ("ساندويش عادي", 1.85, "خبز صاج، ثومية، مخلل", "بروتين: 22غ | دهون: 10غ"),
                ("ساندويش سوبر", 2.75, "حجم أكبر، دجاج أكثر", "بروتين: 32غ | دهون: 14غ"),
                ("ساندويش دبل", 3.50, "دبل دجاج لعشاق الشاورما", "بروتين: 45غ | دهون: 18غ"),
                ("ساندويش تربل (العملاق)", 4.25, "ثلاث أضعاف الدجاج، طعم لا يقاوم", "بروتين: 60غ | دهون: 22غ")
            ],
            "🍱 وجبات الشاورما": [
                ("وجبة عربي عادي", 2.75, "ساندويش مقطع، بطاطا، ثومية، مخلل", "بروتين: 25غ | دهون: 15غ"),
                ("وجبة عربي سوبر", 3.75, "ساندويش سوبر مقطع، بطاطا، ثومية", "بروتين: 35غ | دهون: 18غ"),
                ("وجبة عربي تربل", 5.50, "ساندويش تربل مقطع، بطاطا دبل، ثومية", "بروتين: 65غ | دهون: 25غ"),
                ("وجبة فرط (250غ)", 5.50, "دجاج صافي بدون خبز مع سرفيس", "بروتين: 50غ | دهون: 20غ")
            ],
            "👨‍👩‍👧‍👦 وجبات العيلة": [
                ("سدر العيلة الصغير (شخصين)", 7.50, "24 قطعة شاورما + بطاطا + ثومية", "بروتين: 70غ | دهون: 35غ"),
                ("سدر العيلة الوسط (4 أشخاص)", 12.50, "48 قطعة شاورما + بطاطا وسط + كولا", "بروتين: 140غ | دهون: 65غ"),
                ("السدر الملكي (عائلي ضخم)", 18.50, "64 قطعة شاورما + بطاطا عائلية + 2 كولا", "بروتين: 190غ | دهون: 90غ")
            ],
            "🍔 الزنجر والتندر": [
                ("ساندويش زنجر سوبريم", 3.25, "صدر دجاج، جبنة، خس، مايونيز", "بروتين: 28غ | دهون: 18غ"),
                ("وجبة تندر (5 قطع)", 4.50, "تندر مقرمش، بطاطا، صوص رانش", "بروتين: 35غ | دهون: 20غ")
            ],
            "🥤 مشروبات": [
                ("كولا / سبرايت", 0.60, "بارد منعش", "0"),
                ("برتقال طبيعي فريش", 1.75, "طبيعي 100%", "بروتين: 1غ")
            ]
        }

        for name, price, desc, nut in menu_items[category]:
            st.markdown(f"""
                <div class='menu-item-card'>
                    <div style='display:flex; justify-content:space-between; direction:ltr;'>
                        <span class='item-price'>{price:.2f} JOD</span>
                        <span class='item-name'>{name}</span>
                    </div>
                    <div class='item-desc'>{desc}</div>
                    <div class='nutrition'>📊 {nut}</div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("تخصيص الوجبة (إضافات / ملاحظات)"):
                col1, col2 = st.columns(2)
                extra_ch = col1.checkbox("زيادة جبنة (+0.50)", key=f"ex_{name}")
                no_pk = col2.checkbox("بدون مخلل", key=f"pk_{name}")
                user_note = st.text_input("ملاحظات خاصة", placeholder="مثلاً: خبز محمر...", key=f"note_{name}")
                
                if st.button(f"أضف {name} للسلة", key=f"btn_{name}", use_container_width=True):
                    p = price + (0.50 if extra_ch else 0)
                    st.session_state.cart.append({'n': name, 'p': p, 'note': user_note, 'extra': "جبنة" if extra_ch else ""})
                    st.session_state.total += p
                    st.toast("تمت الإضافة!")

    with col_cart:
        st.markdown("<div style='background:#000; padding:20px; border-radius:20px; border:1px solid #333;'>", unsafe_allow_html=True)
        st.header("🛒 طلبك")
        for item in st.session_state.cart:
            st.write(f"🔹 **{item['n']}** ({item['p']:.2f})")
            if item['note']: st.caption(f"ملاحظة: {item['note']}")
        
        st.divider()
        st.subheader(f"الحساب: {st.session_state.total:.2f} JOD")
        u_name = st.text_input("الاسم")
        u_phone = st.text_input("رقم الهاتف")

        if st.button("تأكيد الطلب 🚀", use_container_width=True):
            if u_name and u_phone:
                # الطلب يُخزن للـ AI فقط
                st.session_state.confirmed_orders.append({"name": u_name, "phone": u_phone, "items": st.session_state.cart, "total": st.session_state.total})
                st.success("✅ تم الاستلام! طلبك تحت التحضير.")
                st.session_state.cart = []; st.session_state.total = 0.0
                st.balloons()
            else: st.error("عبي بياناتك يا طيب")
        
        if st.button("تفريغ السلة"): st.session_state.cart=[]; st.session_state.total=0.0; st.rerun()
        if st.button("⬅️ البوابة"): st.session_state.page='welcome'; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# لوحة تحكم الـ AI (مخفية للزبون)
if st.sidebar.checkbox("الطلبات الواردة (للإدارة فقط)"):
    st.sidebar.write(st.session_state.confirmed_orders)
