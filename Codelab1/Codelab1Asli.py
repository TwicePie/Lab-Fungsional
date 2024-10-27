nilai = [
    {'matkul': 'Fungsional', 'nilai': 95},
    {'matkul': 'Mobile', 'nilai': 55}
]

def tambah_nilai(nama_matkul, jumlah_nilai, nilai_list):
    # Membuat salinan dari daftar nilai untuk menghindari pengaruh pada global state
    nilai_baru = []
    found = False  # Menandai apakah mata kuliah ditemukan

    for item in nilai_list:
        if item['matkul'] == nama_matkul:
            # Jika mata kuliah ditemukan, tambahkan nilai
            nilai_baru.append({'matkul': item['matkul'], 'nilai': item['nilai'] + jumlah_nilai})
            found = True
        else:
            # Jika mata kuliah tidak ditemukan, masukkan item tanpa perubahan
            nilai_baru.append(item)

    if not found:
        print(f"Mata kuliah {nama_matkul} tidak ditemukan dalam daftar!")

    return nilai_baru

# Panggil fungsi tambah_nilai
nilai_baru = tambah_nilai('Mobile', 15, nilai)

# Cek nilai awal
print("Nilai awal: ", nilai)

# Cek nilai hasil tambah_nilai
print("Nilai update: ", nilai_baru)
