data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

def rata_rata(data):
    total_nilai = sum(mahasiswa['nilai'] for mahasiswa in data)
    jumlah_mahasiswa = len(data)
    return total_nilai / jumlah_mahasiswa

# Menghitung nilai rata-rata
nilai_rata_rata = rata_rata(data_mahasiswa)
print(f"Nilai rata-rata: {nilai_rata_rata}")