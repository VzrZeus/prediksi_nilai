import streamlit as st
import pandas as pd
import time
from streamlit_lottie import st_lottie
import requests

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Grade Predictor Pro", page_icon="🏆", layout="wide")

# --- 2. FUNGSI ASSETS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_trophy = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
lottie_login = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ktwnwv5m.json")
lottie_register = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m6zLpk.json")

# --- 3. CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { border: 1px solid #f0f2f6; padding: 20px; border-radius: 12px; box-shadow: 2px 2px 5px rgba(0,0,0,0.03); background-color: white; }
    .login-card, .register-card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stButton>button { width: 100%; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SESSION STATE MANAGEMENT ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
if "users_db" not in st.session_state:
    st.session_state.users_db = {"fajar": "informatika"} 
# Inisialisasi Database Nilai (CRUD)
if "db_nilai" not in st.session_state:
    st.session_state.db_nilai = pd.DataFrame(columns=["Nama", "Tugas", "Absen", "UTS", "UAS", "Skor", "Grade"])

# --- 5. FUNGSI HALAMAN REGISTER ---
def register_page():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='register-card'>", unsafe_allow_html=True)
        if lottie_register:
            st_lottie(lottie_register, height=180, key="reg_anim")
        
        st.markdown("<h2 style='text-align: center;'>📝 Register Akun</h2>", unsafe_allow_html=True)
        new_user = st.text_input("Username Baru", key="reg_user")
        new_pw = st.text_input("Password Baru", type="password", key="reg_pw")
        confirm_pw = st.text_input("Konfirmasi Password", type="password", key="reg_confirm")
        
        if st.button("DAFTAR SEKARANG", key="btn_reg"):
            if new_user and new_pw == confirm_pw:
                st.session_state.users_db[new_user] = new_pw
                st.success(f"Akun {new_user} berhasil dibuat! Silakan Login.")
                time.sleep(1.5)
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("Password tidak cocok atau data belum lengkap!")
        
        if st.button("Kembali ke Login", key="btn_back"):
            st.session_state.page = "login"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 6. FUNGSI HALAMAN LOGIN ---
def login_page():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        if lottie_login:
            st_lottie(lottie_login, height=200, key="login_anim")
        
        st.markdown("<h2 style='text-align: center;'>🔐 Member Login</h2>", unsafe_allow_html=True)
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pw")
        
        if st.button("LOGIN SEKARANG", key="btn_login"):
            if username in st.session_state.users_db and st.session_state.users_db[username] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username 
                st.success(f"Selamat datang, {username}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Username atau password salah!")
        
        st.markdown("<p style='text-align: center;'>Belum punya akun?</p>", unsafe_allow_html=True)
        if st.button("Daftar Akun Baru", key="btn_to_reg"):
            st.session_state.page = "register"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# --- 7. APLIKASI UTAMA (MAIN APP) ---
def main_app():
    with st.sidebar:
        st.title("👨‍🎓 Menu Utama")
        st.write(f"Logged in as: **{st.session_state.current_user}**")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()
        st.divider()
        st.info("Kelola data nilai dan prediksi grade mahasiswa secara cerdas.")

    st.title("📊 Student Performance & Management System")
    
    # Menggunakan Tabs untuk memisahkan fitur Prediksi dan Database
    tab_prediksi, tab_database = st.tabs(["🚀 Prediksi Grade", "📂 Database & CRUD"])

    with tab_prediksi:
        st.markdown("### Input Data Mahasiswa")
        col1, col2 = st.columns([1, 1])
        with col1:
            nama = st.text_input("Nama Mahasiswa", placeholder="Nama Lengkap...", key="input_nama")
            tugas = st.slider("Nilai Tugas", 0, 100, 80)
            absen = st.slider("Kehadiran (%)", 0, 100, 95)

        with col2:
            uts = st.number_input("Nilai UTS", 0, 100, 75)
            uas = st.number_input("Target UAS", 0, 100, 75)

        if st.button("🚀 ANALISIS & SIMPAN"):
            if nama == "":
                st.warning("Mohon isi nama mahasiswa terlebih dahulu.")
            else:
                with st.spinner("Mengkalkulasi..."):
                    time.sleep(0.8)
                    score = (tugas * 0.2) + (absen * 0.1) + (uts * 0.3) + (uas * 0.4)
                    
                    if score >= 85: grade, status, msg = "A", "Lulus (Sangat Baik)", "LUAR BIASA! 🌟"
                    elif score >= 75: grade, status, msg = "B", "Lulus (Baik)", "MANTAP! 👍"
                    elif score >= 60: grade, status, msg = "C", "Lulus (Cukup)", "KERJA BAGUS! 😊"
                    else: grade, status, msg = "D/E", "Kurang Memuaskan", "SEMANGAT! 💪"

                    if score >= 85:
                        c1, c2, c3 = st.columns([1, 1, 1])
                        with c2: st_lottie(lottie_trophy, height=180)
                        st.balloons()
                    
                    st.markdown(f"### Hasil Prediksi: **{nama}**")
                    st.success(msg)
                    
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Skor Akhir", f"{score:.2f}")
                    m2.metric("Grade", grade)
                    m3.metric("Status", status)

                    # LOGIKA CREATE (Menyimpan data ke DataFrame)
                    new_entry = pd.DataFrame([[nama, tugas, absen, uts, uas, score, grade]], 
                                            columns=["Nama", "Tugas", "Absen", "UTS", "UAS", "Skor", "Grade"])
                    st.session_state.db_nilai = pd.concat([st.session_state.db_nilai, new_entry], ignore_index=True)
                    st.toast("Data berhasil disimpan ke database!", icon="💾")

    with tab_database:
        st.markdown("### 🗄️ Manajemen Database Nilai")
        
        # READ (Menampilkan Data)
        if st.session_state.db_nilai.empty:
            st.info("Belum ada data tersimpan.")
        else:
            # Tampilkan Tabel
            st.dataframe(st.session_state.db_nilai, use_container_width=True)

            # Bagian UPDATE & DELETE
            st.divider()
            col_u, col_d = st.columns(2)
            
            with col_u:
                st.markdown("#### 🔄 Update Data")
                idx_update = st.selectbox("Pilih Index untuk di-Update", st.session_state.db_nilai.index)
                nama_baru = st.text_input("Update Nama", value=st.session_state.db_nilai.loc[idx_update, "Nama"])
                if st.button("Update Nama"):
                    st.session_state.db_nilai.at[idx_update, "Nama"] = nama_baru
                    st.success("Data berhasil diperbarui!")
                    st.rerun()

            with col_d:
                st.markdown("#### 🗑️ Hapus Data")
                idx_delete = st.selectbox("Pilih Index untuk di-Hapus", st.session_state.db_nilai.index)
                if st.button("⚠️ Hapus Baris", type="primary"):
                    st.session_state.db_nilai = st.session_state.db_nilai.drop(idx_delete).reset_index(drop=True)
                    st.warning("Data telah dihapus.")
                    st.rerun()

    st.markdown("<br><center><small>Academic Predictor v2.0 | 2026</small></center>", unsafe_allow_html=True)

# --- 8. ALUR NAVIGASI UTAMA ---
if st.session_state.logged_in:
    main_app()
else:
    if st.session_state.page == "login":
        login_page()
    else:
        register_page()