from functools import reduce

nilai_mahasiswa = {
    'Zaidun' : 99,
    'Suwarsono' : 100,
    'Dedi' : 75,
    'Mamat' : 88,
    'Joko' : 40,
    'Rusdi' : 78,
    'Diki' : 100,
    'Ansori' : 92,
    'Andri' : 76,
    'Kahfi' : 58,
    'Edi' : 77,
    'Joko' : 15,
    'Sutadi' : 90,
    'Made' : 55,
    'Nyoto' : 88,
    'Widodo' : 100
}

total_nilai = reduce(lambda total, nilai : total + nilai, nilai_mahasiswa.values(), 0)
nilai_tertinggi = max(nilai_mahasiswa.values())
mahasiswa_lulus = list(filter(lambda nilai : nilai_mahasiswa[nilai] >= 75, nilai_mahasiswa))# mahasiswa lulus kkm = 75
# # tambah 5 poin untuk mahasiswa yang di bawah 75
nilai_mahasiswa_update = dict(map(lambda nilai : (nilai[0], nilai[1] + 5 if nilai[1] < 75 else nilai[1]), nilai_mahasiswa.items())) # lanjutkan hintnya

# tampilkan nilai
print(total_nilai)
print(nilai_tertinggi)
print(mahasiswa_lulus)
print(nilai_mahasiswa_update)
