import streamlit as st

# 1. إعدادات الصفحة والديزاين (Premium Dark Style)
st.set_page_config(page_title="شاورما ع الصاج | القمة", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(45, 0, 0, 0.85)), 
                    url('https://images.unsplash.com/photo-1555396273-367ea4eb4db5?q=80&w=1500');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .main-title {
        font-size: 55px;
        text-align: center;
        color: #ff4b4b;
        text-shadow: 3px 3px 12px #000;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .menu-card {
        background: rgba(15, 15, 15, 0.95);
        border: 1px solid #ff4b4b;
        border-radius: 15px;
        padding: 0px;
        text-align: center;
        margin-bottom: 20px;
        overflow: hidden;
        transition: 0.3s ease-in-out;
    }
    .menu-card:hover { transform: translateY(-8px); border-color: white; }
    .item-img { width: 100%; height: 190px; object-fit: cover; border-bottom: 2px solid #ff4b4b; }
    .card-body { padding: 12px; }
    .price-tag { color: #ff4b4b; font-size: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. التواصل الاجتماعي
st.markdown("""
    <div style='display: flex; justify-content: center; gap: 15px; margin-bottom: 25px;'>
        <a href='#' style='background: linear-gradient(45deg, #f09433, #dc2743); padding: 8px 20px; border-radius: 50px; color: white; text-decoration: none; font-size: 14px;'>📸 Instagram</a>
        <a href='#' style='background: #25d366; padding: 8px 20px; border-radius: 50px; color: white; text-decoration: none; font-size: 14px;'>💬 WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🌯 مطعم شاورما ع الصاج</h1>", unsafe_allow_html=True)

# 3. الرد الآلي "اللبق"
if "chat" not in st.session_state: st.session_state.chat = []
with st.expander("🤖 المساعد الذكي - كيف يمكننا خدمتك؟"):
    user_in = st.text_input("تفضل بإخبارنا بما تشتهيه:")
    if user_in:
        msg = user_in.lower()
        if "برغر" in msg: res = "قسم البرغر عندنا يجمع بين اللحم البلدي والدجاج المقرمش، أنصحك بـ 'رويال دبل'!"
        elif "زنجر" in msg: res = "الزنجر عندنا يحضر بخلطة حارة خاصة، يقدم طازجاً في خبز البريوش أو الصاج."
        elif "دايت" in msg: res = "صحتك بتهمنا! بنقدر نضبطلك أي ساندويش بدون مايونيز ومع خبز قمح."
        else: res = "على الرحب والسعة! نحن هنا لنضمن لك تجربة طعام لا تُنسى."
        st.info(f"🤖: {res}")

# 4. المنيو العملاق (دقة في الأصناف)
tabs = st.tabs(["🔥 الشاورما", "🥩 برغر اللحم", "🍗 برغر الدجاج", "🥪 الساندويشات", "🍗 البروستد", "🥤 المشروبات"])

menu_data = {
    "🔥 الشاورما": [
        ("سوبر صاج كلاسيك", 3.50, "https://images.unsplash.com/photo-1662145031215-9898246d60a5?w=400", "ساندويش ضخم مقطع، بطاطا، ثومية، مخلل بيتي"),
        ("وجبة شاورما دبل", 5.50, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=400", "2 ساندويش صاج، بوكس مقبلات عائلي، مشروب غازي"),
        ("سدر العيلة الملكي", 18.00, "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400", "48 قطعة، مثومة حارة وعادية، لتر كولا، مخللات")
    ],
    "🥩 برغر اللحم": [
        ("رويال برغر بلدي", 4.25, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400", "150غم لحم طازج، جبنة شيدر، بصل مكرمل، صوص المدخن"),
        ("دبل تايتن برغر", 6.00, "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=400", "300غم لحم (قطعتين)، جبنة مضاعفة، خس هولندي، صوص سبيشال"),
        ("مشروم برغر", 4.75, "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400", "لحم مشوي على اللهب، صوص فطر طازج، جبنة سويسرية")
    ],
    "🍗 برغر الدجاج": [
        ("كريسبي تشيكن برغر", 3.50, "https://images.unsplash.com/photo-1610614819513-58e34989848b?w=400", "صدر دجاج مقرمش، صوص المايونيز الحار، جبنة، خس"),
        ("زنجر سوبريم", 3.75, "https://images.unsplash.com/photo-1623653387945-2fd25214f8fc?w=400", "دجاج حار جداً، قطعة تركي مدخن، جبنة، صوص الزنجر"),
        ("وجبة برغر دجاج دبل", 5.25, "https://images.unsplash.com/photo-1525463032172-35804044f51e?w=400", "2 برغر دجاج، بطاطا كريسبي، مشروب غازي")
    ],
    "🥪 الساندويشات": [
        ("ساندويش زنجر صاج", 2.25, "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=400", "قطع الزنجر المقرمشة في خبز الصاج مع الثومية والجبنة"),
        ("ساندويش شاورما فرنسي", 2.00, "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=400", "شاورما دجاج في خبز فرنسي محمص، ثومية، بطاطا بالداخل"),
        ("تورتيلا تشيكن", 2.50, "https://images.unsplash.com/photo-1528605105345-5344ea20e269?w=400", "دجاج مشوي، صوص المكسيك، ذرة، جبنة في خبز التورتيلا")
    ],
    "🍗 البروستد": [
        ("وجبة البركة (4 قطع)", 4.75, "https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=400", "دجاج بروستد ذهبي، بطاطا، ثومية المعلم، خبز طازج"),
        ("سطل العز (12 قطعة)", 13.50, "https://images.unsplash.com/photo-1562967914-608f82629710?w=400", "وجبة عائلية ضخمة مع بطاطا عائلية ولتر كولا")
    ],
    "🥤 المشروبات": [
        ("ماتريكس كولا", 0.50, "https://images.unsplash.com/photo-1527960471264-932f39eb5846?w=400", "المشروب الغازي المنعش والمبرد"),
        ("عصير تقال طبيعي", 1.50, "https://images.unsplash.com/photo-1600271886382-d51b13299c33?w=400", "برتقال معصور فريش 100% بدون سكر مضاف")
    ]
}

# عرض الأصناف
for i, cat in enumerate(menu_data.keys()):
    with tabs[i]:
        cols = st.columns(3)
        for j, (name, price, img, desc) in enumerate(menu_data[cat]):
            with cols[j % 3]:
                st.markdown(f"""
                    <div class='menu-card'>
                        <img src='{img}' class='item-img'>
                        <div class='card-body'>
                            <h3 style='color:white; margin-bottom:5px;'>{name}</h3>
                            <p style='color:#ccc; font-size:13px; height:40px;'>{desc}</p>
                            <p class='price-tag'>{price:.2f} JOD</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"أضف {name}", key=name+str(i)):
                    st.toast(f"✅ تمت إضافة {name}")

# 5. الفوتر (ارقام الشكاوي واللوكيشن)
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📞 للتواصل المباشر")
    st.write("الفرع الرئيسي: 079-1111111")
    st.write("الإدارة والشكاوي: 077-2222222")
with col2:
    st.markdown("### 📍 فروعنا")
    st.write("عمان: شارع الجوعانين | إربد: دوار السعادة")
    st.write("الزرقاء: دخلة الشاورما الفخمة")
with col3:
    st.markdown("### 🏅 لماذا نحن؟")
    st.write("نستخدم اللحوم الطازجة يومياً والخضروات المنتقاة بعناية لضمان أعلى مستويات الجودة.")
