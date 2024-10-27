nilai = [
    {'matkul': 'fungsional', 'nilai': 95},
    {'matkul': 'Mobile', 'nilai': 55}
]

def tambah_nilai(nama_matkul, jumlah_nilai):
    nilai 
    found = False
    for item in nilai:
        if item['matkul'] == nama_matkul:
            item['nilai'] += jumlah_nilai
            print(f"Nilai {nama_matkul} ditambahkan {jumlah_nilai}.\nTotal nilai {nama_matkul} saat ini {item['nilai']}")
            found = True
            break
    if not found:
        print(f"Matkul {nama_matkul} belum terdaftar.")

# cek nilai awal
nilai_lama = [{ 'matkul': item['matkul'], 'nilai': item['nilai']} for item in nilai]
print("Nilai awal: ", nilai_lama)

# Menambahkan nilai ke dalam daftar ke dalam daftar
tambah_nilai('Mobile', 15)

# cek nilai saat ini
print("Nilai asli: ", nilai_lama)
print("Nilai update: ", nilai)