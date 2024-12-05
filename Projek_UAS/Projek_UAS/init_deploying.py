import os
import Anggota_Perpus_CRUD as bc
import Buku_Perpus_CRUD as bc2

os.system("python create_table.py")

bc.registrasi_user('user1', 'password1')
bc.registrasi_user('user2', 'password2')
bc.registrasi_user('user3', 'password3')

bc2.daftar_buku("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "1960", "A novel about racial injustice in the Deep South.")
bc2.daftar_buku("1984", "George Orwell", "Secker & Warburg", "1949", "A dystopian story set in a totalitarian society under constant surveillance.")
bc2.daftar_buku("Moby Dick", "Herman Melville", "Harper & Brothers", "1851", "An epic tale of the voyage of the whaling ship Pequod.")
bc2.daftar_buku("Pride and Prejudice", "Jane Austen", "T. Egerton", "1813", "A romantic novel about manners and matrimonial machinations.")
bc2.daftar_buku("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", "1925", "A critique of the American Dream during the Jazz Age.")
bc2.daftar_buku("War and Peace", "Leo Tolstoy", "The Russian Messenger", "1869", "A historical novel that intertwines the lives of several characters during the Napoleonic Wars.")
bc2.daftar_buku("The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company", "1951", "A story about teenage alienation and rebellion.")
bc2.daftar_buku("The Hobbit", "J.R.R. Tolkien", "George Allen & Unwin", "1937", "A fantasy adventure story about the journey of Bilbo Baggins.")
bc2.daftar_buku("Ulysses", "James Joyce", "Sylvia Beach", "1922", "A complex modernist novel set in Dublin, recounting the events of a single day.")
bc2.daftar_buku("Crime and Punishment", "Fyodor Dostoevsky", "The Russian Messenger", "1866", "A psychological drama that explores the morality of crime and redemption.")
bc2.daftar_buku("The Odyssey", "Homer", "Ancient Greece", "8th Century BC", "An epic poem about Odysseus' adventures on his journey home after the Trojan War.")
bc2.daftar_buku("Brave New World", "Aldous Huxley", "Chatto & Windus", "1932", "A dystopian novel exploring the dangers of a technologically advanced society.")
bc2.daftar_buku("The Divine Comedy", "Dante Alighieri", "Italy", "14th Century", "An epic poem depicting the journey through Hell, Purgatory, and Paradise.")
bc2.daftar_buku("Les Misérables", "Victor Hugo", "A. Lacroix, Verboeckhoven & Cie", "1862", "A story of redemption and revolution in 19th-century France.")
bc2.daftar_buku("The Brothers Karamazov", "Fyodor Dostoevsky", "The Russian Messenger", "1880", "A philosophical novel that delves into faith, free will, and moral struggles.")
bc2.daftar_buku("One Hundred Years of Solitude", "Gabriel García Márquez", "Harper & Row", "1967", "A multi-generational story that portrays the magical realism of Latin America.")
