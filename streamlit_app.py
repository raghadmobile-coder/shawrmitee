import streamlit as st

# 1. إعدادات الصفحة والديزاين (الأحمر والأسود الفخم)
st.set_page_config(page_title="شاورما ع الصاج - النسخة الملكية", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    /* خلفية متدرجة فخمة */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #3d0000 100%);
        color: white;
    }
    /* عنوان 3D */
    .main-title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        color: #ff0000;
        text-shadow: 3px 3px 15px #ff4b4b, 0 0 25px #000;
        margin-bottom: 20px;
    }
    /* تنسيق الكروت */
    .menu-card {
        background: rgba(40, 0, 0, 0.6);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #ff0000;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.5);
    }
    .menu-card:hover {
        transform: scale(1.05);
        box-shadow: 0px 15px 30px rgba(255,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True) # تم تصحيح الكلمة هنا

# 2. الاستقبال واختيار اللغة
lang = st.sidebar.radio("🌐 Choose Language / اختر اللغة", ["العربية", "English"])

if lang == "العربية":
    st.markdown("<h1 class='main-title'>🌯 شاورما ع الصاج الذكي</h1>", unsafe_allow_html=True)
    st.write("### 🔥 أهلاً بك يا غالي! شرفتنا بمطعمنا، اطلب وتدلل..")
    categories = ["الشاورما", "البرغر", "البروستد", "المشروبات"]
else:
    st.markdown("<h1 class='main-title'>🌯 Smart Shawarma Saj</h1>", unsafe_allow_html=True)
    st.write("### 🔥 Welcome! The best food is waiting for you..")
    categories = ["Shawarma", "Burgers", "Broasted", "Drinks"]

# 3. المنيو الضخم
menu = {
    "الشاورما": {"ساندويش صاج": 1.75, "وجبة دبل": 4.50, "سدر العيلة الملكي": 18.00},
    "البرغر": {"كلاسيك برغر لحم": 3.00, "وجبة برغر دبل": 5.50, "زنجر سوبريم": 3.25},
    "البروستد": {"وجبة 4 قطع": 4.75, "وجبة عائلية 8 قطع": 9.00},
    "المشروبات": {"علبة ماتريكس": 0.50, "عصير برتقال طبيعي": 1.50, "عصير تقال": 1.25}
}

# 4. نظام الطلبات
if 'cart' not in st.session_state:
    st.session_state.cart = []

tabs = st.tabs(categories)
for i, cat in enumerate(menu.keys()):
    with tabs[i]:
        cols = st.columns(3)
        for j, (item, price) in enumerate(menu[cat].items()):
            with cols[j % 3]:
                st.markdown(f"<div class='menu-card'><h3>{item}</h3><p style='color:#ff4b4b; font-size:20px;'>{price} JOD</p></div>", unsafe_allow_html=True)
                if st.button(f"أضف {item}", key=item):
                    st.session_state.cart.append({"name": item, "price": price})
                    st.toast(f"✅ {item} انضاف للسلة")

# 5. الفاتورة والـ AI
st.sidebar.markdown("## 🛒 سلتك")
total = sum(item['price'] for item in st.session_state.cart)

for order in st.session_state.cart:
    st.sidebar.write(f"- {order['name']} ({order['price']} JOD)")

st.sidebar.write(f"### المجموع: {total:.2f} JOD")

if st.sidebar.button("🚀 تأكيد الطلب النهائي"):
    if total > 0:
        st.balloons()
        # رد الـ AI المميز
        if total >= 18:
            st.info("🤖 AI: اختيار الملوك! السدر الملكي بدو ناس أكيلة، رح نوصي فيك بالثومية والبطاطا زيادة!")
        elif "علبة ماتريكس" in [i['name'] for i in st.session_state.cart]:
            st.info("🤖 AI: ماتريكس؟ اختيار زقرت! السهرة كملت هيك.")
        else:
            st.info("🤖 AI: صحتين وعافية! طلبك صار عند المعلم وقيد التجهيز.")
    else:
        st.sidebar.error("السلة فاضية يا حبيب!")
