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

    css_path = os.path.join(
        ASSET_FOLDER,
        "style.css"
    )

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

    "show_register": False,

    "user_id": None,

    "username": None,

    "nama": None,

    "role": None

}

for key, value in DEFAULT_SESSION.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ==========================================================
# BELUM LOGIN
# ==========================================================

if not st.session_state.logged_in:

    # Menyembunyikan sidebar
    st.markdown("""
        <style>
            section[data-testid="stSidebar"]{
                display:none;
            }

            div[data-testid="collapsedControl"]{
                display:none;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.show_register:

        from auth.register import register_page

        register_page()

    else:

        from auth.login import login_page

        login_page()

    st.stop()


# ==========================================================
# SUDAH LOGIN
# ==========================================================

# Halaman User
dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="🏠",
    default=True
)

dataset = st.Page(
    "pages/dataset.py",
    title="Dataset Saya",
    icon="📁"
)

kmeans = st.Page(
    "pages/kmeans.py",
    title="K-Means",
    icon="📊"
)

naive = st.Page(
    "pages/naive_bayes.py",
    title="Naive Bayes",
    icon="🧠"
)

evaluasi = st.Page(
    "pages/evaluasi.py",
    title="Uji Model",
    icon="📈"
)

riwayat = st.Page(
    "pages/riwayat.py",
    title="Riwayat",
    icon="🕒"
)

laporan = st.Page(
    "pages/laporan.py",
    title="Laporan",
    icon="📄"
)

profil = st.Page(
    "pages/profile.py",
    title="Profil",
    icon="👤"
)


# ==========================================================
# NAVIGASI BERDASARKAN ROLE
# ==========================================================

if st.session_state.role == "Admin":

    admin_user = st.Page(
        "pages/admin_user.py",
        title="Manajemen User",
        icon="👥"
    )

    admin_dataset = st.Page(
        "pages/admin_dataset.py",
        title="Semua Dataset",
        icon="🗂️"
    )

    navigation = st.navigation([
        dashboard,
        dataset,
        kmeans,
        naive,
        evaluasi,
        riwayat,
        laporan,
        admin_user,
        admin_dataset,
        profil
    ])

elif st.session_state.role == "Pimpinan":

    hasil = st.Page(
        "pages/hasil_analisis.py",
        title="Hasil Analisis",
        icon="📊"
    )

    navigation = st.navigation([
        dashboard,
        hasil,
        laporan,
        profil
    ])

else:

    navigation = st.navigation([
        dashboard,
        dataset,
        kmeans,
        naive,
        evaluasi,
        riwayat,
        laporan,
        profil
    ])

navigation.run()
