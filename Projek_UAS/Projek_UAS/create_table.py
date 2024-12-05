import sqlite3

def init_db():
    conn = sqlite3.connect('Sqlite3.db')
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS anggota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        password TEXT NOT NULL,
        id_buku_dipinjam INTEGER,
        status_peminjaman BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (id_buku_dipinjam) REFERENCES buku(id)
        )
        """
    )
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS buku (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        penulis TEXT NOT NULL,
        penerbit TEXT NOT NULL,
        tahun_terbit INTEGER NOT NULL,
        deskripsi TEXT NOT NULL,
        peminjam_id INTEGER,
        status_peminjaman BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (peminjam_id) REFERENCES anggota(id)
        )
        """
    )
    
    conn.commit()
    conn.close()

def drop_table():
    conn = sqlite3.connect('Sqlite3.db')
    c = conn.cursor()
    c.execute(
        """
        DROP TABLE anggota
        """
    )
    c.execute(
        """
        DROP TABLE buku
        """
    )
    conn.commit()
    conn.close()
if __name__ == '__main__':
    drop_table()
    init_db()