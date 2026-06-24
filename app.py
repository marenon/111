import streamlit as st
import datetime

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram AI", page_icon="🎀", layout="wide")

# 2. إدارة الحالة (State Management) للغات والثيمات والبيانات
if 'lang' not in st.session_state:
    st.session_state.lang = 'Ar'  # الافتراضي عربي
if 'theme' not in st.session_state:
    st.session_state.theme = 'Light'  # الافتراضي صباحي
if 'database' not in st.session_state:
    # بيانات وهمية أولية للتوضيح داخل السجل
    st.session_state.database = [
        {"name": "سارة أحمد", "phone": "07701234567", "age": 45, "family": "نعم", "result": "حميد (Benign)", "time": "2026-06-25 10:30"},
        {"name": "مريم علي", "phone": "07809876543", "age": 52, "family": "لا", "result": "خبيث (Malignant)", "time": "2026-06-25 11:15"}
    ]

# النصوص المترجمة للغتين
text = {
    'Ar': {
        'title': "🎀 نظام فحص الماموجرام الذكي",
        'login': "👩‍⚕️ أولاً: تسجيل دخول الطبيب",
        'user': "اسم المستخدم",
        'pass': "كلمة المرور",
        'btn_login': "حفظ الحساب ودخول",
        'patient_sec': "📋 ثانياً: بيانات المريض",
        'p_name': "اسم المريض الكامل",
        'p_phone': "رقم الهاتف",
        'p_age': "العمر",
        'family_q': "هل يوجد تاريخ إصابة بسرطان الثدي في العائلة؟",
        'upload_sec': "📷 ثالثاً: رفع صورة أو ملف الماموجرام",
        'upload_placeholder': "اختر صورة الماموجرام أو اسحبها هنا...",
        'result_sec': "🔬 رابعاً: نتيجة التحليل الذكي",
        'result_placeholder': "اختر النتيجة لتجربة التلوين الوردي:",
        'normal': "طبيعي (Normal)",
        'benign': "غير طبيعي - حميد (Benign)",
        'malignant': "غير طبيعي - خبيث (Malignant)",
        'save_record': "💾 حفظ السجل الحالي في البيانات",
        'footer': "✨ صحتكِ تهمنا ✨",
        'menu_title': "⚙️ القائمة الذكية",
        'db_view': "📊 سجل البيانات الكامل",
        'support': "🛠️ تواصل مع الدعم الفني",
        'support_desc': "إذا واجهت أي خلل تقني، يرجى كتابته هنا:",
        'send': "إرسال بلاغ",
        'msg_saved': "تم حفظ الحساب!",
        'msg_record_added': "تم إضافة المريض بنجاح إلى سجل البيانات والوقت!"
    },
    'En': {
        'title': "🎀 Smart Mammogram System",
        'login': "👩‍⚕️ First: Doctor Login",
        'user': "Username / Email",
        'pass': "Password",
        'btn_login': "Save Account & Login",
        'patient_sec': "📋 Second: Patient Information",
        'p_name': "Patient Full Name",
        'p_phone': "Phone Number",
        'p_age': "Age",
        'family_q': "Is there a family history of breast cancer?",
        'upload_sec': "📷 Third: Upload Mammogram",
        'upload_placeholder': "Choose a mammogram image or drag it here...",
        'result_sec': "🔬 Fourth: AI Analysis Result",
        'result_placeholder': "Select result to test pink coloring:",
        'normal': "Normal",
        'benign': "Abnormal - Benign",
        'malignant': "Abnormal - Malignant",
        'save_record': "💾 Save Record to Database",
        'footer': "✨ Your Health Matters ✨",
        'menu_title': "⚙️ Smart Menu",
        'db_view': "📊 Complete Records Log",
        'support': "🛠️ Contact Technical Support",
        'support_desc': "If you encounter any technical glitch, please write it here:",
        'send': "Send Report",
        'msg_saved': "Account Saved!",
        'msg_record_added': "Patient successfully added to log with timestamp!"
    }
}

L = text[st.session_state.lang]

