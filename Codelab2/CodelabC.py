data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

# TO-DO 1: deklarasi fungsi generator
def nilai_ganjil(data):
    # TO-DO 2: isi fungsi
    for mahasiswa in data:
        nilai = mahasiswa['nilai']
        if nilai % 2 != 0:  # Mengecek apakah nilai ganjil
            yield nilai  # TO-DO 3: output fungsi

# TO-DO 4: panggil fungsi generator untuk membuat generator object yang berisi
# data mahasiswa dengan nilai ganjil
var = nilai_ganjil(data_mahasiswa)

# TO-DO 5: menampilkan/print hasil dari generator object
print("Nilai ganjil dari mahasiswa:")
for nilai in var:
    print(nilai)
