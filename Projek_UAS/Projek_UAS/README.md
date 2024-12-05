# LANGKAH - LANGKAH TESTING
1. RUN "python init_testing.py"

# LANGKAH - LANGKAH DEPLOY 
1. RUN "python init_deploying.py"
2. RUN "python frontend_controler.py"

NOTE : init deploying hanya perlu dijalankan satu kali saja pada saat melakukan deploy pertama kali. Setelah itu, apabila ingin menjalankan program, jalankan langkah 2 saja. 

Dokumentasi Aplikasi
- Anggota_Perpus_CRUD.py : Berisi Aplikasi CRUD untuk Anggota Perpustakaan
- Buku_Perpus_CRUD.py : Berisi Aplikasi CRUD untuk Buku Perpustakaan
- create_db.py : Hanya untuk membuat db sqlite apabila belum ada
- create_table.py : Membuat semua table yang diperlukan pada db sqlite
- frontend_controler.py : Berisi aplikasi flask. Berfungsi sebagai pengontrol aplikasi antara page html dan logic aplikasi (python)
- Fitur_Lainnya.py : Berisi fitur lainnya seperti fitur pencarian, fitur pengembalian buku, fitur peminjaman buku
- init_deploying.py : Berisi langkah - langkah untuk melakukan deploy aplikasi pertama kali
- init_testing.py : Berisi langkah - langkah untuk melakukan testing aplikasi
- test_frontend_controler.py : Berisi testcase untuk aplikasi
- Folder templates : Berisi semua file html yang digunakan pada aplikasi
- requirements.txt : Berisi semua library yang digunakan pada aplikasi