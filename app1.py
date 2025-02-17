from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

# Fungsi untuk mendapatkan koneksi database
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

# Menutup koneksi database setelah request selesai
@app.teardown_appcontext
def close_connection(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Halaman utama
@app.route('/')
def index():
    return render_template('kamigori.html')

# Halaman daftar makanan
@app.route('/makanan')
def makanan():
    db = get_db()
    cursor = db.execute("SELECT * FROM makanan")
    makanan_list = cursor.fetchall()
    return render_template('makanan.html', makanan_list=makanan_list)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/nature')
def nature():
    return render_template('nature.html')

# Jalankan server
if __name__ == '__main__':
    app.run(debug=True)
