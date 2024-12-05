import sqlite3

db_name = 'Sqlite3.db'

def cek_user_status(id_anggota):
    #BUAT KONEKSI KE DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #QUERY CEK STATUS PEMINJAMAN DARI TABEL ANGGOTA BERDASARKAN ID
    c.execute(
        """
        SELECT status_peminjaman FROM anggota WHERE id=?
        """,(id_anggota,)
    )
    #AMBIL DATA
    data = c.fetchone()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return data

def cek_buku_status(id_buku):
    #BUAT KONEKSI KE DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #QUERRY CEK STATUS PEMINJAMAN BUKU DARI TABEL BUKU BERDASARKAN ID
    c.execute(
        """
        SELECT status_peminjaman FROM buku WHERE id=?
        """,(id_buku,)
    )
    #AMBIL DATA
    data = c.fetchone()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return data

def pinjam_buku(id_anggota, id_buku):
    #BUAT KONEKSI KE DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #CEK APAKAH USER SEDANG MEMINJAM BUKU ATAU TIDAK.
    status_user, = cek_user_status(id_anggota)
    if status_user == 1:
        return False, "User sedang meminjam buku. Harap mengembalikan dulu"
    
    #CEK APAKAH BUKU YANG INGIN DIPINJAM, SEDANG DIPINJAM ATAU TIDAK
    status_buku, = cek_buku_status(id_buku)
    if status_buku == 1:
        return False, "Buku sedang dipinjam. Harap memilih buku lain"
    

    #QUERRY PEMINJAMAN BUKU
    c.execute(
        """
        UPDATE anggota SET id_buku_dipinjam=?, status_peminjaman=? WHERE id=?
        """,(id_buku,True,id_anggota)
    )

    c.execute(
        """
        UPDATE buku SET peminjam_id=?, status_peminjaman=? WHERE id=?
        """,(id_anggota,True,id_buku)
    )

    #Commit transaksi
    conn.commit()
    #TUTUP KONEKSI
    conn.close()
    #RETURN status dan pesan
    return True, "Buku berhasil dipinjam"

def cari_buku(search):
    #BUAT KONEKSI KE DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #QUERRY REQUEST BUKU YANG DICARI OLEH USER BERDASARKAN JUDUL
    c.execute(
        """
        SELECT * FROM buku WHERE judul LIKE ?
        """,('%'+search+'%',)
    )

    #AMBIL SEMUA DATA
    data = c.fetchall()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA    
    return data

def kembalikan_buku(id_anggota, id_buku):
    #BUAT KONEKSI KE DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()

    #QUERRY DATA ANGGOTA BERDASARKAN ID
    c.execute(
        """
        SELECT id,id_buku_dipinjam, status_peminjaman FROM anggota WHERE id=?
        """,(id_anggota,)
    )

    #AMBIL DATA DAN UNPACK
    anggota_id, id_buku_dipinjam, status_peminjaman_anggota = c.fetchone()

    #QUERRY DATA BUKU BERDASARKAN ID
    c.execute(
        """
        SELECT id, peminjam_id, status_peminjaman FROM buku WHERE id=?
        """,(id_buku,)
    )

    #AMBIL DATA DAN UNPACK
    buku_id, peminjam_id, status_peminjaman_buku = c.fetchone()

    #SUSUN SEMUA DALAM TUPLE
    pack1 = (id_anggota, id_buku)
    pack2 = (anggota_id, id_buku_dipinjam)
    pack3 = (peminjam_id, buku_id)

    #KONFIRMASI STATUS PEMINJAMAN BUKU PADA KEDUANYA
    if status_peminjaman_buku == 0 and status_peminjaman_anggota == 0:
        return False, "Buku tidak sedang dipinjam atau peminjam sedang tidak meminjam buku " + status_peminjaman_anggota +" " + status_peminjaman_buku
    
    #COMPARE APAKAH ID ANGGOTA DAN BUKU YANG DIPINJAM ITU SAMA DENGAN DI TABEL BUKU
    if pack1 == pack2 == pack3:
        c.execute(
            """
            UPDATE buku SET status_peminjaman = ?, peminjam_id = ? WHERE id = ?
            """,(False, None, id_buku)
        )

        c.execute(
            """
            UPDATE anggota SET status_peminjaman = ?, id_buku_dipinjam = ? WHERE id = ?
            """,(False, None, id_anggota)
        )
        #Commit transaksi
        conn.commit()
        #TUTUP KONEKSI
        conn.close()
        #RETURN status, pesan
        return True, "Buku berhasil dikembalikan"
    else:
        return False, "Buku tidak ditemukan atau buku tidak dipinjam oleh anggota"




