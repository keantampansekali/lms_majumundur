import pytest
from flask import session


# Test login functionality
def test_login(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
    assert response.status_code == 200
    assert 'username' in session
    assert session['username'] == 'testuser'
    assert b'Invalid username or password' in response.data or b'Manage Anggota Perpustakaan' in response.data

# Test index route (when user is logged in)
def test_index_logged_in(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/anggota_index')
    print(response.status_code)
    assert response.status_code == 200
    assert b'employee' in response.data  # Assuming "Employees" is present in the index page content

# Test add employee route (GET)
def test_add_employee_get(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/add')
    assert response.status_code == 200
    assert b'Add' in response.data

# Test add employee route (POST)
def test_add_employee_post(client, monkeypatch):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    # def mock_add_user(name, password):
    #     return True, 'User added successfully!'

    # monkeypatch.setattr('Anggota_Perpus_CRUD.registrasi_user', mock_add_user)
    response = client.post('/add', data={'name': 'new_employee', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Anggota added successfully!' in response.data

# Test edit employee route (GET)
def test_edit_employee_get(client, monkeypatch):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    # def mock_read_a_user_by_id(id):
    #     return (id, 'current_name', 'password123')
    
    # monkeypatch.setattr('Anggota_Perpus_CRUD.read_a_user_by_id', mock_read_a_user_by_id)
    response = client.get('/edit/2')
    assert response.status_code == 200
    assert b'Edit' in response.data

# Test edit employee route (POST)
def test_edit_employee_post(client, monkeypatch):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    # def mock_update_user(id, current_name, name, password):
    #     return True, 'Updated successfully!'
    
    # monkeypatch.setattr('Anggota_Perpus_CRUD.update_user', mock_update_user)
    response = client.post('/edit/2', data={'name': 'updated_employee', 'password': 'new_password'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Anggota updated successfully!' in response.data

# Test delete employee route
def test_delete_employee(client, monkeypatch):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    # def mock_delete_user(id):
    #     return False, 'Deleted successfully!'
    
    # monkeypatch.setattr('Anggota_Perpus_CRUD.delete_user', mock_delete_user)
    response = client.get('/delete/2', follow_redirects=True)
    print(response.status_code)
    assert response.status_code == 200
    assert b'Anggota deleted successfully!' in response.data

#TEST BUKU_PERPUS_CRUD HERE
def test_buku_index(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku_index')
    assert response.status_code == 200
    assert b'Manage Buku Perpustakaan' in response.data

def test_tambah_buku_get(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku/add')
    assert response.status_code == 200
    assert b"Add Book" in response.data

def test_tambah_buku_post(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    data = {
        'judul': 'New Book',
        'penulis': 'Author Name',
        'penerbit': 'Publisher Name',
        'tahun_terbit': '2024',
        'deskripsi': 'This is a description of the new book.'
    }
    response = client.post('/buku/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buku berhasil ditambahkan!" in response.data

def test_edit_buku_get(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku/edit/2')
    assert response.status_code == 200
    assert b"Edit Book" in response.data

def test_edit_buku_post(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    data = {
        'judul': 'Updated Book',
        'penulis': 'Updated Author',
        'penerbit': 'Updated Publisher',
        'tahun_terbit': '2024',
        'deskripsi': 'Updated description'
    }
    response = client.post('/buku/edit/2', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buku berhasil diupdate!" in response.data

def test_delete_buku(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku/delete/2', follow_redirects=True)
    assert response.status_code == 200
    assert b"Buku berhasil dihapus!" in response.data

#TES FITUR TAMBAHAN
def test_pinjam_buku(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku/pinjam/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Buku berhasil dipinjam!" in response.data

def test_kembalikan_buku(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/buku/kembalikan/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Buku berhasil dikembalikan!" in response.data


#TES LOGOUT. DIPANGGIL TERAKHIR KARENA SEMUA FUNGSI SEBELUMNYA HARUS DI TES DENGAN SESSION.
def test_logout(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'You have been logged out.' in response.data
    assert 'username' not in session