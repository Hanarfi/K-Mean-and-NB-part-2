# ==========================================================
# SISTEM ANALISIS DATA PASIEN RAWAT INAP ANAK
# APP.PY
# ==========================================================

import os
import streamlit as st

from config import APP_NAME, ASSET_FOLDER
from database import create_tables

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# MEMBUAT DATABASE
# ==========================================================

create_tables()

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    css_path = os.path.join(ASSET_FOLDER, "style.css")

    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================================================
# SESSION DEFAULT
# ==========================================================

DEFAULT_SESSION = {
    "logged_in": False,
    "user_id": None,
    "username": None,
    "nama": None,
    "role": None
}

for key, value in DEFAULT_SESSION.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# HALAMAN AUTENTIKASI
# ==========================================================

login_page = st.Page(
    "auth/login.py",
    title="Login",
    icon="🔐",
    default=True
)

register_page = st.Page(
    "auth/register.py",
    title="Register",
    icon="📝"
)

# ==========================================================
# HALAMAN USER
# ==========================================================

dashboard_page = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="🏠",
    default=True
)

dataset_page = st.Page(
    "pages/dataset.py",
    title="Dataset Saya",
    icon="📁"
)

kmeans_page = st.Page(
    "pages/kmeans.py",
    title="K-Means",
    icon="📊"
)

naive_bayes_page = st.Page(
    "pages/naive_bayes.py",
    title="Naive Bayes",
    icon="🧠"
)

evaluasi_page = st.Page(
    "pages/evaluasi.py",
    title="Uji Model",
    icon="📈"
)

riwayat_page = st.Page(
    "pages/riwayat.py",
    title="Riwayat",
    icon="🕒"
)

laporan_page = st.Page(
    "pages/laporan.py",
    title="Laporan",
    icon="📄"
)

profil_page = st.Page(
    "pages/profile.py",
    title="Profil",
    icon="👤"
)

# ==========================================================
# HALAMAN ADMIN
# ==========================================================

admin_user_page = st.Page(
    "pages/admin_user.py",
    title="Manajemen User",
    icon="👥"
)

admin_dataset_page = st.Page(
    "pages/admin_dataset.py",
    title="Semua Dataset",
    icon="🗂️"
)

# ==========================================================
# HALAMAN PIMPINAN
# ==========================================================

hasil_analisis_page = st.Page(
    "pages/hasil_analisis.py",
    title="Hasil Analisis",
    icon="📊"
)

# ==========================================================
# NAVIGASI
# ==========================================================

if not st.session_state.logged_in:

    navigation = st.navigation(
        [login_page, register_page],
        position="hidden"
    )

elif st.session_state.role == "Admin":

    navigation = st.navigation([
        dashboard_page,
        dataset_page,
        kmeans_page,
        naive_bayes_page,
        evaluasi_page,
        riwayat_page,
        laporan_page,
        admin_user_page,
        admin_dataset_page,
        profil_page
    ])

elif st.session_state.role == "Pimpinan":

    navigation = st.navigation([
        dashboard_page,
        hasil_analisis_page,
        laporan_page,
        profil_page
    ])

else:

    navigation = st.navigation([
        dashboard_page,
        dataset_page,
        kmeans_page,
        naive_bayes_page,
        evaluasi_page,
        riwayat_page,
        laporan_page,
        profil_page
    ])

navigation.run()



from database import fetch_all

users = fetch_all("SELECT * FROM users")

st.dataframe(users)

import streamlit as st

st.write(st.__version__)
