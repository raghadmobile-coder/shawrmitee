import streamlit as st

# 1. إعدادات الصفحة والديزاين (CSS) لعمل خلفية 3D وألوان فخمة
st.set_page_config(page_title="Shawarma Al-Saj | شاورما ع الصاج", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #4b0000 100%);
        color: white;
    }
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ff4b4b;
        text-shadow: 2px 2px 10px #000;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .menu-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 75, 75, 0.3);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_status=True)

# 2. اختيار اللغة والاستقبال
col_lang1, col_lang2 = st.columns([8, 2])
with col_lang2:
    lang = st.selectbox("🌐 Language", ["العربية", "English"])

if lang == "العربية":
    title = "🌯 مطعم شاورما ع الصاج الذكي"
    welcome_msg = "أهلاً بك في عالم القرمشة! نورتنا يا غالي، شو بنقدر نضبطلك اليوم؟"
    order_btn = "تأكيد الطلب 🚀"
else:
    title = "🌯 Shawarma Al-Saj Smart Bot"
    welcome_msg = "Welcome to the world of crunch! What can we prepare for you today?"
    order_btn = "Confirm Order 🚀"

st.markdown(f"<h1 class='main-title'>{title}</h1>", unsafe_allow_status=True)
st.write(f"### {welcome_msg}")

# 3. المنيو الضخم (شاورما، برغر، بروستد، مشروبات)
menu = {
    "قسم الشاورما": {
        "ساندويش صاج عادي": 1.75,
        "وجبة سوبر صاج": 3.50,
        "سدر العيلة الملكي": 18.00
    },
    "قسم البرغر": {
        "كلاسيك برغر لحم": 3.00,
        "تشيكن برغر زقرت": 2.75,
        "وجبة برغر دبل": 5.00
    },
    "قسم البروستد": {
        "وجبة بروستد 4 قطع": 4.50,
        "وجبة بروستد عائلية 8 قطع": 8.50
    },
    "المشروبات": {
        "علبة ماتريكس": 0.50,
        "عصير برتقال طبيعي": 1.50,
        "مياه معدنية": 0.25
    }
}

# 4. اختيار الطلبات بدقة
selected_items = {}
st.sidebar.header("🛒 سلة المشتريات")

tabs = st.tabs(list(menu.keys()))
for i, category in enumerate(menu.keys()):
    with tabs[i]:
        st.subheader(f"🔥 {category}")
        cols = st.columns(len(menu[category]))
        for j, (item, price) in enumerate(menu[category].items()):
            with cols[j]:
                st.markdown(f"<div class='menu-card'><b>{item}</b><br>{price} JOD</div>", unsafe_allow_status=True)
                if st.button(f"أضف {item}", key=item):
                    selected_items[item] = price
                    st.toast(f"تم إضافة {item}")

# 5. ملخص الطلب والرد الذكي
total = sum(selected_items.values())

if total > 0:
    st.sidebar.markdown("---")
    st.sidebar.write("### طلباتك الحالية:")
    for itm, prc in selected_items.items():
        st.sidebar.write(f"- {itm}: {prc} JOD")
    
    st.sidebar.write(f"## المجموع: {total:.2f} JOD")
    
    if st.sidebar.button(order_btn):
        st.balloons()
        st.success("تم إرسال طلبك بنجاح!")
        
        # رد الـ AI المميز
        if "سدر العيلة الملكي" in selected_items:
            st.info("🤖 AI: السدر الملكي بدو طاوله قوية! اختيار الملوك، رح نوصي فيك بالثومية!")
        elif "علبة ماتريكس" in selected_items:
            st.info("🤖 AI: ماتريكس وبرغر؟ هيك السهرة كملت! صحتين وعافية.")
        elif total > 10:
            st.info("🤖 AI: فاتورة دسمة لعيونك! رح نبعتلك عصير برتقال طبيعي ضيافة من المحل.")
