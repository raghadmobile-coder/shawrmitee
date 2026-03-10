import streamlit as st
import time

# 1. إعدادات الصفحة والديزاين (الخلفية بالصور والحركة)
st.set_page_config(page_title="شاورما ع الصاج - VIP", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    /* خلفية بصور الوجبات مع تدرج أسود شفاف */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(60, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1555939594-58d7cb561ad1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .main-title {
        font-family: 'Cairo', sans-serif;
        font-size: 65px;
        text-align: center;
        color: #ff4b4b;
        text-shadow: 4px 4px 15px #000;
        margin-top: -50px;
    }
    .social-btns {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .social-icon {
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .insta { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
    .whats { background: #25d366; }
    .menu-card {
        background: rgba(0, 0, 0, 0.7);
        padding: 15px;
        border-radius: 20px;
        border: 1px solid #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. روابط التواصل الاجتماعي (أعلى الصفحة)
st.markdown("""
    <div class="social-btns">
        <a href="https://instagram.com/YourAccount" class="social-icon insta">📸 Instagram</a>
        <a href="https://wa.me/962700000000" class="social-icon whats">💬 WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🌯 شاورما ع الصاج - الملكي</h1>", unsafe_allow_html=True)

# 3. الرد الآلي "الأخذ والعطاء" (Advanced Chatbot)
st.subheader("🤖 مساعدك الذكي (احكي معه عن أي شيء!)")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("اكتب رسالتك هنا...")

if user_input:
    # منطق الرد الذكي
    bot_reply = ""
    ui = user_input.lower()
    
    if "مرحبا" in ui or "سلام" in ui:
        bot_reply = "هلا وغلا بنور العين! كيف المود اليوم؟ جوعان ولا جاي تدردش؟"
    elif "جوعان" in ui or "أكل" in ui:
        bot_reply = "والله وأنا كمان! بس نصيحة من أخ لأخوه: جرب سدر العيلة الملكي، بخليك تنسى همومك."
    elif "شو بتنصحني" in ui:
        bot_reply = "إذا بتحب القرمشة، خذلك بروستد. إذا بدك شي كلاسيك، الشاورما صاج ما عليها كلام. شو رايك؟"
    elif "نفسيتي" in ui or "تعبان" in ui:
        bot_reply = "سلامة قلبك! الأكل الطيب هو أحسن علاج. اطلب علبة ماتريكس مع وجبة أطفال وانسى العالم."
    else:
        bot_reply = f"والله إنك ذوق! ' {user_input} ' حكيك درر.. بس شكلك ناوي تطلب، شو بدك نبلش؟"

    st.session_state.chat_history.append({"user": user_input, "bot": bot_reply})

# عرض المحادثة
for chat in st.session_state.chat_history[-3:]: # عرض آخر 3 رسائل
    st.info(f"👤 أنت: {chat['user']}")
    st.success(f"🤖 المساعد: {chat['bot']}")

# 4. المنيو الضخم (تفاصيل دقيقة)
st.markdown("---")
tabs = st.tabs(["🔥 الشاورما", "🍔 البرغر", "🍗 البروستد", "🍼 وجبات الأطفال", "🥤 المشروبات"])

# بيانات المنيو مع التفاصيل
menu_data = {
    "الشاورما": {
        "صاج عادي (100غم)": [1.75, "خبز صاج مقرمش، ثومية أصلية، مخلل بيتي"],
        "وجبة دبل (24 قطعة)": [4.50, "شاورما مقطعة، بطاطا عريضة، ثومية، مخلل، كولا"],
        "سدر العيلة (48 قطعة)": [18.00, "سدر ضخم للعزائم، 4 أنواع مقبلات، لتر كولا"]
    },
    "البرغر": {
        "برغر لحم أنغوس": [4.00, "150غم لحم طازج، جبنة شيدر، بصل مكرمل، صوص خاص"],
        "زنجر سوبريم حار": [3.25, "صدر دجاج مقرمش، صوص حار، سلامي وجبنة"]
    },
    "البروستد": {
        "وجبة 4 قطع": [4.75, "دجاج متبل بـ 11 بهار، بطاطا، ثومية، خبز طازج"],
        "سطل عائلي (12 قطعة)": [12.50, "سطل كامل للعيلة مع كل الإضافات والبطاطا"]
    },
    "وجبات الأطفال": {
        "بوكس السنافر": [2.50, "3 قطع ناجتس، بطاطا، عصير طبيعي، لعبة مفاجأة"],
        "وجبة ميني شاورما": [2.25, "ساندويش صغير، بطاطا، عصير برتقال"]
    },
    "المشروبات": {
        "علبة ماتريكس": [0.50, "المشروب الغازي المنعش"],
        "عصير تقال (طبيعي)": [1.50, "برتقال معصور فريش 100%"]
    }
}

for i, (cat_name, cat_content) in enumerate(menu_data.items()):
    with tabs[i]:
        cols = st.columns(3)
        for j, (item, details) in enumerate(cat_content.items()):
            with cols[j % 3]:
                st.markdown(f"""
                    <div class='menu-card'>
                        <h3>{item}</h3>
                        <p style='color: #bbb;'>{details[1]}</p>
                        <h4 style='color: #ff4b4b;'>{details[0]} JOD</h4>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"إضافة {item}", key=f"{item}_{i}"):
                    st.toast(f"تم إضافة {item} لعيونك!")

# 5. الفوتر (الموقع والشكاوي)
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("### 📍 لوكيشن الأفرع")
    st.write("- عمان: الدوار السابع - خلف كارفور")
    st.write("- إربد: شارع الجامعة - بجانب المكتبة")
with col2:
    st.write("### 📞 للتواصل")
    st.write("الإدارة: 06-000000")
    st.write("الشكاوي: 079-000000")
with col3:
    st.write("### 🌟 تابعونا")
    st.write("نحن نهتم برأيكم جداً، شاركونا تجربتكم على السوشيال ميديا.")
