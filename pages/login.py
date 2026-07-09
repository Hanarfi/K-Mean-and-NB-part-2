import streamlit as st
import hashlib

from database import fetch_one
from config import APP_NAME


# ==========================================================
# HASH PASSWORD
# ==========================================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ==========================================================
# JIKA SUDAH LOGIN
# ==========================================================

if st.session_state.get("logged_in", False):
    st.switch_page("app.py")


# ==========================================================
# TAMPILAN LOGIN
# ==========================================================

st.title("🏥 " + APP_NAME)

st.subheader("Login")

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

login = st.button(
    "Login",
    use_container_width=True
)


# ==========================================================
# PROSES LOGIN
# ==========================================================

if login:

    if username == "" or password == "":

        st.warning("Username dan Password wajib diisi.")

    else:

        password_hash = hash_password(password)

        user = fetch_one(
            """
            SELECT *
            FROM users
            WHERE username=?
            AND password=?
            """,
            (
                username,
                password_hash
            )
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.user_id = user["id_user"]

            st.session_state.username = user["username"]

            st.session_state.nama = user["nama"]

            st.session_state.role = user["role"]

            st.success("Login berhasil.")

            st.rerun()

        else:

            st.error(
                "Username atau Password salah."
            )
