import streamlit as st
import time

# Thiết lập cấu hình trang
st.set_page_config(page_title="Khu Vườn Trên Mây", layout="wide")

# CSS cho giao diện
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #87CEEB, #E0F6FF);
    font-family: 'Arial', sans-serif;
    overflow: hidden;
}

.cloud {
    position: absolute;
    background: white;
    border-radius: 100px;
    opacity: 0.8;
    animation: float 20s infinite linear;
}

@keyframes float {
    0% { transform: translateX(0); }
    50% { transform: translateX(100px); }
    100% { transform: translateX(0); }
}

#cloud1 { width: 200px; height: 100px; top: 10%; left: 10%; }
#cloud2 { width: 150px; height: 80px; top: 20%; left: 60%; animation-delay: -5s; }
#cloud3 { width: 180px; height: 90px; top: 30%; left: 30%; animation-delay: -10s; }

.garden-container {
    position: relative;
    height: 80vh;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.pot {
    position: absolute;
    width: 100px;
    height: 100px;
    background: url('https://img.icons8.com/color/96/000000/plant-under-sun.png');
    background-size: cover;
    cursor: pointer;
    transition: transform 0.3s;
}

.pot:hover {
    transform: scale(1.2);
}

#pot1 { bottom: 20%; left: 20%; }
#pot2 { bottom: 20%; left: 40%; }
#pot3 { bottom: 20%; left: 60%; }

.spirit {
    position: absolute;
    width: 80px;
    height: 80px;
    background: url('https://img.icons8.com/color/96/000000/phoenix.png');
    background-size: cover;
    animation: fly 5s infinite ease-in-out;
}

@keyframes fly {
    0% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}

#spirit1 { top: 10%; left: 25%; }
#spirit2 { top: 15%; left: 65%; }

.login-form {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(255, 255, 255, 0.9);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    z-index: 1000;
    animation: popup 0.5s ease-out;
}

@keyframes popup {
    0% { transform: translate(-50%, -60%) scale(0.8); opacity: 0; }
    100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
}

.login-form input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #87CEEB;
    border-radius: 5px;
    font-size: 16px;
}

.login-form button {
    width: 100%;
    padding: 10px;
    background: #87CEEB;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
}

.login-form button:hover {
    background: #4682B4;
}

.scoreboard {
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.9);
    padding: 10px 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.stButton>button {
    background: #87CEEB;
    color: white;
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    transition: background 0.3s;
}

.stButton>button:hover {
    background: #4682B4;
}
</style>
""", unsafe_allow_html=True)

# HTML cho mây
st.markdown("""
<div id="cloud1" class="cloud"></div>
<div id="cloud2" class="cloud"></div>
<div id="cloud3" class="cloud"></div>
""", unsafe_allow_html=True)

# Quản lý trạng thái
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'plants' not in st.session_state:
    st.session_state.plants = {1: "Empty", 2: "Empty", 3: "Empty"}
if 'spirits' not in st.session_state:
    st.session_state.spirits = {1: "Hungry", 2: "Hungry"}

# Form đăng nhập
if not st.session_state.logged_in:
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #4682B4;">Đăng Nhập Khu Vườn Trên Mây</h2>', unsafe_allow_html=True)
    
    username = st.text_input("Tên người chơi", key="username")
    password = st.text_input("Mật khẩu", type="password", key="password")
    
    if st.button("Đăng Nhập"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Đăng nhập thành công!")
            st.rerun()
        else:
            st.error("Vui lòng nhập đầy đủ thông tin!")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Giao diện chính
    st.markdown(f'<h1 style="text-align: center; color: #4682B4;">Chào mừng {st.session_state.username} đến với Khu Vườn Trên Mây!</h1>', unsafe_allow_html=True)
    st.markdown('<div class="garden-container">', unsafe_allow_html=True)
    
    # Chậu cây
    for i in range(1, 4):
        st.markdown(f'<div id="pot{i}" class="pot"></div>', unsafe_allow_html=True)
    
    # Linh thú
    st.markdown('<div id="spirit1" class="spirit"></div>', unsafe_allow_html=True)
    st.markdown('<div id="spirit2" class="spirit"></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bảng điểm
    st.markdown(f'<div class="scoreboard">Điểm: {st.session_state.score}</div>', unsafe_allow_html=True)
    
    # Tính năng game
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Quản lý chậu cây")
        pot_id = st.selectbox("Chọn chậu", [1, 2, 3], key="pot_select")
        action = st.selectbox("Hành động", ["Trồng cây", "Tưới nước", "Thu hoạch"], key="pot_action")
        if st.button("Thực hiện", key="pot_button"):
            if action == "Trồng cây":
                if st.session_state.plants[pot_id] == "Empty":
                    st.session_state.plants[pot_id] = "Planted"
                    st.session_state.score += 5
                    st.success(f"Đã trồng cây ở chậu {pot_id}!")
                else:
                    st.warning("Chậu này đã có cây!")
            elif action == "Tưới nước":
                if st.session_state.plants[pot_id] != "Empty":
                    st.session_state.plants[pot_id] = "Watered"
                    st.session_state.score += 3
                    st.success(f"Đã tưới nước cho cây ở chậu {pot_id}!")
                else:
                    st.warning("Chậu này chưa có cây!")
            elif action == "Thu hoạch":
                if st.session_state.plants[pot_id] in ["Planted", "Watered"]:
                    st.session_state.plants[pot_id] = "Empty"
                    st.session_state.score += 10
                    st.success(f"Đã thu hoạch cây ở chậu {pot_id}!")
                else:
                    st.warning("Chậu này chưa có cây để thu hoạch!")
    
    with col2:
        st.subheader("Tương tác linh thú")
        spirit_id = st.selectbox("Chọn linh thú", [1, 2], key="spirit_select")
        spirit_action = st.selectbox("Hành động với linh thú", ["Cho ăn", "Chơi cùng"], key="spirit_action")
        if st.button("Tương tác", key="spirit_button"):
            if spirit_action == "Cho ăn":
                st.session_state.spirits[spirit_id] = "Fed"
                st.session_state.score += 5
                st.success(f"Linh thú {spirit_id} đã được cho ăn!")
            elif spirit_action == "Chơi cùng":
                st.session_state.spirits[spirit_id] = "Happy"
                st.session_state.score += 7
                st.success(f"Đã chơi cùng linh thú {spirit_id}!")
    
    # Hiển thị trạng thái
    st.write("**Trạng thái chậu cây:**", st.session_state.plants)
    st.write("**Trạng thái linh thú:**", st.session_state.spirits)
    
    # Nút đăng xuất
    if st.button("Đăng xuất", key="logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.score = 0
        st.session_state.plants = {1: "Empty", 2: "Empty", 3: "Empty"}
        st.session_state.spirits = {1: "Hungry", 2: "Hungry"}
        st.rerun()
