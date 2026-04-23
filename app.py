import streamlit as st
import pandas as pd
import time
from streamlit_lottie import st_lottie
import requests

# --- Fungsi untuk Mengambil Animasi Lottie ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Link animasi piala (Lottie JSON)
lottie_trophy = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Grade Predictor Pro", page_icon="🏆", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stMetric { border: 1px solid #f0f2f6; padding: 20px; border-radius: 12px; box-shadow: 2px 2px 5px rgba(0,0,0,0.03); }
    [data-testid="stMetricValue"] { font-size: 28px; color: #007BFF; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 AI Grade Prediction System")
st.markdown("Prediksi grade akhir berdasarkan bobot akademik standar.")
st.divider()

# --- Input Section ---
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("📝 Data Performa")
    nama = st.text_input("Nama Mahasiswa", placeholder="Nama Lengkap...")
    tugas = st.slider("Nilai Tugas (Rata-rata)", 0, 100, 80)
    absen = st.slider("Kehadiran (%)", 0, 100, 95)

with col2:
    st.subheader("🎯 Estimasi Ujian")
    uts = st.number_input("Nilai UTS", min_value=0, max_value=100, value=75)
    uas = st.number_input("Target Nilai UAS", min_value=0, max_value=100, value=75)

# --- Logic Prediksi ---
if st.button("🚀 ANALISIS SEKARANG"):
    with st.spinner("Mengkalkulasi data akademik..."):
        time.sleep(0.8)
        
        score = (tugas * 0.2) + (absen * 0.1) + (uts * 0.3) + (uas * 0.4)
        
        if score >= 85: 
            grade, status = "A", "Lulus (Sangat Baik)"
            feedback_msg = "LUAR BIASA! 🌟 Kamu mendapatkan Piala Emas Akademik!"
        elif score >= 75: 
            grade, status = "B", "Lulus (Baik)"
            feedback_msg = "MANTAP! 👍 Performa yang sangat solid."
        elif score >= 60: 
            grade, status = "C", "Lulus (Cukup)"
            feedback_msg = "KERJA BAGUS! 😊 Tingkatkan lagi di semester depan."
        else: 
            grade, status = "D/E", "Kurang Memuaskan"
            feedback_msg = "TETAP SEMANGAT! 💪 Evaluasi strategimu segera."

       # --- FEEDBACK VISUAL (PIALA) ---
        if score >= 85:
            # Tetap tampilkan piala Lottie di tengah
            c1, c2, c3 = st.columns([1, 1, 1])
            with c2:
                if lottie_trophy:
                    st_lottie(lottie_trophy, height=200, key="trophy")
            
            # GANTI BARIS 72 DENGAN INI:
            st.balloons()  # Efek balon terbang (Bawaan resmi Streamlit)
            st.toast("Prediksi Grade A! Kamu luar biasa! 🏆", icon="🎉")
        # --- Output Display ---
        st.markdown(f"### Hasil Prediksi: **{nama if nama else 'Mahasiswa'}**")
        
        if score >= 75: st.success(feedback_msg)
        else: st.warning(feedback_msg)

        m1, m2, m3 = st.columns(3)
        m1.metric("Prediksi Nilai Akhir", f"{score:.2f}")
        m2.metric("Grade", grade)
        m3.metric("Status", status)

        st.divider()
        
        # --- Insight Strategis ---
        c_left, c_right = st.columns([2, 1])
        with c_left:
            st.subheader("💡 Analisis Rekomendasi")
            if grade != "A":
                target_a = (85 - (tugas * 0.2 + absen * 0.1 + uts * 0.3)) / 0.4
                if target_a <= 100:
                    st.info(f"✨ **Target Grade A:** Kamu butuh nilai UAS minimal **{target_a:.1f}**.")
            
            if absen < 75:
                st.error("❗ **Peringatan:** Kehadiran kritis!")

        with c_right:
            st.subheader("📊 Distribusi Nilai")
            chart_data = pd.DataFrame({
                "Komponen": ["Tugas", "Absen", "UTS", "UAS"],
                "Kontribusi": [tugas*0.2, absen*0.1, uts*0.3, uas*0.4]
            })
            st.bar_chart(chart_data.set_index("Komponen"))

st.markdown("<br><center><small>Academic Predictor v2.0 | 2026</small></center>", unsafe_allow_html=True)