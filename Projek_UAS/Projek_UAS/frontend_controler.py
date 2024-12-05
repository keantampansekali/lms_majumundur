from flask import Flask, render_template, request, redirect, url_for, flash, session
import Anggota_Perpus_CRUD as bc
import Buku_Perpus_CRUD as bc2
import Fitur_Lainnya as bc3


app = Flask(__name__)
app.secret_key = 'your_secret_key'


# session.clear()

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')


# Routes for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username, password)

        user = bc.verify_user_login(username, password)
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'username' not in session:
        return redirect(url_for('login'))
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# CRUD Routes
@app.route('/anggota_index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    flash("Session Active: " + session['username'] + "", "danger")
    employees = bc.read_all_user()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        status, message = bc.registrasi_user(name, password)
        if status: 
            flash('Anggota added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash(message, 'danger')
    return render_template('form.html', action='Add')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        print(name, password)

        id,current_name, passwd, id_buku, status_peminjaman = bc.read_a_user_by_id(id)
        
        # Update the employee in the database
        status , message = bc.update_user(id, current_name, name, password)
        if status:
            flash('Anggota updated successfully!'+message, 'success')
            # id, current_name, passwd, id_buku, status_peminjaman = bc.read_a_user_by_id(id)
            # flash(str(id) + current_name + passwd, 'success')
        else:
            flash(message, 'danger')
        return redirect(url_for('index'))
    else:
        employee = bc.read_a_user_by_id(id)
        return render_template('form.html', action='Edit', employee=employee)

@app.route('/delete/<int:id>')
def delete_employee(id):
    if 'username' not in session:
        return redirect(url_for('login'))

    # Delete the employee from the database
    status, message = bc.delete_user(id)
    if status:
        flash('Anggota deleted successfully!', 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('index'))


#BUKU PERPUS CRUD START HERE
@app.route('/buku_index', methods=['GET','POST'])
def buku_index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        search_query = request.form['search']

        buku = bc3.cari_buku(search_query)
    else:
        buku = bc2.baca_tabel_buku()
    return render_template('books_list.html',books=buku)


@app.route('/user/buku_index', methods=['GET', 'POST'])
def buku_index_user():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        search_query = request.form['search']
        
        buku = bc3.cari_buku(search_query)
    else:
        #QUERRY LIST BUKU
        buku = bc2.baca_tabel_buku()

    user_name = session['username']

    id, nama, password, id_buku_dipinjam, status_peminjaman = bc.read_a_user(user_name)

    buku_pinjam = bc2.baca_satu_buku_by_id(id_buku_dipinjam)


    return render_template('books_list_user.html',books=buku, buku_pinjam=buku_pinjam)


@app.route('/buku/add', methods=['GET', 'POST'])
def tambah_buku():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']
        tahun_terbit = request.form['tahun_terbit']
        deskripsi = request.form['deskripsi']

        status, pesan = bc2.daftar_buku(judul, penulis, penerbit, tahun_terbit, deskripsi)
        if status:
            flash('Buku berhasil ditambahkan!', 'success')
            return redirect(url_for('buku_index'))
        else:
            flash(pesan, 'danger')


    return render_template('add_book.html')

@app.route('/buku/edit/<int:id>', methods=['GET', 'POST'])
def edit_buku(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    buku = bc2.baca_satu_buku_by_id(id)

    if not buku:
        flash('Buku tidak ditemukan', 'danger')
        return redirect(url_for('buku_index'))

    if request.method == 'POST':
        judul_baru = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']
        tahun_terbit = request.form['tahun_terbit']
        deskripsi = request.form['deskripsi']

        status, pesan = bc2.update_buku(id, judul_baru, penulis, penerbit, tahun_terbit, deskripsi)

        if status:
            flash('Buku berhasil diupdate!', 'success')
            return redirect(url_for('buku_index'))
        else:
            flash(pesan, 'danger')

    return render_template('edit_books.html', book=buku)


@app.route('/buku/delete/<int:id>')
def delete_buku(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    status, pesan = bc2.delete_user(id)

    if status:
        flash('Buku berhasil dihapus!', 'success')
    else:
        flash(pesan, 'danger')
    
    return redirect(url_for('buku_index'))

@app.route('/buku/pinjam/<int:id_buku>')
def pinjam_buku(id_buku):
    if 'username' not in session:
        return redirect(url_for('login'))

    user_name = session['username']

    id_anggota, nama, password, id_buku_dipinjam, status_peminjaman = bc.read_a_user(user_name)

    status, pesan = bc3.pinjam_buku(id_anggota, id_buku)

    if status:
        flash('Buku berhasil dipinjam!', 'success')
    else:
        flash(pesan, 'danger')
    return redirect(url_for('buku_index_user'))

@app.route('/buku/kembalikan/<int:id_buku>')
def kembalikan_buku(id_buku):
    if 'username' not in session:
        return redirect(url_for('login'))
    user_name = session['username']
    id_anggota, nama, password, id_buku_dipinjam, status_peminjaman = bc.read_a_user(user_name)

    status, pesan = bc3.kembalikan_buku(id_anggota, id_buku)

    if status:
        flash('Buku berhasil dikembalikan!', 'success')
    else:
        flash(pesan, 'danger')
    return redirect(url_for('buku_index_user'))


if __name__ == '__main__':
    app.run(debug=True)