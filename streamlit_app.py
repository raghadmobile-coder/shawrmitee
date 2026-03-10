import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="شاورما ع الصاج", page_icon="🌯")

st.title("🌯 مطعم شاورما ع الصاج - أونلاين")
st.markdown("---")

# المنيو
menu = {
    "ساندويش عادي": 1.75,
    "وجبة سوبر": 3.50,
    "وجبة دبل": 4.50,
    "سدر العيلة الملكي": 18.00,
    "بوكس السعادة": 12.50,
    "بطاطا كبير": 1.50
}

# اختيار الفرع (UI/UX)
branch = st.sidebar.selectbox("📍 اختر الفرع الأقرب إليك:", ["عمان", "إربد", "الزرقاء"])

# عرض المنيو واختيار الأصناف
st.subheader("📋 قائمة الطعام")
order_list = []
total_bill = 0

# عمل مربعات اختيار بجانب كل صنف
for item, price in menu.items():
    if st.checkbox(f"{item} - {price} JOD"):
        order_list.append(item)
        total_bill += price

st.markdown("---")

# زر الطلب والرد الذكي
if st.button("تأكيد الطلب 🚀"):
    if total_bill > 0:
        st.success(f"تم استلام طلبك من فرع {branch}!")
        
        # الرد الذكي AI
        if total_bill == max(menu.values()):
            st.info("🤖 AI: اختيار فخم! السدر الملكي بدو ناس أكيلة، صحتين!")
        elif total_bill > 15:
            st.info("🤖 AI: فاتورة دسمة! رح نبعتلك ثومية وبطاطا هدية من المطعم.")
        else:
            st.info("🤖 AI: اختيار ممتاز! شاورما ع الصاج دايماً بتبيض الوجه.")
            
        st.write("🛒 **سلتك تحتوي على:**", ", ".join(order_list))
        st.write(f"💰 **المجموع النهائي:** {total_bill:.2f} JOD")
    else:
        st.error("الرجاء اختيار صنف واحد على الأقل!")