import streamlit as st
import urllib.parse

# Konfigurasi Halaman
st.set_page_config(page_title="Form Bukber KaDesa", page_icon="🍱", layout="centered")

# --- HEADER & JUDUL ---
st.title("🍱 Form Pemesanan Bukber - KaDesa")
st.markdown("Pilih paket dan menu favoritmu di bawah ini.")

# --- FORM PEMESANAN ---
with st.form("form_bukber", clear_on_submit=False):
    
    # 1. Informasi Dasar
    st.subheader("📍 Data Pemesan")
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Lengkap / Grup")
        tanggal = st.date_input("Tanggal Acara")
    with col2:
        jumlah = st.number_input("Jumlah Pax (Orang)", min_value=1, step=1)
        whatsapp = st.text_input("Nomor WhatsApp (Contoh: 0812xxx)")

    st.markdown("---")

    # 2. Pilihan Paket
    st.subheader("🍱 Pilih Jenis Paket")
    paket = st.selectbox("Daftar Paket", [
        "Paket 54.900 (1 Ayam/Gurameh, 1 Tumisan)",
        "Paket 59.900 (1 Ayam/Gurameh, 2 Tumisan)",
        "Paket 69.900 (Ayam Potong + Gurami Fillet, 2 Tumisan)"
    ])

    # 3. Kustomisasi Menu
    st.subheader("🍽️ Kustomisasi Menu")
    
    nasi = st.selectbox("Pilihan Nasi", ["Nasi Putih", "Nasi Liwet", "Nasi Merah"])
    nasi_bakar = st.checkbox("Ganti Nasi Bakar (+Rp3.000/pack)")

    col_lauk1, col_lauk2 = st.columns(2)
    with col_lauk1:
        ayam = st.selectbox("Pilihan Olahan Ayam", ["Goreng Lengkuas", "Bakar Kecap"])
        pejantan = st.checkbox("Upgrade Ayam Pejantan (+10rb)")
    with col_lauk2:
        gurameh = st.selectbox("Pilihan Olahan Gurameh", ["Asam Manis", "Pesmol", "Goreng"])

    gorengan = st.multiselect("Pilihan Gorengan (Pilih 1)", 
                             ["Tempe Goreng", "Tempe Mendoan", "Bakwan Sayur", "Tahu Goreng"])
    
    tumisan = st.multiselect("Pilihan Tumisan (Sesuai Paket)", 
                            ["Tumis Toge Tahu", "Tumis Daun Pepaya", "Tumis Soon Cabai Hijau", "Tumis Ace Tempe", "Tumis Kangkung"])

    sambal = st.radio("Pilihan Sambal", ["Sambal Bawang", "Sambal Trasi"], horizontal=True)

    st.markdown("---")
    
    # 4. Fitur Upload File (Bukti Transfer/List Nama)
    st.subheader("📁 Lampiran (Opsional)")
    uploaded_file = st.file_uploader("Upload Bukti Transfer atau Daftar Nama", type=['jpg','png','jpeg','pdf'])

    catatan = st.text_area("Catatan Tambahan (Contoh: Meja di area taman)")

    # TOMBOL SUBMIT
    submit_button = st.form_submit_button("SIMPAN & KIRIM PESANAN")

# --- LOGIKA SETELAH KLIK SUBMIT ---
if submit_button:
    if not nama or not whatsapp:
        st.error("Mohon isi Nama dan Nomor WhatsApp terlebih dahulu!")
    else:
        st.success(f"Pesanan atas nama **{nama}** berhasil dicatat secara sistem!")
        st.balloons()

        # Generate Pesan WhatsApp Otomatis
        teks_wa = f"*PESANAN BUKBER KADESA*\n\n" \
                  f"*Nama:* {nama}\n" \
                  f"*Tanggal:* {tanggal}\n" \
                  f"*Jumlah:* {jumlah} Pax\n" \
                  f"*Paket:* {paket}\n" \
                  f"*Detail:* {nasi} {'(+ Nasi Bakar)' if nasi_bakar else ''}, {ayam}/{gurameh}, {', '.join(tumisan)}, {sambal}\n" \
                  f"*Catatan:* {catatan}"
        
        # Encoding teks agar bisa masuk URL
        pesan_encoded = urllib.parse.quote(teks_wa)
        
        # Link WhatsApp Admin (Ganti dengan nomor admin resto yang benar)
        link_wa = f"https://wa.me/6281393099930?text={pesan_encoded}"

        st.info("Langkah terakhir: Klik tombol di bawah ini untuk mengirim detail ke WhatsApp Admin.")
        st.markdown(f'''
            <a href="{link_wa}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:10px; cursor:pointer; font-weight:bold;">
                    📲 KIRIM KONFIRMASI KE WHATSAPP
                </button>
            </a>
            ''', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Powered by Gemini AI Collaboration")
