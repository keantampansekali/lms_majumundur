import os

# START TESTING
os.system("python create_table.py")
os.system("python Anggota_Perpus_CRUD.py")
os.system("python Buku_Perpus_CRUD.py")
os.system("py -m pytest")
os.system("python create_table.py")
os.system("python Buku_Perpus_CRUD.py")
os.system("python Anggota_Perpus_CRUD.py")