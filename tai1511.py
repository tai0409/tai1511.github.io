import streamlit as st
import random
import os

# -------------------- Khởi tạo trạng thái --------------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# -------------------- Hàm xử lý đăng ký / đăng nhập --------------------
def register(username, password):
    if username in st.session_state.users:
        return False
    st.session_state.users[username] = password
    return True

def login(username, password):
    return st.session_state.users.get(username) == password

def choose_attack():
    return random.choice(["Cào xé", "Cắn mạnh", "Chưởng lửa", "Gầm sấm"])

# -------------------- Giao diện --------------------
st.set_page_config(page_title="Đấu Trường Thú Web", layout="centered")
st.title("🐾 ĐẤU TRƯỜNG THÚ - Web Arena 🐯")

menu = ["Đăng nhập", "Đăng ký", "Vào game"]
choice = st.sidebar.radio("📋 Menu", menu)

# -------------------- Đăng ký --------------------
if choice == "Đăng ký":
    st.subheader("📌 Đăng ký tài khoản")
    new_user = st.text_input("👤 Tên người dùng")
    new_pass = st.text_input("🔒 Mật khẩu", type="password")
    if st.button("Đăng ký"):
        if register(new_user, new_pass):
            st.success("✅ Đăng ký thành công! Vui lòng đ
