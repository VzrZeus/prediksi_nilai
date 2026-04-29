import streamlit as st
import pandas as pd
import time
from streamlit_lottie import st_lottie
import requests

# --- 1. CONFIG & ASSETS ---
st.set_page_config(page_title="AI Grade Predictor", page_icon="🔐", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

# Animasi untuk halaman login
lottie_login = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ktwnwv5m.json")
lottie_trophy = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")

# --- 2. CUSTOM CSS (MODERN UI) ---
st.markdown("""
    <style>
    /* Mengubah background utama */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Card style untuk Form Login */
    [data-testid="stVerticalBlock"] > div:has(div.login-box) {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    /* Styling tombol */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 4. HALAMAN LOGIN ---
def show_login():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st_lottie(lottie_login, height=200, key="login_anim")
        st.markdown("<h2 style='text-align: center; color: #333;'>Selamat Datang</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>Silakan login untuk mengakses AI Predictor</p>", unsafe_allow_html=True)
        
        user = st.text_input("👤 Username", placeholder="fajar")
        pw = st.text_input("🔑 Password", type="password", placeholder="********")
        
        if st.button("LOGIN SEKARANG"):
            if user == "fajar" and pw == "informatika":
                st.session_state.logged_in = True
                st.toast("Login Berhasil!", icon="✅")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Username atau password salah!")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. HALAMAN UTAMA (PREDIKSI) ---
def show_main():
    # Sidebar untuk Logout
    with st.sidebar:
        st.markdown(f"### 👤 User: Fajar")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.rerun()
        st.divider()
        st.info("Gunakan aplikasi ini untuk simulasi nilai UAS Anda.")

    # Konten Dashboard Prediksi
    st.title("🎓 AI Student Grade Predictor")
    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📝 Data Performa")
        nama = st.text_input("Nama Mahasiswa", value="Fajar")
        tugas = st.slider("Nilai Tugas", 0, 100, 80)
        absen = st.slider("Kehadiran (%)", 0, 100, 95)

    with col2:
        st.subheader("🎯 Estimasi Ujian")
        uts = st.number_input("Nilai UTS", 0, 100, 75)
        uas = st.number_input("Target Nilai UAS", 0, 100, 75)

    if st.button("🚀 ANALISIS SEKARANG"):
        with st.spinner("Mengkalkulasi..."):
            time.sleep(1)
            score = (tugas * 0.2) + (absen * 0.1) + (uts * 0.3) + (uas * 0.4)
            
            if score >= 85: grade, status = "A", "Sangat Baik"
            elif score >= 75: grade, status = "B", "Baik"
            elif score >= 60: grade, status = "C", "Cukup"
            else: grade, status = "D/E", "Kurang"

            if score >= 85:
                st.balloons()
                c1, c2, c3 = st.columns([1,1,1])
                with c2: st_lottie(lottie_trophy, height=150)

            st.success(f"### Hasil Prediksi: {grade} ({status})")
            st.metric("Skor Akhir", f"{score:.2f}")

# --- 6. JALANKAN APLIKASI ---
if st.session_state.logged_in:
    show_main()
else:
    show_login()