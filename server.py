# server.py - CPMK.09.2 Server API
# Install terlebih dahulu: pip install flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# Data buku disimpan dalam list (sebagai pengganti database)
buku_data = [
    {"id": 1, "judul": "Harry Potter", "pengarang": "J.K. Rowling", "tahun": 1997},
    {"id": 2, "judul": "Laskar Pelangi", "pengarang": "Andrea Hirata", "tahun": 2005},
    {"id": 3, "judul": "Bumi Manusia", "pengarang": "Pramoedya Ananta Toer", "tahun": 1980}
]

id_counter = 4  # Counter untuk ID buku baru

# ENDPOINT UTAMA
@app.route('/', methods=['GET'])
def home():
    """Endpoint utama untuk mengecek server"""
    return jsonify({
        "message": "Server Manajemen Buku API",
        "status": "running",
        "endpoints": {
            "GET /api/buku": "Mendapatkan semua buku",
            "GET /api/buku/<id>": "Mendapatkan buku berdasarkan ID",
            "POST /api/buku": "Menambah buku baru",
            "PUT /api/buku/<id>": "Update buku",
            "DELETE /api/buku/<id>": "Hapus buku"
        }
    })

# GET - Mendapatkan semua buku
@app.route('/api/buku', methods=['GET'])
def get_semua_buku():
    """Mendapatkan semua data buku"""
    return jsonify({
        "status": "success",
        "data": buku_data,
        "total": len(buku_data)
    })

# GET - Mendapatkan buku berdasarkan ID
@app.route('/api/buku/<int:id_buku>', methods=['GET'])
def get_buku_by_id(id_buku):
    """Mendapatkan buku berdasarkan ID"""
    buku = next((b for b in buku_data if b["id"] == id_buku), None)
    
    if buku:
        return jsonify({
            "status": "success",
            "data": buku
        })
    else:
        return jsonify({
            "status": "error",
            "message": f"Buku dengan ID {id_buku} tidak ditemukan"
        }), 404

# POST - Menambah buku baru
@app.route('/api/buku', methods=['POST'])
def tambah_buku():
    """Menambah buku baru"""
    global id_counter
    
    try:
        data = request.get_json()
        
        # Validasi data
        if not data or not all(key in data for key in ["judul", "pengarang", "tahun"]):
            return jsonify({
                "status": "error",
                "message": "Data tidak lengkap. Diperlukan: judul, pengarang, tahun"
            }), 400
        
        # Membuat buku baru
        buku_baru = {
            "id": id_counter,
            "judul": data["judul"],
            "pengarang": data["pengarang"],
            "tahun": int(data["tahun"])
        }
        
        buku_data.append(buku_baru)
        id_counter += 1
        
        return jsonify({
            "status": "success",
            "message": "Buku berhasil ditambahkan",
            "data": buku_baru
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# PUT - Update buku
@app.route('/api/buku/<int:id_buku>', methods=['PUT'])
def update_buku(id_buku):
    """Update data buku"""
    try:
        data = request.get_json()
        
        # Cari buku berdasarkan ID
        buku = next((b for b in buku_data if b["id"] == id_buku), None)
        
        if not buku:
            return jsonify({
                "status": "error",
                "message": f"Buku dengan ID {id_buku} tidak ditemukan"
            }), 404
        
        # Update data buku
        if "judul" in data:
            buku["judul"] = data["judul"]
        if "pengarang" in data:
            buku["pengarang"] = data["pengarang"]
        if "tahun" in data:
            buku["tahun"] = int(data["tahun"])
        
        return jsonify({
            "status": "success",
            "message": "Buku berhasil diupdate",
            "data": buku
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# DELETE - Hapus buku
@app.route('/api/buku/<int:id_buku>', methods=['DELETE'])
def hapus_buku(id_buku):
    """Hapus buku berdasarkan ID"""
    global buku_data
    
    # Cari index buku
    buku_index = next((i for i, b in enumerate(buku_data) if b["id"] == id_buku), None)
    
    if buku_index is not None:
        buku_terhapus = buku_data.pop(buku_index)
        return jsonify({
            "status": "success",
            "message": f"Buku '{buku_terhapus['judul']}' berhasil dihapus",
            "data": buku_terhapus
        })
    else:
        return jsonify({
            "status": "error",
            "message": f"Buku dengan ID {id_buku} tidak ditemukan"
        }), 404

# Error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint tidak ditemukan"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Terjadi kesalahan server"
    }), 500

if __name__ == '__main__':
    print("🚀 Server API Manajemen Buku dimulai...")
    print("📖 Akses: http://localhost:5000")
    print("📋 API Docs: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)