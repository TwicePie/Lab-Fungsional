data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

def kelulusan(data):
    return [
        {**mahasiswa, 'nilai': 'sempurna' if mahasiswa['nilai'] >= 85 else 'memenuhi' if mahasiswa['nilai'] >= 60 else 'gagal'}
        for mahasiswa in data
    ]

# Mengubah nilai menjadi kategori kelulusan
data_kelulusan = kelulusan(data_mahasiswa)
print(data_kelulusan)
