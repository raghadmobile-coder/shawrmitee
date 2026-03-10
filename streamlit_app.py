import streamlit as st

# 1. إعدادات الصفحة والديزاين الاحترافي
st.set_page_config(page_title="شاورما ع الصاج - الملكي", page_icon="🌯", layout="wide")

# CSS للتصميم، الخلفية، وحركة الأزرار
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(40, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=1500');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .main-title {
        font-size: 60px;
        text-align: center;
        color: #ff4b4b;
        text-shadow: 3px 3px 10px #000;
        font-weight: bold;
    }
    .social-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    .social-link {
        padding: 10px 20px;
        border-radius: 30px;
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .insta-bg { background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); }
    .whats-bg { background: #25d366; }
    .menu-card {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #ff4b4b;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .item-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. حسابات التواصل الاجتماعي
st.markdown("""
    <div class='social-container'>
        <a class='social-link insta-bg' href='https://instagram.com/shawrmitee'>📸 انستغرام</a>
        <a class='social-link whats-bg' href='https://wa.me/962700000000'>💬 واتساب</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🌯 شاورما ع الصاج - الملكي</h1>", unsafe_allow_html=True)

# 3. الرد الآلي الذكي (Chatbot)
st.subheader("🤖 مساعدك الذكي")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_chat = st.text_input("احكي معي عن مودك أو اسألني شو أطلب:")
if user_chat:
    reply = "نورتنا! "
    msg = user_chat.lower()
    if "جوعان" in msg: reply = "ولا يهمك، السدر الملكي هو اللي رح يحل المشكلة هسا!"
    elif "نفسيتي" in msg or "تعبان" in msg: reply = "سلامة قلبك، جرب وجبة الأطفال فيها لعبة بتفرحك، أو ساندويش صاج يعدل المود."
    elif "نصيحة" in msg: reply = "بنصحك بالبروستد عنا، قرمشة عالمية!"
    else: reply = "والله حكيك ذهب! بس شكلك بدك توصي، شو حابب تاكل؟"
    
    st.session_state.chat_history.append((user_chat, reply))

for user_m, bot_m in st.session_state.chat_history[-2:]:
    st.write(f"👤: {user_m}")
    st.info(f"🤖: {bot_m}")

# 4. المنيو بالصور والتفاصيل
st.markdown("---")
tabs = st.tabs(["🔥 شاورما", "🍔 برغر", "🍗 بروستد", "🍼 وجبات أطفال", "🥤 مشروبات"])

# داتا المنيو
menu_items = {
    "شاورما": [
        ("صاج سوبر", 3.50, "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=400", "شاورما دبل مع بطاطا ومقبلات"),
        ("سدر العيلة", 18.00, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400", "48 قطعة شاورما تكفي كل العيلة")
    ],
    "برغر": [
        ("برغر أنغوس", 4.50, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400", "لحم طازج 150غم مع صوص سبيشال")
    ],
    "بروستد": [
        ("وجبة 4 قطع", 4.75, "https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=400", "دجاج مقرمش بخلطة المعلم السرية")
    ],
    "وجبات أطفال": [
        ("بوكس السنافر", 2.50, "https://images.unsplash.com/photo-1558930761-0b9183f12df1?w=400", "قطع دجاج، بطاطا، عصير ولعبة")
    ],
    "مشروبات": [
        ("ماتريكس", 0.50, "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400", "مشروب منعش"),
        ("عصير برتقال", 1.50, "https://images.unsplash.com/photo-1600271886382-d51b13299c33?w=400", "برتقال طبيعي معصور فريش")
    ]
}

for i, cat in enumerate(menu_items.keys()):
    with tabs[i]:
        cols = st.columns(len(menu_items[cat]))
        for j, (name, price, img, desc) in enumerate(menu_items[cat]):
            with cols[j]:
                st.markdown(f"""
                    <div class='menu-card'>
                        <img src='{img}' class='item-img'>
                        <h3>{name}</h3>
                        <p>{desc}</p>
                        <h4 style='color:#ff4b4b'>{price} JOD</h4>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name):
                    st.toast(f"تم إضافة {name}")

# 5. الفوتر (الموقع والشكاوي)
st.markdown("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.write("📍 **الأفرع:** عمان - السابعة | إربد - الجامعة")
with c2:
    st.write("☎️ **الطلبات:** 0790000000")
with c3:
    st.write("⚠️ **الشكاوي:** 0770000000")
