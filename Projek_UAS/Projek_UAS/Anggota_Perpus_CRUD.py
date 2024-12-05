import sqlite3

db_name = 'Sqlite3.db'

#CREATE USER
def registrasi_user(nama, password):
    conn = sqlite3.connect(db_name)

    #BUAT CURSOR
    c = conn.cursor()

    #CEK APAKAH USER DENGAN NAMA TERSEBUT SUDAH ADA ATAU BELUM
    #KALAU ADA, MAKA TIDAK BOLEH REGISTRASI (NAMA USER HARUS UNIK)
    data_nama = read_a_user(nama)
    if data_nama is not None:
        return False, "User name already exist"


    #ISI NAMA USER DAN PASSWORD KE TABEL ANGGOTA
    c.execute(
        """
        INSERT INTO anggota (nama, password) VALUES (?,?)
        """,(nama,password)
    )
    
    #COMMIT TRANSAKSI
    conn.commit()
    conn.close()
    return True, "Working"

# READ SELURUH DATA PADA TABEL USER
def read_all_user():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    #EKSEKUSI QUERRY UNTUK MENGAMBIL SEMUA ROW PADA TABEL ANGGOTA
    c.execute(
        """
        SELECT * FROM anggota
        """
    )
    data = c.fetchall()
    conn.close()
    #RETURN DATA (TIDAK PERLU STATUS/PESAN KARENA HANYA MELAKUKAN READ. LOGIC AKAN DI URUS DI FLASK APP)
    return data

def read_a_user_by_id(id):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    #EKSEKUSI QUERRY UNTUK MENGAMBIL ROW BERDASARKAN ID
    c.execute(
        """
        SELECT * FROM anggota WHERE id = ?
        """,(id,)
    )
    #AMBIL SATU DATA SAJA
    data = c.fetchone()
    conn.close()   
    return data

def read_a_user(nama):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    #EKSEKUSI QUERRY UNTUK MENGAMBIL ROW BERDASARKAN NAMA
    c.execute(
        """
        SELECT * FROM anggota WHERE nama = ?
        """,(nama,)
    )
    #AMBIL SATU DATA SAJA
    data = c.fetchone()
    conn.close()
    return data

def update_user(id,nama, nama_baru, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Cek apakah user asli atau tidak
    cek_user  = read_a_user(nama)
    if cek_user is None:
        return False, "User not found"


    # Cek apakah user name yang dipilih, ada atau tidak.
    if nama_baru != nama:
        cek_username = read_a_user(nama_baru)
        if cek_username is not None:
            return False, "User name already exist"

    
    #EKSESKUSI QUERRY UNTUK UPDATE USER

    c.execute(
        """
        UPDATE anggota SET nama =?,password=? WHERE id=?
        """,(nama_baru,password, id)
    )


    #COMMIT TRANSAKSI
    conn.commit()
    conn.close()
    return True, "Working"

def delete_user(id):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    #CEK APAKAH USER DENGAN ID INI ADA DI DB ATAU TIDAK.
    cek_user  = read_a_user_by_id(id)
    if cek_user is None:
        return False, "User not found"

    #UNPACK DATA
    id, nama, password, id_buku_dipinjam, status_peminjaman = cek_user
    #EKSESKUSI QUERRY UNTUK DELETE USER
    c.execute(
        """
        UPDATE buku SET peminjam_id = ?, status_peminjaman = ? WHERE id = ?
        """,(None, False, id_buku_dipinjam)
    )

 
    #EKSEKUSI QUERRY UNTUK MENGHAPUS ROW BERDASARKAN ID
    c.execute(
        """
        DELETE FROM anggota WHERE id = ?
        """,(id,)
    )
    #COMMIT TRANSAKSI
    conn.commit()
    #TUTUP KONEKSI
    conn.close()
    #RETURN STATUS DAN PESAN
    return True, "Working"


def verify_user_login(nama, password):
    #MEMBUAT KONEKSI DENGAN DB
    conn = sqlite3.connect(db_name)
    #BUAT KURSOR
    c = conn.cursor()
    #EKSEKUSI QUERRY UNTUK MENGAMBIL ROW BERDASARKAN NAMA DAN PASSWORD
    c.execute(
        """
        SELECT * FROM anggota WHERE nama = ? AND password = ?
        """,(nama,password)
        
    )
    #AMBIL SATU DATA SAJA
    user = c.fetchone()
    #TUTUP KONEKSI
    conn.close()
    #RETURN DATA
    return user



def not_in_use():

    # def add_user(nama, password):
    #     conn = sqlite3.connect(db_name)
    #     c = conn.cursor()

    #     exist_user = read_a_user(nama)
    #     if exist_user is not None:
    #         return False, "User name already exist"

    #     c.execute(
    #         """
    #         INSERT INTO anggota (nama, password) VALUES (?,?)
    #         """,(nama,password)
    #     )
    #     conn.commit()
    #     conn.close()

    #     return True, "Working"
    pass



if __name__ == '__main__':
    print(registrasi_user('testuser','testpassword'))
    print(read_all_user())

    