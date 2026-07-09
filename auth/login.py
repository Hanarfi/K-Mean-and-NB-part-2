import streamlit as st

from config import APP_NAME
from config import LOGO


# ==========================================================
# HEADER
# ==========================================================

left, center, right = st.columns([1, 2, 1])

with center:

    st.write("")

    st.image(LOGO, width=140)

    st.markdown(
        f"""
        <h2 style="text-align:center;">
            {APP_NAME}
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;color:gray;">
            Silakan login untuk melanjutkan
        </p>
        """,
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

    login_button = st.button(
        "🔐 Login",
        use_container_width=True
    )

    st.write("")

    st.markdown(
        "<p style='text-align:center;'>Belum memiliki akun?</p>",
        unsafe_allow_html=True
    )

    register_button = st.button(
        "📝 Register",
        use_container_width=True
    )
