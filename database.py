import sqlite3

# Koneksi ke database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Hapus tabel lama jika ada (agar tidak terjadi duplikasi)
cursor.execute("DROP TABLE IF EXISTS makanan")

# Membuat tabel makanan dengan kolom gambar
cursor.execute("""
CREATE TABLE makanan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    deskripsi TEXT NOT NULL,
    gambar TEXT NOT NULL
)
""")

# Memasukkan data makanan dengan gambar
cursor.executemany("""
INSERT INTO makanan (nama, deskripsi, gambar) VALUES (?, ?, ?)
""", [
    ("圓心の由来", "Koshian paste is wrapped in habutae dough kneaded with soy sauce. Please enjoy the subtle aroma of soy sauce and the refined flavor of red beans..", "kue.jpg"),
    ("モロヘイヤ 羊羹", "Yokan, which has an elegant taste with a beautiful uguisu color kneaded with Moroheiya, a specialty of Kamigori Town, is perfect for tea!", "teh.jpg"),
    ("スノーボール", "This cookie has a crispy texture and is also made using jumbo peanuts. It is baked with ground peanuts, flour, butter, sugar, etc., and finally sprinkled with powdered sugar.", "snowball.jpg")
])

# Simpan perubahan dan tutup koneksi
conn.commit()
conn.close()

print("Database dan tabel makanan berhasil dibuat dengan data lengkap.")
