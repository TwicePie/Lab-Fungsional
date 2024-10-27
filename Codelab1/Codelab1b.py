# Data nilai awal
nilai = [
    {'matkul': 'fungsional', 'nilai': 95},
    {'matkul': 'Mobile', 'nilai': 55}
]

# Pure Function untuk menambah nilai
def tambah_nilai(nama_matkul, jumlah_nilai, nilai_list):
    nilai_baru = []  # Membuat salinan daftar nilai
    found = False  # Menandai apakah matkul ditemukan
    
    for item in nilai_list:
        if item['matkul'] == nama_matkul:
            # Menambah nilai dan memasukkan ke dalam nilai_baru
            nilai_baru.append({'matkul': item['matkul'], 'nilai': item['nilai'] + jumlah_nilai})
            found = True
        else:
            nilai_baru.append(item)  # Tidak diubah jika matkul tidak cocok
    
    if not found:
        print(f"Matkul {nama_matkul} belum terdaftar.")
    
    return nilai_baru

# Fungsi generator untuk mencetak data nilai
def cetak_nilai(nilai_list):
    for item in nilai_list:
        yield f"Matkul: {item['matkul']}, Nilai: {item['nilai']}"

# Cek nilai awal
print("Nilai awal:")
for data in cetak_nilai(nilai):
    print(data)

# Menambahkan nilai ke dalam daftar menggunakan pure function
nilai_baru = tambah_nilai('Mobile', 15, nilai)

# Cek nilai setelah update
print("\nNilai setelah update:")
for data in cetak_nilai(nilai_baru):
    print(data)
