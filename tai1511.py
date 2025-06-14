
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
    border-radius: 50%;
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

# Form đăng nhập
if not st.session_state.logged_in:
    with st.container():
        st.markdown("""
        <div class="login-form">
            <h2 style="text-align: center; color: #4682B4;">Đăng Nhập Khu Vườn Trên Mây</h2>
            <input type="text" id="username" placeholder="Tên người chơi">
            <input type="password" id="password" placeholder="Mật khẩu">
            <button onclick="login()">Đăng Nhập</button>
        </div>
        """, unsafe_allow_html=True)
        # Giả lập đăng nhập
        if st.button("Đăng Nhập (Giả lập)"):
            st.session_state.logged_in = True
            st.rerun()
else:
    # Giao diện chính
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
        pot_id = st.selectbox("Chọn chậu", [1, 2, 3])
        action = st.selectbox("Hành động", ["Trồng cây", "Tưới nước", "Thu hoạch"])
        if st.button("Thực hiện"):
            if action == "Trồng cây":
                st.session_state.plants[pot_id] = "1"
                st.session_state.score += 5
                st.success(f"Đã trồng cây ở chậu {pot_id}!")
            elif action == "Tưới nước":
                if st.session_state.plants[pot_id] != "Empty":
                    st.session_state.score += 3
                    st.success(f"Đã tưới nước cho cây ở chậu {pot_id}!")
                else:
                    st.warning("Chậu này chưa có cây!")
            elif action == "Thu hoạch":
                if st.session_state.plants[pot_id] != "Empty":
                    st.session_state.plants[pot_id] = "Empty"
                    st.session_state.score += 10
                    st.success(f"Đã thu hoạch cây ở chậu {pot_id}!")
                else:
                    st.warning("Chậu này chưa có cây!")
    
    with col2:
        st.subheader("Tương tác linh thú")
        spirit_action = st.selectbox("Hành động với linh thú", ["Cho ăn", "Chơi cùng"])
        if st.button("Tương tác"):
            if spirit_action == "Cho ăn":
                st.session_state.score += 5
                st.success("Linh thú đã được cho ăn!")
            elif spirit_action == "Chơi cùng":
                st.session_state.score += 7
                st.success("Đã chơi cùng linh thú!")
    
    # Hiển thị trạng thái chậu
    st.write("Trạng thái chậu cây:", st.session_state.plants)

    # Nút đăng xuất
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.rerun()
