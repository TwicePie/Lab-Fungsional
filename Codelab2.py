from functools import reduce

# Data buku
books = [
    {'judul': 'Pulang', 'penulis': 'Tere Liye', 'halaman': 400},
    {'judul': 'Kapan Hujan?', 'penulis': 'Ziggy Z.', 'halaman': 142},
    {'judul': 'Manusia Alam', 'penulis': 'Leila S. Chudori', 'halaman': 448},
    {'judul': 'Origin', 'penulis': 'Dan Brown', 'halaman': 511},
    {'judul': 'Rahasia Pelangi', 'penulis': 'Ruwi Meita', 'halaman': 288},
    {'judul': 'Kubah', 'penulis': 'Ahmad Tohari', 'halaman': 184},
    {'judul': 'Dompet Ayah Sepatu Ibu', 'penulis': 'J. S. Khairen', 'halaman': 210}
]

# 1. Fungsi book_filter untuk menyaring buku yang judulnya diawali dengan huruf 'K'
filtered_books = list(filter(lambda book : book['judul'].startswith('K'), books))
# def book_filter():
#     filtered_books = [book for book in books if book['judul'].startswith('K')]
print("Daftar buku yang judulnya diawali dengan huruf 'K':")
for book in filtered_books:
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")

# 2. Fungsi untuk mengambil daftar judul buku menggunakan map()
judul_buku_list = list(map(lambda book : book['judul'], books))
# def judul_buku(book):
#     return book['judul']

# def daftar_judul_buku():
#     judul_buku_list = list(map(judul_buku, books))
print("\nDaftar judul buku:")
for judul in judul_buku_list:
    print(judul)

# 3. Fungsi untuk menyaring buku dengan halaman lebih dari 200 menggunakan filter()
books_200 = list(filter(lambda book : book['halaman'] > 200, books))
# def lebih_200(book):
#     return book['halaman'] > 200

# def buku_lebih_200_halaman():
#     books_200 = list(filter(lebih_200, books))
print("\nDaftar buku dengan lebih dari 200 halaman:")
for book in books_200:
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")

# 4. Fungsi untuk menghitung total halaman semua buku menggunakan reduce()
total_halaman = reduce(lambda total, book : total + book['halaman'], books, 0)
# def hitung_halaman(total, book):
#     return total + book['halaman']

# def total_halaman_buku():
#     total_halaman = reduce(hitung_halaman, books, 0)
print(f"\nTotal jumlah halaman semua buku: {total_halaman}")

# Menjalankan semua fungsi

# book_filter()
# daftar_judul_buku()
# buku_lebih_200_halaman()
# total_halaman_buku()
