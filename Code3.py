#TO_DO 1
# HANYA CONTOH, silahkan dimodif
nilai_mahasiswa = {
    "Rawr": {"Matematika": 85, "Fisika": 90, "Kimia": 80},
    "Gendang": {"Matematika": 75, "Fisika": 80, "Kimia": 70},
    "Lestari": {"Matematika": 95, "Fisika": 85, "Kimia": 90},
    "IshowSpeed": {"Matematika": 60, "Fisika": 65, "Kimia": 70},
    "MasukPak": {"Matematika": 70, "Fisika": 75, "Kimia": 80}
}

#TO_DO 2
def rata_rata_mahasiswa(nilai_mahasiswa):
    rata_rata_setiap_mahasiswa = {}
    for mahasiswa, nilai in nilai_mahasiswa.items():
        total_nilai = sum(nilai.values())
        jumlah_mata_kuliah = len(nilai)
        rata_rata = total_nilai / jumlah_mata_kuliah
        rata_rata_setiap_mahasiswa[mahasiswa] = rata_rata
    return rata_rata_setiap_mahasiswa

#TO_DO 3
def rata_rata_seluruh_mahasiswa(nilai_mahasiswa):
    total_nilai = 0
    total_mata_kuliah = 0
    for nilai in nilai_mahasiswa.values():
        total_nilai += sum(nilai.values())
        total_mata_kuliah += len(nilai)
    rata_rata = total_nilai / total_mata_kuliah
    return rata_rata


#panggil fungsi dan tampilkan hasilnya
rata_rata_per_mahasiswa = rata_rata_mahasiswa(nilai_mahasiswa)
print("Rata-rata nilai setiap mahasiswa:")
for mahasiswa, rata_rata in rata_rata_per_mahasiswa.items():
    print(f"{mahasiswa}: {rata_rata:.2f}")

rata_rata_semua_mahasiswa = rata_rata_seluruh_mahasiswa(nilai_mahasiswa)
print("\nRata-rata nilai seluruh mahasiswa: {:.2f}".format(rata_rata_semua_mahasiswa))
