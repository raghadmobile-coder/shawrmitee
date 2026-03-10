import streamlit as st

# 1. إعدادات الصفحة والديزاين (Premium Dark Style)
st.set_page_config(page_title="شاورما ع الصاج | هيبة الملكي", page_icon="🌯", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(55, 0, 0, 0.85)), 
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
    }
    .menu-card {
        background: rgba(15, 15, 15, 0.98);
        border: 1px solid #ff4b4b;
        border-radius: 20px;
        padding: 0px;
        text-align: center;
        margin-bottom: 25px;
        overflow: hidden;
        transition: 0.3s ease-in-out;
    }
    .menu-card:hover { transform: translateY(-8px); border-color: white; }
    
    /* تنسيق صورة السدر الملكي العملاق (Zoom Out) */
    .royal-img {
        width: 100%;
        height: 550px; /* كبرنا الارتفاع عشان يبان السدر كامل */
        object-fit: contain; /* أهم تعديل: ابعاد الكاميرا واظهار السدر بالكامل */
        background: #000; /* خلفية سوداء عشان الصورة ما تقطع */
        border-bottom: 4px solid #ff4b4b;
    }
    
    .item-img { width: 100%; height: 230px; object-fit: cover; border-bottom: 3px solid #ff4b4b; }
    .card-body { padding: 18px; }
    .price-tag { color: #ff4b4b; font-size: 24px; font-weight: bold; }
    .details-text { color: #bbb; font-size: 15px; line-height: 1.6; height: 50px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر والترحيب
st.markdown("<h1 class='main-title'>🌯 شاورما ع الصاج - المنيو الملكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ccc; font-size:18px;'>كل لقمة عنا محبوكة بحب ودقة.. تفضل وشوف الهيبة</p>", unsafe_allow_html=True)

# 3. المنيو الملكي (صور مرئية بالكامل وتفاصيل دقيقة)
tabs = st.tabs(["👑 السدر الملكي العملاق", "🌯 الشاورما العربي", "🥩 برغر الأنغوس البلدي", "🍗 البروستد كريسبي", "🥤 المشروبات"])

menu_data = {
    "👑 السدر الملكي العملاق": [
        ("سدر العيلة الملكي VIP (العملاق)", 18.50, "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=1200", 
         "سدر معدني عملاق يحتوي على 60 قطعة شاورما دجاج (صافي 100%)، مصفوفة بدقة، مع 4 علب ثومية (عادي، حار، مدخن، كاري)، بطاطا عائلية كريسبي، مخللات بيتية، لتر ونصف كولا عائلي.")
    ],
    "🌯 الشاورما العربي": [
        ("وجبة سوبر صاج (150غم)", 3.75, "https://images.unsplash.com/photo-1662145031215-9898246d60a5?w=500", 
         "ساندويش شاورما عربي (150غم دجاج صفي) في خبز صاج، مقطع لـ 6 قطع، يقدم مع بطاطا، ثومية، ومخلل خيار بيتي."),
        ("وجبة دبل عربي (2 برغر)", 5.75, "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=500", 
         "2 ساندويش صاج عربي ضخم، علبة ثومية كبيرة، بوكس بطاطا مدعم، ومشروب غازي منعش.")
    ],
    "🥩 برغر الأنغوس البلدي": [
        ("أنغوس تشيز برغر البلدي", 4.75, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500", 
         "180غم لحم أنغوس بلدي طازج يومياً، جبنة شيدر أصلية، بصل مكرمل، صوص رويال المدخن، خبز بريوش."),
        ("برغر لحم تايتن (300غم دبل)", 6.50, "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500", 
         "قطعتين لحم (300غم مجموع)، طبقتين جبنة شيدر، خس لولو روسو هولندي، صوص سبيشال، وودجز.")
    ],
    "🍗 البروستد كريسبي": [
        ("وجبة البروستد (4 قطع)", 4.95, "https://images.unsplash.com/photo-1626645738196-c2a7c8d08f58?w=500", 
         "دجاجة (صدر، جناح، فخذ، دبوس) متبلة بـ 11 بهار، بطاطا مقلية، علبة ثومية، خبز مخبوز فوراً."),
        ("سطل البروستد (12 قطعة)", 13.75, "https://images.unsplash.com/photo-1562967914-608f82629710?w=500", 
         "12 قطعة دجاج كريسبي مقرمش، بطاطا عائلية ضخمة، 3 علب ثومية، لتر كولا، مخلل.")
    ],
    "🥤 المشروبات": [
        ("ماتريكس بلو (Matrix)", 0.60, "https://images.unsplash.com/photo-1527960471264-932f39eb5846?w=500", 
         "المشروب الغازي الرسمي المنعش والمبرد."),
        ("عصير برتقال فريش (طبيعي)", 1.75, "https://images.unsplash.com/photo-1600271886382-d51b13299c33?w=500", 
         "عصير برتقال طبيعي 100% معصور يدوياً عند الطلب.")
    ]
}

# 4. عرض الأصناف بنظام الكروت المرنة
for i, cat in enumerate(menu_data.keys()):
    with tabs[i]:
        if cat == "👑 السدر الملكي العملاق": # عرض السدر كرت ضخم Full Screen لهيبته
            item = menu_data[cat][0]
            st.markdown(f"""
                <div class='menu-card' style='max-width: 1000px; margin: 0 auto 30px auto;'>
                    <img src='{item[2]}' class='royal-img'>
                    <div class='card-body'>
                        <h2 style='color:#ff4b4b; font-size:35px;'>{item[0]}</h2>
                        <p style='font-size:18px; color:#ddd; line-height:1.8; text-align:right;'>{item[3]}</p>
                        <p class='price-tag' style='font-size:35px;'>{item[1]:.2f} JOD</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("اطلب السدر الملكي العملاق الآن", key="king_btn"): st.toast("✅ تم إضافة السدر الملكي للسلة!")
        else:
            cols = st.columns(2)
            for j, (name, price, img, desc) in enumerate(menu_data[cat]):
                with cols[j % len(cols)]:
                    st.markdown(f"""
                        <div class='menu-card'>
                            <img src='{img}' class='item-img'>
                            <div class='card-body'>
                                <h3>{name}</h3>
                                <p class='details-text'>{desc}</p>
                                <p class='price-tag'>{price:.2f} JOD</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"أضف {name}", key=name+str(i)): st.toast(f"✅ تمت إضافة {name}")

# 5. الفوتر الاحترافي (ارقام الشكاوي واللوكيشن)
st.markdown("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.write("### 📞 للتواصل والطلب")
    st.write("الرقم الموحد: 079-1111111")
    st.write("واتساب الإدارة والشكاوي: 077-9999999")
with c2:
    st.write("### 📍 خارطة الفروع")
    st.write("عمان: الدوار السابع | إربد: شارع الجامعة")
    st.write("الزرقاء: دخلة الشاورما الفخمة")
with c3:
    st.write("### 🕒 ساعات العمل")
    st.write("يومياً من الساعة 12:00 ظهراً")
    st.write("حتى الساعة 4:00 فجراً")
