import os
import streamlit as st

from config import APP_NAME, HOSPITAL_NAME, ASSET_FOLDER


# ==========================================================
# LOGO
# ==========================================================

logo_path = os.path.join(
    ASSET_FOLDER,
    "logo.png"
)


# ==========================================================
# LAYOUT
# ==========================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if os.path.exists(logo_path):
        st.image(logo_path, width=180)

    st.markdown(f"## {APP_NAME}")

    st.caption(HOSPITAL_NAME)

    st.divider()

    username = st.text_input(
        "Username",
        placeholder="Masukkan username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Masukkan password"
    )

    login = st.button(
        "🔐 Login",
        use_container_width=True
    )

    st.divider()

    st.write("Belum memiliki akun?")

    st.page_link(
        "pages/register.py",
        label="Daftar di sini"
    )
