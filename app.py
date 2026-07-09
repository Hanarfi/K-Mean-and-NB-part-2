# ==========================================================
# SISTEM ANALISIS DATA PASIEN RAWAT INAP ANAK
# ==========================================================

import streamlit as st

from config import APP_NAME
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
# SESSION
# ==========================================================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = None

if "role" not in st.session_state:
    st.session_state.role = None


# ==========================================================
# FUNGSI MEMUAT CSS
# ==========================================================

def load_css():

    try:

        with open("style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()


# ==========================================================
# HALAMAN SEMENTARA
# ==========================================================

st.title(APP_NAME)

st.info("🚧 Sistem sedang dalam tahap pengembangan.")

st.write("Tahap berikutnya: Login")