# 3. التحكم بالثيمات (صباحي / ليلي) والخلفيات الوردية عبر CSS المتفاعل
bg_color = "#FFF5F5" if st.session_state.theme == "Light" else "#1A1012"
text_color = "#4A1521" if st.session_state.theme == "Light" else "#FFE4E6"
card_bg = "#FFFFFF" if st.session_state.theme == "Light" else "#2D1B1E"
border_color = "#FBCFE8" if st.session_state.theme == "Light" else "#4C242E"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; }}
    h1, h2, h3, h4, p, label, span {{ color: {text_color} !important; font-family: 'Arial', sans-serif; }}
    .stTextInput input, .stNumberInput input, .stSelectbox div {{
        border: 2px solid {border_color} !important;border-radius: 10px !important;
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}
    .stButton button {{
        background-color: #EC4899 !important; color: white !important;
        border-radius: 8px !important; border: none !important; width: 100%; font-weight: bold;
    }}
    .stButton button:hover {{ background-color: #DB2777 !important; }}
    .footer {{
        text-align: center; font-size: 28px; font-weight: bold; color: #DB2777;
        margin-top: 50px; padding: 20px; border-top: 2px dashed #FBCFE8;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. الشريط العلوي (Header) لتبديل اللغة والثيم
top_col1, top_col2, top_col3 = st.columns([6, 1, 1])
with top_col1:
    st.markdown(f"<h1 style='color: #DB2777;'>{L['title']}</h1>", unsafe_allow_html=True)
with top_col2:
    if st.button("🌐 En/عربي"):
        st.session_state.lang = 'En' if st.session_state.lang == 'Ar' else 'Ar'
        st.rerun()
with top_col3:
    if st.button("🌙/☀️"):
        st.session_state.theme = 'Dark' if st.session_state.theme == 'Light' else 'Light'
        st.rerun()

st.markdown("<hr style='border: 1px solid #FBCFE8;'>", unsafe_allow_html=True)

# 5. القائمة الجانبية (النقاط الثلاثة / الخيارات المتقدمة)
with st.sidebar:
    st.markdown(f"## {L['menu_title']}")
    
    # الخيار الأول: عرض البيانات المحفوظة والوقت والتاريخ
    with st.expander(L['db_view'], expanded=False):
        if st.session_state.database:
            for item in st.session_state.database:
                st.markdown(f"""
                ---
                👤 الاسم: {item['name']}  
                📞 الهاتف: {item['phone']} | 🎂 العمر: {item['age']}  
                🧬 تاريخ عائلي: {item['family']}  
                🔬 التشخيص: {item['result']}  
                📅 الوقت: {item['time']}
                """)
        else:
            st.write("لا توجد سجلات بعد.")
            
    # الخيار الثاني: تواصل مع الدعم الفني
    with st.expander(L['support'], expanded=False):
        st.write(L['support_desc'])
        bug_report = st.text_area("", placeholder="...")
        if st.button(L['send']):
            st.success("تم إرسال بلاغك لفريق الدعم بنجاح.")

# -------------------------------------------------------------
# الواجهة الرئيسية الممتدة (Single Page)
# -------------------------------------------------------------

# 1. قسم حساب الطبيب
st.markdown(f"### {L['login']}")
col1, col2 = st.columns(2)
with col1: password = st.text_input(L['pass'], type="password")
with col2: username = st.text_input(L['user'])
if st.button(L['btn_login']):
    st.success(L['msg_saved'])

st.markdown("<br><hr>", unsafe_allow_html=True)

# 2. قسم بيانات المريض
st.markdown(f"### {L['patient_sec']}")
p_name = st.text_input(L['p_name'])
col3, col4 = st.columns(2)
with col3: p_phone = st.text_input(L['p_phone'])
with col4: p_age = st.number_input(L['p_age'], min_value=1, max_value=120, value=40)
family_history = st.radio(L['family_q'], ("لا" if st.session_state.lang=='Ar' else "No", "نعم" if st.session_state.lang=='Ar' else "Yes"))

st.markdown("<br><hr>", unsafe_allow_html=True)

# 3. قسم رفع الملف
st.markdown(f"### {L['upload_sec']}")
uploaded_file = st.file_uploader(L['upload_placeholder'], type=["jpg", "jpeg", "png", "pdf"])

st.markdown("<br><hr>", unsafe_allow_html=True)

# 4. قسم النتيجة وتدرجات الألوان الوردية المتفاعلة
st.markdown(f"### {L['result_sec']}")
result_type = st.selectbox(L['result_placeholder'], [L['normal'], L['benign'], L['malignant']])

current_result = ""
if result_type == L['normal']:
    current_result = "Normal"
    st.markdown("""
        <div style="background-color: #FCE7F3; padding: 20px; border-radius: 10px; border-left: 8px solid #F472B6; margin-bottom:15px;">
            <h3 style="color: #9D174D !important; margin: 0;">النتيجة: طبيعي (Normal) ✨</h3>
        </div>
    """, unsafe_allow_html=True)
elif result_type == L['benign']:
    current_result = "Benign (حميد)"
    st.markdown("""<div style="background-color: #FBCFE8; padding: 20px; border-radius: 10px; border-left: 8px solid #EC4899; margin-bottom:15px;">
            <h3 style="color: #831843 !important; margin: 0;">النتيجة: غير طبيعي - حميد (Benign) 🌸</h3>
        </div>
    """, unsafe_allow_html=True)
elif result_type == L['malignant']:
    current_result = "Malignant (خبيث)"
    st.markdown("""
        <div style="background-color: #F472B6; padding: 20px; border-radius: 10px; border-left: 8px solid #9D174D; margin-bottom:15px;">
            <h3 style="color: white !important; margin: 0;">النتيجة: غير طبيعي - خبيث (Malignant) ⚠️</h3>
        </div>
    """, unsafe_allow_html=True)

# زر حفظ السجل الحالي في القائمة (السجل المحفوظ) مع التقاط الوقت والتاريخ تلقائياً
if st.button(L['save_record']):
    if p_name:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        new_record = {
            "name": p_name,
            "phone": p_phone,
            "age": p_age,
            "family": family_history,
            "result": current_result,
            "time": now
        }
        st.session_state.database.append(new_record)
        st.success(L['msg_record_added'])
    else:
        st.error("الرجاء إدخال اسم المريض أولاً لحفظ السجل.")

# 5. التذييل الثابت
st.markdown(f"<div class='footer'>{L['footer']}</div>", unsafe_allow_html=True)