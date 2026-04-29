import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# --- ASSETS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

# Animasi khusus untuk Register (User SignUp)
lottie_register = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m6zLpk.json")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
    }
    
    /* Register Card */
    .register-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    
    /* Button Styling */
    div.stButton > button:first-child {
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        height: 3rem;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC REGISTER ---
def show_register():
    cols = st.columns([1, 2, 1])
    
    with cols[1]:
        st.markdown('<div class="register-container">', unsafe_allow_html=True)
        
        # Header & Animasi
        if lottie_register:
            st_lottie(lottie_register, height=150, key="reg_anim")
        
        st.markdown("<h2 style='text-align: center; color: #333;'>Join the Community</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #777;'>Buat akun untuk mulai memprediksi grade nilai kamu</p>", unsafe_allow_html=True)
        
        # Form Input
        with st.form("register_form"):
            col_name1, col_name2 = st.columns(2)
            with col_name1:
                first_name = st.text_input("Nama Depan")
            with col_name2:
                last_name = st.text_input("Nama Belakang")
                
            email = st.text_input("📧 Email", placeholder="fajar@student.com")
            username = st.text_input("👤 Username")
            
            password = st.text_input("🔑 Password", type="password")
            confirm_password = st.text_input("确认 Confirm Password", type="password")
            
            agree = st.checkbox("Saya setuju dengan syarat dan ketentuan")
            
            submit_reg = st.form_submit_button("DAFTAR SEKARANG")
            
            if submit_reg:
                if not username or not password:
                    st.error("Username dan Password wajib diisi!")
                elif password != confirm_password:
                    st.error("Konfirmasi password tidak cocok!")
                elif not agree:
                    st.warning("Anda harus menyetujui syarat & ketentuan.")
                else:
                    # Simulasi simpan data
                    with st.spinner("Mendaftarkan akun Anda..."):
                        time.sleep(2)
                        st.balloons()
                        st.success(f"Akun @{username} berhasil dibuat!")
                        st.info("Silakan buka halaman login untuk masuk.")

        # Tombol navigasi balik ke login (opsional)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sudah punya akun? Login di sini"):
            st.write("Navigasi ke login...") # Ganti dengan logika pindah page
            
        st.markdown('</div>', unsafe_allow_html=True)

# Jalankan fungsi
show_register()