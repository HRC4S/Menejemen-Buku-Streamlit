# 📚 Sistem Manajemen Buku - CPMK Project

Project sederhana untuk memenuhi CPMK.06.1 dan CPMK.09.2 dengan tema manajemen buku.

## 🎯 CPMK yang Dipenuhi

### CPMK.06.1 (Bobot: 40%)
Program sederhana yang menggunakan:
- ✅ **Percabangan**: if-else untuk validasi dan menu
- ✅ **Perulangan**: while dan for untuk menu dan iterasi data
- ✅ **Function**: berbagai function untuk modularitas
- ✅ **List**: menyimpan data buku dalam list
- ✅ **String**: manipulasi string untuk pencarian dan formatting
- ✅ **OOP**: Class Buku dan ManajemenBuku

### CPMK.09.2 (Bobot: 50%)
REST API Client-Server dengan:
- ✅ **GET**: Mengambil data buku (semua & by ID)
- ✅ **POST**: Menambah buku baru
- ✅ **PUT**: Update data buku
- ✅ **DELETE**: Hapus buku
- ✅ **Python**: Menggunakan Flask (server) dan requests (client)

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install flask requests streamlit
```

### 2. Jalankan Server (Terminal 1)
```bash
python server.py
```
Server akan berjalan di: `http://localhost:5000`

### 3. Jalankan Client (Terminal 2)
```bash
python -m streamlit run client.py
```

### 4. Jalankan Program Basic (Opsional)
```bash
python models.py
```

## 📁 Struktur File

```
project/
├── main.py          # CPMK.06.1 - Program basic
├── server.py        # CPMK.09.2 - REST API Server
├── client.py        # CPMK.09.2 - API Client
├── requirements.txt # Dependencies
└── README.md        # Dokumentasi
```

## 🔗 API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/buku` | Mengambil semua buku |
| GET | `/api/buku/<id>` | Mengambil buku berdasarkan ID |
| POST | `/api/buku` | Menambah buku baru |
| PUT | `/api/buku/<id>` | Update buku |
| DELETE | `/api/buku/<id>` | Hapus buku |

## 📊 Contoh Data JSON

### POST Request (Tambah Buku):
```json
{
    "judul": "Sang Pemimpi",
    "pengarang": "Andrea Hirata",
    "tahun": 2006
}
```

### Response Success:
```json
{
    "status": "success",
    "message": "Buku berhasil ditambahkan",
    "data": {
        "id": 4,
        "judul": "Sang Pemimpi",
        "pengarang": "Andrea Hirata",
        "tahun": 2006
    }
}
```

## 🧪 Testing API

### Manual Testing dengan Client:
1. Jalankan `server.py`
2. Jalankan `client.py`
3. Pilih menu untuk test semua method (GET, POST, PUT, DELETE)

### Testing dengan Postman/Curl:
```bash
# GET semua buku
curl http://localhost:5000/api/buku

# POST tambah buku
curl -X POST http://localhost:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul":"Test Book","pengarang":"Test Author","tahun":2024}'

# PUT update buku
curl -X PUT http://localhost:5000/api/buku/1 \
  -H "Content-Type: application/json" \
  -d '{"judul":"Updated Title"}'

# DELETE hapus buku
curl -X DELETE http://localhost:5000/api/buku/1
```

## 🎯 Fitur Utama

### Program Basic (models.py):
- Menampilkan Menu
- Tambahkan Buku
- Cari Buku dengan ID
- Hapus Buku Dengan ID
