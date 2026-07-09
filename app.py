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
# SESSION
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
# HALAMAN
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
# NAVIGASI
# ==========================================================

if not st.session_state.logged_in:

    navigation = st.navigation([
        login_page,
        register_page
    ])

else:

    st.write("Dashboard akan dibuat pada tahap berikutnya.")

    st.stop()


navigation.run()

from database import fetch_all

users = fetch_all("SELECT * FROM users")

st.dataframe(users)

import streamlit as st

st.write(st.__version__)
