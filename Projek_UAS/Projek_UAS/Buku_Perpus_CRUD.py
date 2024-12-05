import sqlite3

db_name = 'Sqlite3.db'


def daftar_buku(judul, penulis, penerbit, tahun_terbit, deskripsi_buku):
    #MEMULAI KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT CURSOR
    c = conn.cursor()

    #ISI DATA BUKU KEDALAM TABEL BUKU
    c.execute(
        """
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, deskripsi) VALUES (?,?,?,?,?)
        """,(judul,penulis,penerbit,tahun_terbit, deskripsi_buku)
    )

    #COMMIT TRANSAKSI
    conn.commit()
    #TUTUP KONEKSI
    conn.close()
    #RETURN STATUS DAN PESAN
    return True, "Working"


def baca_satu_buku(judul):
    #MEMULAI KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT CURSOR
    c = conn.cursor()

    #EKSEKUSI QUERRY UNTUK MENGAMBIL ROW BERDASARKAN JUDUL
    c.execute(
        """
        SELECT * FROM buku WHERE judul=?
        """,(judul,)
    )
    #AMBIL SATU DATA SAJA
    data = c.fetchone()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return data

def baca_satu_buku_by_id(id):
    #MEMULAI KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #EKSEKUSI QUERRY UNTUK MENGAMBIL ROW BERDASARKAN ID
    c.execute(
        """
        SELECT * FROM buku WHERE id=?
        """,(id,)
    )
    #AMBIL SATU DATA SAJA
    data = c.fetchone()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return data

def baca_tabel_buku():
    #MEMULAI KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()
    #EKSEKUSI QUERRY UNTUK MENGAMBIL SEMUA ROW PADA TABEL BUKU
    c.execute(
        """
        SELECT * FROM buku
        """
    )
    #AMBIL SEMUA ROW
    data = c.fetchall()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return data

def update_buku(id,judul_baru, penulis, penerbit, tahun_terbit,deskripsi):
    #MEMULAI KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #EKSEKUSI QUERRY UNTUK UPDATE BUKU
    c.execute(
        """
        UPDATE buku SET judul=?,penulis=?,penerbit=?,tahun_terbit=?, deskripsi=? WHERE id=?
        """,(judul_baru,penulis,penerbit,tahun_terbit,deskripsi,id)
    )
    #COMMIT TRANSAKSI
    conn.commit()
    #TUTUP KONEKSI
    conn.close()
    #RETURN STATUS DAN PESAN
    return True, "Working"


def delete_user(id):
    #MEMBUAT KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #CEK APAKAH DENGAN ID INI ADA DI DB ATAU TIDAK.
    cek_buku = baca_satu_buku_by_id(id)
    if cek_buku is None:
        return False, "Buku not found"

    #UNPACK DATA
    id, judul, penulis, penerbit, tahun_terbit, deskripsi, peminjam_id, status_peminjaman = cek_buku

    #CEK APAKAH BUKU SEDANG DIPINJAM ATAU TIDAK
    if peminjam_id is not None:
        #KALAU DIPINJAM, LEPAS BUKU DARI PEMINJAMAN USER
        c.execute(
            """
            UPDATE anggota SET id_buku_dipinjam = ?, status_peminjaman = ? WHERE id = ?
            """,(None, False, peminjam_id)
        )
        

    #EKSEKUSI QUERRY UNTUK MENGHAPUS ROW BERDASARKAN ID
    c.execute(
        """
        DELETE FROM buku WHERE id = ?
        """,(id,)
    )

    #COMMIT TRANSAKSI
    conn.commit()
    #TUTUP KONEKSI
    conn.close()
    #RETURN STATUS DAN PESAN
    return True, "Working"



if __name__ == '__main__':
    print(daftar_buku("COO","ME","THEM","2024","DESKRIPSI BUKU"))
    print(baca_tabel_buku())
    
        

    
    
    

