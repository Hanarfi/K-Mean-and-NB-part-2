import streamlit as st

from config import APP_NAME
from config import LOGO


# ======================================================
# HEADER
# ======================================================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    if LOGO:
        st.image(LOGO, width=180)

    st.markdown(
        f"<h2 style='text-align:center;'>{APP_NAME}</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Silakan login untuk melanjutkan.</p>",
        unsafe_allow_html=True
    )

    st.write("")

    username = st.text_input(
        "Username",
        placeholder="Masukkan username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Masukkan password"
    )

    st.write("")

    login_btn = st.button(
        "🔐 Login",
        use_container_width=True
    )

    st.write("")

    st.caption("Belum memiliki akun?")

    register_btn = st.button(
        "📝 Register",
        use_container_width=True
    )
