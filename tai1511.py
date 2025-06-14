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
            st.success("✅ Đăng ký thành công! Vui lòng đăng nhập.")
        else:
            st.error("❌ Tên người dùng đã tồn tại.")

# -------------------- Đăng nhập --------------------
elif choice == "Đăng nhập":
    st.subheader("🔐 Đăng nhập")
    username = st.text_input("👤 Tên người dùng")
    password = st.text_input("🔒 Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"🎉 Chào mừng {username} quay lại!")
        else:
            st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")

# -------------------- Vào game --------------------
elif choice == "Vào game":
    if not st.session_state.logged_in:
        st.warning("⚠️ Bạn cần đăng nhập để chơi game.")
    else:
        st.subheader(f"🎮 Đấu trường bắt đầu - Chiến đấu thôi, {st.session_state.username}!")

        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/lion.gif", caption="🦁 Bạn", width=250)
        with col2:
            st.image("assets/tiger.gif", caption="🐯 Đối thủ", width=250)

        attack = st.selectbox("💥 Chọn tuyệt chiêu của bạn:", 
                              ["Cào xé", "Cắn mạnh", "Chưởng lửa", "Gầm sấm"])
        
        if st.button("⚔️ Tấn công"):
            enemy_attack = choose_attack()
            st.info(f"🐯 Đối thủ dùng tuyệt chiêu: **{enemy_attack}**")
            
            result = random.choice(["win", "lose"])
            if result == "win":
                st.success("🎉 Bạn đã chiến thắng trận đấu!")
                st.image("assets/win.gif", width=300)
            else:
                st.error("💀 Bạn đã thất bại!")
                st.image("lose.gif", width=300)

        st.caption("🔥 Mỗi trận đấu là ngẫu nhiên, hãy thử nhiều lần!")

