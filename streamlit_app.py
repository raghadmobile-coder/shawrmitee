import streamlit as st
import requests

# --- إعدادات الربط النهائية (جاهزة للعمل) ---
TELEGRAM_TOKEN = "8766182179:AAfFCZKc5qJ7xgvisfkEhARahtyj-5guJJo"
TELEGRAM_CHAT_ID = "7629461559"

def send_telegram_notification(order_details):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": order_details,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

# 1. إعدادات الصفحة والتنسيق
st.set_page_config(
    page_title="الضيعة | مطعم شاورما وبروستد",
    page_icon="🍖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total' not in st.session_state: st.session_state.total = 0.0

# --- CSS (تصميم حديث - أزرق وأبيض) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    .stApp { 
        background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
        color: #262626;
        font-family: 'Cairo', sans-serif;
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        padding: 60px 40px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 10px 40px rgba(0, 149, 246, 0.2);
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .hero-subtitle {
        font-size: 20px;
        font-weight: 400;
        opacity: 0.95;
        margin-bottom: 20px;
    }
    
    /* Navigation */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }
    
    .nav-btn {
        padding: 12px 28px;
        border-radius: 25px;
        border: none;
        font-size: 16px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        background: white;
        color: #0095F6;
        box-shadow: 0 4px 15px rgba(0, 149, 246, 0.1);
    }
    
    .nav-btn:hover {
        background: #0095F6;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 149, 246, 0.3);
    }
    
    .nav-btn.active {
        background: #0095F6;
        color: white;
    }
    
    /* Menu Items */
    .menu-item-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #E8ECEF;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .menu-item-card:hover {
        box-shadow: 0 8px 25px rgba(0, 149, 246, 0.15);
        transform: translateY(-4px);
        border-color: #0095F6;
    }
    
    .item-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    
    .item-name {
        font-size: 20px;
        font-weight: 700;
        color: #0077B6;
        margin-bottom: 8px;
        text-align: right;
    }
    
    .item-desc {
        font-size: 14px;
        color: #65676B;
        margin-bottom: 10px;
        text-align: right;
        line-height: 1.5;
    }
    
    .item-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #E8ECEF;
    }
    
    .item-price {
        font-size: 24px;
        font-weight: 900;
        color: #0095F6;
    }
    
    .nutrition-tag {
        color: #65676B;
        font-size: 13px;
        background: #F0F0F0;
        padding: 6px 12px;
        border-radius: 20px;
        text-align: center;
    }
    
    /* Categories */
    .category-section {
        margin-bottom: 40px;
    }
    
    .category-title {
        font-size: 32px;
        font-weight: 900;
        color: #0077B6;
        margin-bottom: 30px;
        padding-bottom: 15px;
        border-bottom: 3px solid #0095F6;
        text-align: right;
    }
    
    .category-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 20px;
    }
    
    /* Cart */
    .cart-container {
        background: white;
        border-radius: 16px;
        padding: 25px;
        border: 2px solid #0095F6;
        box-shadow: 0 4px 15px rgba(0, 149, 246, 0.1);
        position: sticky;
        top: 20px;
    }
    
    .cart-header {
        font-size: 24px;
        font-weight: 900;
        color: #0095F6;
        text-align: center;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid #E8ECEF;
    }
    
    .cart-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #F0F0F0;
        font-size: 14px;
    }
    
    .cart-item:last-child {
        border-bottom: none;
    }
    
    .cart-total {
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
    }
    
    .cart-empty {
        text-align: center;
        color: #65676B;
        padding: 20px;
        font-size: 16px;
    }
    
    /* Buttons */
    .btn-add {
        background: #0095F6;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .btn-add:hover {
        background: #0077B6;
        transform: scale(1.02);
    }
    
    .btn-delete {
        background: #FF6B6B;
        color: white;
        border: none;
        padding: 6px 12px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 700;
        font-size: 12px;
    }
    
    .btn-delete:hover {
        background: #FF5252;
    }
    
    .btn-submit {
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 8px;
        font-weight: 900;
        font-size: 16px;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .btn-submit:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 149, 246, 0.3);
    }
    
    /* Info Sections */
    .info-section {
        background: white;
        border-radius: 16px;
        padding: 40px;
        margin-bottom: 30px;
        border: 1px solid #E8ECEF;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .section-title {
        font-size: 28px;
        font-weight: 900;
        color: #0077B6;
        margin-bottom: 25px;
        text-align: right;
    }
    
    /* Testimonials */
    .testimonial-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        border: 1px solid #E8ECEF;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .testimonial-text {
        color: #262626;
        font-size: 16px;
        margin-bottom: 10px;
        text-align: right;
        line-height: 1.6;
    }
    
    .testimonial-author {
        color: #0095F6;
        font-weight: 700;
        text-align: right;
        font-size: 14px;
    }
    
    .testimonial-rating {
        color: #FFC107;
        font-size: 14px;
        margin-bottom: 10px;
    }
    
    /* Contact Section */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    
    .contact-item {
        background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%);
        color: white;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
    }
    
    .contact-label {
        font-size: 14px;
        opacity: 0.9;
        margin-bottom: 10px;
    }
    
    .contact-value {
        font-size: 20px;
        font-weight: 900;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title { font-size: 32px; }
        .hero-subtitle { font-size: 16px; }
        .category-grid { grid-template-columns: 1fr; }
        .category-title { font-size: 24px; }
        .cart-container { position: relative; top: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# --- بيانات المنتجات مع الصور ---
items_db = {
    "🔥 العروض الملكية": [
        {
            "name": "أوفر الصحاب (2 سوبر)",
            "price": 4.95,
            "desc": "2 ساندويش سوبر + بطاطا + كولا",
            "nut": "65g Protein | 1200 Cal",
            "image": "https://images.unsplash.com/photo-1552858905-b0f63dc27615?w=400&h=300&fit=crop"
        },
        {
            "name": "عرض الـ 3 وجبات",
            "price": 6.50,
            "desc": "3 وجبات عربي عادي + سرفيس كامل",
            "nut": "90g Protein | 1800 Cal",
            "image": "https://images.unsplash.com/photo-1609501676725-7186f017a4b5?w=400&h=300&fit=crop"
        },
        {
            "name": "وجبة التوفير اليومية",
            "price": 1.95,
            "desc": "ساندويش عادي + بطاطا + كولا علبة",
            "nut": "25g Protein | 600 Cal",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400&h=300&fit=crop"
        }
    ],
    "🌯 شاورما (أحجام)": [
        {
            "name": "شاورما عادي",
            "price": 1.25,
            "desc": "خبز صاج، ثومية، مخلل",
            "nut": "22g Protein | 450 Cal",
            "image": "https://images.unsplash.com/photo-1599599810694-b5ac4dd94b73?w=400&h=300&fit=crop"
        },
        {
            "name": "شاورما سوبر",
            "price": 1.95,
            "desc": "دجاج إضافي وحجم أكبر",
            "nut": "32g Protein | 620 Cal",
            "image": "https://images.unsplash.com/photo-1552858905-b0f63dc27615?w=400&h=300&fit=crop"
        },
        {
            "name": "شاورما دبل",
            "price": 2.75,
            "desc": "دبل دجاج لعشاق الشاورما",
            "nut": "45g Protein | 800 Cal",
            "image": "https://images.unsplash.com/photo-1585614894260-fdb563f9f6d6?w=400&h=300&fit=crop"
        },
        {
            "name": "شاورما تربل (العملاق)",
            "price": 3.50,
            "desc": "3 أضعاف الدجاج",
            "nut": "60g Protein | 950 Cal",
            "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop"
        }
    ],
    "🍔 برغرات الساحل": [
        {
            "name": "كلاسيك برغر دجاج",
            "price": 2.50,
            "desc": "صدر دجاج، جبنة، خس، صوص",
            "nut": "28g Protein | 550 Cal",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400&h=300&fit=crop"
        },
        {
            "name": "كلاسيك برغر لحم",
            "price": 2.95,
            "desc": "لحم بقري، جبنة، مخلل، صوص",
            "nut": "26g Protein | 600 Cal",
            "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop"
        },
        {
            "name": "وجبة برغر دبل",
            "price": 3.95,
            "desc": "2 شريحة جبنة + بطاطا + كولا",
            "nut": "45g Protein | 850 Cal",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400&h=300&fit=crop"
        }
    ],
    "👨‍👩‍👧‍👦 وجبات العيلة": [
        {
            "name": "سدر العيلة الملكي",
            "price": 14.95,
            "desc": "64 قطعة + بطاطا دبل + كولا عائلي",
            "nut": "190g Protein | 4500 Cal",
            "image": "https://images.unsplash.com/photo-1609501676725-7186f017a4b5?w=400&h=300&fit=crop"
        },
        {
            "name": "سدر عيلة وسط",
            "price": 9.95,
            "desc": "32 قطعة + بطاطا + كولا",
            "nut": "95g Protein | 2200 Cal",
            "image": "https://images.unsplash.com/photo-1585614894260-fdb563f9f6d6?w=400&h=300&fit=crop"
        }
    ],
    "🍗 بروستد مقرمش": [
        {
            "name": "بروستد 4 قطع",
            "price": 3.25,
            "desc": "مع بطاطا وثومية وكولا",
            "nut": "35g Protein | 800 Cal",
            "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc45a?w=400&h=300&fit=crop"
        },
        {
            "name": "وليمة بروستد 21 قطعة",
            "price": 14.50,
            "desc": "21 قطعة + بطاطا دبل + كولا ضخم",
            "nut": "190g Protein | 4200 Cal",
            "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc45a?w=400&h=300&fit=crop"
        }
    ],
    "🍟 قائمة الإضافات": [
        {
            "name": "علبة بطاطا - كبير",
            "price": 1.50,
            "desc": "حجم عائلي مقرمش",
            "nut": "650 Cal",
            "image": "https://images.unsplash.com/photo-1585238341710-4aca6d51e4c4?w=400&h=300&fit=crop"
        },
        {
            "name": "علبة مثومة - كبير",
            "price": 0.75,
            "desc": "ثومية المحل الأصلية",
            "nut": "150 Cal",
            "image": "https://images.unsplash.com/photo-1599599810727-ab7cead31006?w=400&h=300&fit=crop"
        },
        {
            "name": "علبة جبنة شيدر",
            "price": 0.50,
            "desc": "جبنة سائلة ساخنة",
            "nut": "200 Cal",
            "image": "https://images.unsplash.com/photo-1599599810694-b5ac4dd94b73?w=400&h=300&fit=crop"
        }
    ],
    "🥤 مشروبات": [
        {
            "name": "كولا بارد",
            "price": 0.45,
            "desc": "مشروب منعش بارد",
            "nut": "140 Cal",
            "image": "https://images.unsplash.com/photo-1554866585-acbb73ce3362?w=400&h=300&fit=crop"
        },
        {
            "name": "عصير برتقال طازج",
            "price": 0.95,
            "desc": "عصير برتقال طازج يومي",
            "nut": "110 Cal",
            "image": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400&h=300&fit=crop"
        }
    ]
}

# --- التقييمات ---
testimonials = [
    {"name": "محمود الحاج", "rating": "⭐⭐⭐⭐⭐", "text": "أفضل شاورما تذوقتها! الطعم واللحم روعة والسعر ممتاز"},
    {"name": "فاطمة علي", "rating": "⭐⭐⭐⭐⭐", "text": "الجودة عالية جداً والتوصيل سريع. من أفضل المطاعم بالعمّ"},
    {"name": "أحمد سالم", "rating": "⭐⭐⭐⭐⭐", "text": "الفريق محترف وودود جداً. الطعام جاهز بسرعة وطازج"},
    {"name": "سارة محمد", "rating": "⭐⭐⭐⭐⭐", "text": "تجربة رائعة من البداية للنهاية. أنصح الكل بزيارة الضيعة"},
]

# --- Navigation Bar ---
st.markdown("""
    <style>
    .nav-wrapper { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; flex-wrap: wrap; }
    </style>
""", unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    if st.button("🏠 الرئيسية", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()

with nav_col2:
    if st.button("📋 المنيو", use_container_width=True):
        st.session_state.page = 'menu'
        st.rerun()

with nav_col3:
    if st.button("📧 تواصل معنا", use_container_width=True):
        st.session_state.page = 'contact'
        st.rerun()

st.divider()

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # Hero Section
    st.markdown("""
        <div class='hero-container'>
            <div class='hero-title'>🍖 مطعم الضيعة 🍖</div>
            <div class='hero-subtitle'>طعم أصيل | جودة عالية | أسعار منافسة</div>
            <div class='hero-subtitle' style='font-size: 18px; opacity: 0.9;'>
                🏪 الفروع | 📞 079-0000000 | ⏰ من 10 صباح لـ 2 صباح
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Info Section
    st.markdown("""
        <div class='info-section'>
            <div class='section-title'>🌟 عن مطعم الضيعة</div>
            <p style='font-size: 18px; line-height: 1.8; color: #262626; text-align: right;'>
                في مطعم الضيعة، نقدم لك أفضل الشاورما والبروستد والبرغرات بجودة عالية وأسعار منافسة. 
                كل وجبة تُحضّر بحب واهتمام باستخدام أطيب المكونات. فريقنا مدرب على أعلى مستويات الخدمة 
                لنضمن لك تجربة طعام لا تنسى.
            </p>
            <p style='font-size: 18px; line-height: 1.8; color: #262626; text-align: right; margin-top: 20px;'>
                ⏰ مفتوح: 10 صباح - 2 صباح | 📍 فروع متعددة | 🚚 توصيل سريع
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Menu Preview
    st.markdown("""
        <div class='info-section'>
            <div class='section-title'>📋 أقسام القائمة</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;'>
                <div style='font-size: 40px; margin-bottom: 10px;'>🌯</div>
                <div style='font-size: 20px; font-weight: 900;'>شاورما</div>
                <div style='font-size: 14px; opacity: 0.9; margin-top: 10px;'>أحجام مختلفة</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;'>
                <div style='font-size: 40px; margin-bottom: 10px;'>🍔</div>
                <div style='font-size: 20px; font-weight: 900;'>برغرات</div>
                <div style='font-size: 14px; opacity: 0.9; margin-top: 10px;'>لحم وبدجاج</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #0095F6 0%, #0077B6 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;'>
                <div style='font-size: 40px; margin-bottom: 10px;'>🍗</div>
                <div style='font-size: 20px; font-weight: 900;'>بروستد</div>
                <div style='font-size: 14px; opacity: 0.9; margin-top: 10px;'>مقرمش وطازج</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Testimonials
    st.markdown("""
        <div class='info-section'>
            <div class='section-title'>⭐ آراء الزبائن</div>
        </div>
    """, unsafe_allow_html=True)
    
    for testimonial in testimonials:
        st.markdown(f"""
            <div class='testimonial-card'>
                <div class='testimonial-rating'>{testimonial['rating']}</div>
                <div class='testimonial-text'>"{testimonial['text']}"</div>
                <div class='testimonial-author'>— {testimonial['name']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact
    st.markdown("""
        <div class='info-section'>
            <div class='section-title'>📞 تواصل معنا</div>
            <div class='contact-grid'>
                <div class='contact-item'>
                    <div class='contact-label'>📱 الهاتف</div>
                    <div class='contact-value'>079-0000000</div>
                </div>
                <div class='contact-item'>
                    <div class='contact-label'>📍 الموقع</div>
                    <div class='contact-value'>عمّان</div>
                </div>
                <div class='contact-item'>
                    <div class='contact-label'>⏰ الأوقات</div>
                    <div class='contact-value'>10 صباح - 2 صباح</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Social Media
    st.markdown("""
        <div class='info-section' style='text-align: center;'>
            <div class='section-title' style='text-align: center;'>تابعنا على وسائل التواصل</div>
            <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
                <a href='https://www.instagram.com/dayaarestaurant/?hl=ar' target='_blank' style='text-decoration: none;'>
                    <div style='background: #E1306C; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700;'>📸 Instagram</div>
                </a>
                <a href='https://wa.me/962790000000' target='_blank' style='text-decoration: none;'>
                    <div style='background: #25D366; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700;'>💬 WhatsApp</div>
                </a>
                <a href='tel:+962790000000' style='text-decoration: none;'>
                    <div style='background: #0095F6; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700;'>📞 اتصل بنا</div>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🛒 اطلب الآن", use_container_width=True, key="cta_order"):
            st.session_state.page = 'menu'
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)

# --- صفحة المنيو ---
elif st.session_state.page == 'menu':
    # Header
    st.markdown("""
        <div class='hero-container'>
            <div class='hero-title'>📋 المنيو الكامل</div>
            <div class='hero-subtitle'>اختر من أفضل الأطباق</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Categories - Tabs
    col_cats = st.columns(4)
    categories = list(items_db.keys())
    
    # Get current category from session
    if 'current_category' not in st.session_state:
        st.session_state.current_category = categories[0]
    
    # Category buttons
    for i, cat in enumerate(categories[:4]):
        with col_cats[i]:
            if st.button(cat, key=f"cat_{i}", use_container_width=True):
                st.session_state.current_category = cat
                st.rerun()
    
    if len(categories) > 4:
        col_cats2 = st.columns(len(categories) - 4)
        for i, cat in enumerate(categories[4:]):
            with col_cats2[i]:
                if st.button(cat, key=f"cat_{i+4}", use_container_width=True):
                    st.session_state.current_category = cat
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Menu display with cart
    col_menu, col_cart = st.columns([3, 1.2], gap="medium")
    
    with col_menu:
        st.markdown(f"<div class='category-title'>{st.session_state.current_category}</div>", unsafe_allow_html=True)
        
        # Display items in grid
        items = items_db[st.session_state.current_category]
        cols = st.columns(3)
        
        for idx, item in enumerate(items):
            with cols[idx % 3]:
                st.markdown(f"""
                    <div class='menu-item-card'>
                        <img src='{item['image']}' class='item-image' alt='{item['name']}' />
                        <div class='item-name'>{item['name']}</div>
                        <div class='item-desc'>{item['desc']}</div>
                        <div class='item-footer'>
                            <span class='item-price'>{item['price']:.2f} د.ا</span>
                        </div>
                        <div class='nutrition-tag'>{item['nut']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"➕ أضف للسلة", key=f"add_{idx}_{st.session_state.current_category}", use_container_width=True):
                    st.session_state.cart.append({'n': item['name'], 'p': item['price']})
                    st.session_state.total += item['price']
                    st.rerun()
    
    with col_cart:
        # Cart Section
        st.markdown("<div class='cart-container'>", unsafe_allow_html=True)
        st.markdown("<div class='cart-header'>🛒 السلة</div>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.markdown("<div class='cart-empty'>السلة فارغة</div>", unsafe_allow_html=True)
        else:
            for i, item in enumerate(st.session_state.cart):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"""
                        <div class='cart-item'>
                            <span>{item['p']:.2f} د.ا</span>
                            <span>{item['n']}</span>
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("🗑️", key=f"del_{i}", use_container_width=True):
                        st.session_state.total -= st.session_state.cart[i]['p']
                        st.session_state.cart.pop(i)
                        st.rerun()
        
        st.markdown(f"""
            <div class='cart-total'>
                الإجمالي: {st.session_state.total:.2f} د.ا
            </div>
        """, unsafe_allow_html=True)
        
        # User Info
        u_name = st.text_input("👤 اسمك", placeholder="أدخل اسمك")
        u_phone = st.text_input("📱 رقم الهاتف", placeholder="أدخل رقم هاتفك")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("📤 إرسال الطلب", use_container_width=True):
            if u_name and u_phone and st.session_state.cart:
                items_txt = "\n".join([f"• {x['n']} - {x['p']:.2f} د.ا" for x in st.session_state.cart])
                full_msg = f"""
<b>🔔 طلب جديد من موقع الضيعة!</b>
👤 <b>الزبون:</b> {u_name}
📞 <b>الهاتف:</b> {u_phone}
📦 <b>الطلبات:</b>
{items_txt}
💰 <b>الإجمالي:</b> {st.session_state.total:.2f} د.ا
                """
                send_telegram_notification(full_msg)
                st.success("✅ تم إرسال الطلب بنجاح! سيتصل بك الفريق قريباً")
                st.session_state.cart = []
                st.session_state.total = 0.0
                st.balloons()
            else:
                if not st.session_state.cart:
                    st.warning("⚠️ السلة فارغة!")
                if not u_name:
                    st.warning("⚠️ أدخل اسمك من فضلك")
                if not u_phone:
                    st.warning("⚠️ أدخل رقم هاتفك من فضلك")

# --- صفحة التواصل ---
elif st.session_state.page == 'contact':
    st.markdown("""
        <div class='hero-container'>
            <div class='hero-title'>📞 تواصل معنا</div>
            <div class='hero-subtitle'>نحن هنا لخدمتك</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class='info-section'>
                <div class='section-title'>📱 المعلومات</div>
                <div style='font-size: 18px; line-height: 2; text-align: right; color: #262626;'>
                    <div style='margin-bottom: 20px;'>
                        <strong>☎️ الهاتف:</strong><br>
                        <span style='color: #0095F6; font-weight: 700;'>079-0000000</span>
                    </div>
                    <div style='margin-bottom: 20px;'>
                        <strong>📍 الموقع:</strong><br>
                        <span style='color: #0095F6; font-weight: 700;'>عمّان - الأردن</span>
                    </div>
                    <div style='margin-bottom: 20px;'>
                        <strong>⏰ ساعات العمل:</strong><br>
                        <span style='color: #0095F6; font-weight: 700;'>10 صباح - 2 صباح</span><br>
                        <span style='font-size: 14px;'>كل أيام الأسبوع</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='info-section'>
                <div class='section-title'>💬 تواصل معنا</div>
            </div>
        """, unsafe_allow_html=True)

        contact_name = st.text_input("👤 اسمك", placeholder="أدخل اسمك")
        contact_email = st.text_input("📧 بريدك الإلكتروني", placeholder="أدخل بريدك")
        contact_message = st.text_area("💬 رسالتك", placeholder="أخبرنا برأيك أو استفسارك", height=150)

        if st.button("📤 إرسال الرسالة", use_container_width=True):
            if contact_name and contact_email and contact_message:
                msg = f"""
<b>📧 رسالة جديدة من الموقع!</b>
👤 <b>الاسم:</b> {contact_name}
📧 <b>البريد:</b> {contact_email}
💬 <b>الرسالة:</b>
{contact_message}
                """
                send_telegram_notification(msg)
                st.success("✅ تم إرسال رسالتك بنجاح! شكراً لتواصلك معنا")
            else:
                st.warning("⚠️ يرجى ملء جميع الحقول")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div class='info-section'>
            <div class='section-title'>🌐 تابعنا على وسائل التواصل</div>
            <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
                <a href='https://www.instagram.com/dayaarestaurant/?hl=ar' target='_blank' style='text-decoration: none;'>
                    <div style='background: #E1306C; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700; font-size: 16px;'>📸 Instagram</div>
                </a>
                <a href='https://wa.me/962790000000' target='_blank' style='text-decoration: none;'>
                    <div style='background: #25D366; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700; font-size: 16px;'>💬 WhatsApp</div>
                </a>
                <a href='tel:+962790000000' style='text-decoration: none;'>
                    <div style='background: #0095F6; color: white; padding: 15px 25px; border-radius: 8px; font-weight: 700; font-size: 16px;'>📞 اتصل مباشرة</div>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)
