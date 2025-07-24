# streamlit_app.py - Web Interface untuk API Client
# Install: pip install streamlit requests

import streamlit as st
import requests
import json

# Konfigurasi halaman
st.set_page_config(
    page_title="Perpustakaan|Belive In God",
    page_icon="📚",
    layout="wide"
)

# URL API Server
API_BASE_URL = "http://localhost:5000"
API_URL = f"{API_BASE_URL}/api/buku"

def test_server_connection():
    """Test koneksi ke server"""
    try:
        response = requests.get(API_BASE_URL, timeout=3)
        return response.status_code == 200
    except:
        return False

def get_all_books():
    """GET - Mendapatkan semua buku"""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()['data']
        return []
    except:
        return []

def get_book_by_id(book_id):
    """GET - Mendapatkan buku berdasarkan ID"""
    try:
        response = requests.get(f"{API_URL}/{book_id}")
        if response.status_code == 200:
            return response.json()['data']
        return None
    except:
        return None

def add_book(judul, pengarang, tahun):
    """POST - Menambah buku baru"""
    try:
        data = {
            "judul": judul,
            "pengarang": pengarang,
            "tahun": tahun
        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 201, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def update_book(book_id, judul=None, pengarang=None, tahun=None):
    """PUT - Update buku"""
    try:
        data = {}
        if judul: data['judul'] = judul
        if pengarang: data['pengarang'] = pengarang
        if tahun: data['tahun'] = tahun
        
        response = requests.put(f"{API_URL}/{book_id}", json=data)
        return response.status_code == 200, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def delete_book(book_id):
    """DELETE - Hapus buku"""
    try:
        response = requests.delete(f"{API_URL}/{book_id}")
        return response.status_code == 200, response.json()
    except Exception as e:
        return False, {"message": str(e)}

# MAIN STREAMLIT APP
def main():
    st.title("📚 Sistem Manajemen Buku - Belive In God")
    st.markdown("**Menejemen Buku Untuk Perpustakaan**")
    
    # Check server connection
    if not test_server_connection():
        st.error("❌ Server tidak dapat diakses! Pastikan server.py sudah berjalan di http://localhost:5000")
        st.info("Jalankan server dengan: `python server.py`")
        return
    
    st.success("✅ Berhasil Terhubung Dengan Server")
    
    # Sidebar untuk navigasi
    st.sidebar.title("🔧 Menu Operasi")
    menu = st.sidebar.selectbox(
        "Pilih Operasi:",
        ["📋 Lihat Semua Buku (GET)", "🔍 Cari Buku by ID (GET)", 
         "➕ Tambah Buku (POST)", "✏️ Update Buku (PUT)", "🗑️ Hapus Buku (DELETE)"]
    )
    
    # Main content area
    if menu == "📋 Lihat Semua Buku (GET)":
        st.header("📋 Daftar Semua Buku")
        
        if st.button("🔄 Refresh Data"):
            st.rerun()
        
        books = get_all_books()
        
        if books:
            st.success(f"📊 Total: {len(books)} buku ditemukan")
            
            # Tampilkan dalam tabel
            for book in books:
                with st.container():
                    col1, col2, col3, col4 = st.columns([1, 3, 2, 1])
                    
                    with col1:
                        st.write(f"**ID: {book['id']}**")
                    with col2:
                        st.write(f"📖 **{book['judul']}**")
                    with col3:
                        st.write(f"👤 {book['pengarang']}")
                    with col4:
                        st.write(f"📅 {book['tahun']}")
                    
                    st.divider()
        else:
            st.info("📭 Tidak ada buku dalam database")
    
    elif menu == "🔍 Cari Buku by ID (GET)":
        st.header("🔍 Cari Buku Berdasarkan ID")
        
        book_id = st.number_input("Masukkan ID Buku:", min_value=1, step=1)
        
        if st.button("🔍 Cari Buku"):
            book = get_book_by_id(book_id)
            
            if book:
                st.success("✅ Buku ditemukan!")
                
                # Tampilkan detail buku
                col1, col2 = st.columns(2)
                
                with col1:
                    st.info(f"**ID:** {book['id']}")
                    st.info(f"**Judul:** {book['judul']}")
                
                with col2:
                    st.info(f"**Pengarang:** {book['pengarang']}")
                    st.info(f"**Tahun:** {book['tahun']}")
            else:
                st.error(f"❌ Buku dengan ID {book_id} tidak ditemukan")
    
    elif menu == "➕ Tambah Buku (POST)":
        st.header("➕ Tambah Buku Baru")
        
        with st.form("add_book_form"):
            judul = st.text_input("📖 Judul Buku:")
            pengarang = st.text_input("👤 Nama Pengarang:")
            tahun = st.number_input("📅 Tahun Terbit:", min_value=1000, max_value=2030, value=2024)
            
            submitted = st.form_submit_button("➕ Tambah Buku")
            
            if submitted:
                if judul and pengarang:
                    success, response = add_book(judul, pengarang, tahun)
                    
                    if success:
                        st.success(f"✅ {response['message']}")
                        st.json(response['data'])
                        st.balloons()  # Animasi celebrasi
                    else:
                        st.error(f"❌ {response['message']}")
                else:
                    st.error("❌ Judul dan pengarang tidak boleh kosong!")
    
    elif menu == "✏️ Update Buku (PUT)":
        st.header("✏️ Update Data Buku")
        
        # Tampilkan daftar buku untuk referensi
        with st.expander("📋 Lihat Daftar Buku"):
            books = get_all_books()
            for book in books:
                st.write(f"ID: {book['id']} - {book['judul']} ({book['pengarang']}, {book['tahun']})")
        
        with st.form("update_book_form"):
            book_id = st.number_input("ID Buku yang akan diupdate:", min_value=1, step=1)
            
            st.write("**Kosongkan field yang tidak ingin diubah:**")
            judul = st.text_input("📖 Judul Baru (opsional):")
            pengarang = st.text_input("👤 Pengarang Baru (opsional):")
            tahun = st.number_input("📅 Tahun Baru (opsional):", min_value=0, max_value=2030, value=0)
            
            submitted = st.form_submit_button("✏️ Update Buku")
            
            if submitted:
                # Hanya kirim data yang diisi
                judul_update = judul if judul else None
                pengarang_update = pengarang if pengarang else None
                tahun_update = tahun if tahun > 0 else None
                
                if judul_update or pengarang_update or tahun_update:
                    success, response = update_book(book_id, judul_update, pengarang_update, tahun_update)
                    
                    if success:
                        st.success(f"✅ {response['message']}")
                        st.json(response['data'])
                    else:
                        st.error(f"❌ {response['message']}")
                else:
                    st.warning("⚠️ Tidak ada data yang akan diupdate")
    
    elif menu == "🗑️ Hapus Buku (DELETE)":
        st.header("🗑️ Hapus Buku")
        
        # Tampilkan daftar buku
        books = get_all_books()
        
        if books:
            st.write("**Daftar Buku:**")
            for book in books:
                st.write(f"ID: {book['id']} - {book['judul']} ({book['pengarang']}, {book['tahun']})")
            
            st.divider()
            
            book_id = st.number_input("ID Buku yang akan dihapus:", min_value=1, step=1)
            
            # Konfirmasi penghapusan
            st.warning("⚠️ **Peringatan:** Penghapusan tidak dapat dibatalkan!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🗑️ Hapus Buku", type="primary"):
                    success, response = delete_book(book_id)
                    
                    if success:
                        st.success(f"✅ {response['message']}")
                        st.rerun()  # Refresh halaman
                    else:
                        st.error(f"❌ {response['message']}")
            
            with col2:
                if st.button("❌ Batal"):
                    st.info("Penghapusan dibatalkan")
        else:
            st.info("📭 Tidak ada buku untuk dihapus")
    
    # Footer
    st.divider()
    st.markdown("---")
    st.markdown("**🚀 Sistem Manajemen Buku API Client**")
    st.markdown("**Belive In God**")
    st.markdown("*Dibuat dengan Streamlit & Python*")

if __name__ == "__main__":
    main()