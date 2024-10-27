# Meminta input tanggal lahir
tanggal_lahir = int(input("Masukkan tanggal lahir (angka 1-31): "))

# Membuat generator expression untuk bilangan kelipatan dari tanggal lahir
kelipatan_generator = (x for x in range(1000) if x % tanggal_lahir == 0)

# Menampilkan 10 data pertama menggunakan method next() dan looping
print("10 bilangan kelipatan pertama:")
for _ in range(10):
    print(next(kelipatan_generator))
