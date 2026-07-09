# ==========================================================
# SISTEM ANALISIS DATA PASIEN RAWAT INAP ANAK
# APP.PY
# ==========================================================

import streamlit as st

from config import APP_NAME
from config import APP_VERSION

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

# ==========================================================
# HALAMAN AWAL
# ==========================================================

if not st.session_state.login:
    st.switch_page("pages/login.py")

st.write("Dashboard")
