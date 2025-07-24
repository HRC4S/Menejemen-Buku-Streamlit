# CPMK.06.1 - Program Manajemen Buku Sederhana
# Menggunakan: percabangan, perulangan, function, list, string, dan OOP

class Buku:
    """Class untuk merepresentasikan buku (OOP)"""
    def __init__(self, id_buku, judul, pengarang, tahun):
        self.id_buku = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
    
    def info_buku(self):
        """Function untuk menampilkan info buku (string formatting)"""
        return f"ID: {self.id_buku} | Judul: {self.judul} | Pengarang: {self.pengarang} | Tahun: {self.tahun}"

class ManajemenBuku:
    """Class untuk mengelola koleksi buku"""
    def __init__(self):
        self.daftar_buku = []  # List untuk menyimpan buku
        self.id_counter = 1
    
    def tambah_buku(self, judul, pengarang, tahun):
        """Function untuk menambah buku baru"""
        buku_baru = Buku(self.id_counter, judul, pengarang, tahun)
        self.daftar_buku.append(buku_baru)
        self.id_counter += 1
        print(f"✓ Buku '{judul}' berhasil ditambahkan!")
    
    def tampilkan_semua_buku(self):
        """Function untuk menampilkan semua buku dengan perulangan"""
        if not self.daftar_buku:  # Percabangan
            print("Tidak ada buku dalam koleksi.")
            return
        
        print("\n=== DAFTAR BUKU ===")
        for buku in self.daftar_buku:  # Perulangan
            print(buku.info_buku())
    
    def cari_buku(self, kata_kunci):
        """Function untuk mencari buku berdasarkan judul atau pengarang"""
        hasil_pencarian = []
        
        # Perulangan untuk mencari
        for buku in self.daftar_buku:
            # String operation dan percabangan
            if (kata_kunci.lower() in buku.judul.lower() or 
                kata_kunci.lower() in buku.pengarang.lower()):
                hasil_pencarian.append(buku)
        
        if hasil_pencarian:  # Percabangan
            print(f"\n=== HASIL PENCARIAN '{kata_kunci}' ===")
            for buku in hasil_pencarian:  # Perulangan
                print(buku.info_buku())
        else:
            print(f"Tidak ditemukan buku dengan kata kunci '{kata_kunci}'")
    
    def hapus_buku(self, id_buku):
        """Function untuk menghapus buku berdasarkan ID"""
        for i, buku in enumerate(self.daftar_buku):  # Perulangan
            if buku.id_buku == id_buku:  # Percabangan
                buku_terhapus = self.daftar_buku.pop(i)
                print(f"✓ Buku '{buku_terhapus.judul}' berhasil dihapus!")
                return
        
        print(f"Buku dengan ID {id_buku} tidak ditemukan.")

def tampilkan_menu():
    """Function untuk menampilkan menu"""
    print("\n" + "="*40)
    print("      SISTEM MANAJEMEN BUKU")
    print("="*40)
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Cari Buku")
    print("4. Hapus Buku")
    print("5. Keluar")
    print("="*40)

def main():
    """Function utama program"""
    # Membuat objek manajemen buku
    perpustakaan = ManajemenBuku()
    
    # Menambahkan beberapa buku contoh
    perpustakaan.tambah_buku("Harry Potter", "J.K. Rowling", 1997)
    perpustakaan.tambah_buku("Laskar Pelangi", "Andrea Hirata", 2005)
    perpustakaan.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)
    
    # Perulangan utama program
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("Pilih menu (1-5): ").strip()
            
            # Percabangan untuk menangani pilihan menu
            if pilihan == "1":
                print("\n--- TAMBAH BUKU ---")
                judul = input("Masukkan judul buku: ").strip()
                pengarang = input("Masukkan nama pengarang: ").strip()
                
                # Validasi input tahun
                while True:  # Perulangan untuk validasi
                    try:
                        tahun = int(input("Masukkan tahun terbit: "))
                        break
                    except ValueError:
                        print("Tahun harus berupa angka!")
                
                # String validation
                if judul and pengarang:  # Percabangan
                    perpustakaan.tambah_buku(judul, pengarang, tahun)
                else:
                    print("Judul dan pengarang tidak boleh kosong!")
            
            elif pilihan == "2":
                perpustakaan.tampilkan_semua_buku()
            
            elif pilihan == "3":
                print("\n--- CARI BUKU ---")
                kata_kunci = input("Masukkan kata kunci (judul/pengarang): ").strip()
                if kata_kunci:  # Percabangan
                    perpustakaan.cari_buku(kata_kunci)
                else:
                    print("Kata kunci tidak boleh kosong!")
            
            elif pilihan == "4":
                print("\n--- HAPUS BUKU ---")
                perpustakaan.tampilkan_semua_buku()
                try:
                    id_buku = int(input("Masukkan ID buku yang akan dihapus: "))
                    perpustakaan.hapus_buku(id_buku)
                except ValueError:
                    print("ID harus berupa angka!")
            
            elif pilihan == "5":
                print("Terima kasih telah menggunakan Sistem Manajemen Buku!")
                break  # Keluar dari perulangan
            
            else:
                print("Pilihan tidak valid! Pilih 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user.")
            break
        except Exception as e:
            print(f"Terjadi error: {e}")

# Menjalankan program
if __name__ == "__main__":
    main()