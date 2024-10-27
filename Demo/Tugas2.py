# Data reservasi hotel
data_penginapan = [
    {"room_id": "GJ101", "customer_name": "Karina Aespa", "expenses": 1000, "jumlah_orang": 2, "tanggal_menginap": "2024-10-10"},
    {"room_id": "GJ102", "customer_name": "Wonyoung Ive", "expenses": 1200, "jumlah_orang": 3, "tanggal_menginap": "2024-10-10"},
    {"room_id": "GJ103", "customer_name": "Winter Aespa", "expenses": 800, "jumlah_orang": 1, "tanggal_menginap": "2024-10-10"},
    {"room_id": "GJ104", "customer_name": "Bob Marley", "expenses": 950, "jumlah_orang": 4, "tanggal_menginap": "2024-10-10"},
    {"room_id": "GJ201", "customer_name": "Sakura Lleserafim", "expenses": 1500, "jumlah_orang": 2, "tanggal_menginap": "2024-10-11"},
    {"room_id": "GJ202", "customer_name": "Pak diddy", "expenses": 1100, "jumlah_orang": 2, "tanggal_menginap": "2024-10-11"},
    {"room_id": "GJ203", "customer_name": "Fufu Fafa", "expenses": 1300, "jumlah_orang": 1, "tanggal_menginap": "2024-10-11"},
    {"room_id": "GJ204", "customer_name": "Thomas Slebew", "expenses": 1400, "jumlah_orang": 3, "tanggal_menginap": "2024-10-11"},
    {"room_id": "GJ301", "customer_name": "Mamat Skibidi", "expenses": 1700, "jumlah_orang": 2, "tanggal_menginap": "2024-10-12"},
    {"room_id": "GJ302", "customer_name": "Eka Sigma", "expenses": 900, "jumlah_orang": 1, "tanggal_menginap": "2024-10-12"},
    {"room_id": "GJ303", "customer_name": "Farriel Rizz", "expenses": 800, "jumlah_orang": 4, "tanggal_menginap": "2024-10-12"},
    {"room_id": "GJ304", "customer_name": "Nizam Rauls", "expenses": 950, "jumlah_orang": 3, "tanggal_menginap": "2024-10-12"}
]

# Fungsi cari_customer: Mencari customer berdasarkan nama dan menghitung total tagihan
def cari_customer(data_penginapan, nama):
    hasil = [data for data in data_penginapan if data['customer_name'].lower() == nama.lower()]
    if not hasil:
        return f"Customer dengan nama '{nama}' tidak ditemukan."
    else:
        total_tagihan = sum(data['expenses'] for data in hasil)
        for data in hasil:
            print(f"ID Kamar: {data['room_id']}")
            print(f"Nama: {data['customer_name']}")
            print(f"Tagihan: {data['expenses']}")
            print(f"Jumlah Orang: {data['jumlah_orang']}")
            print(f"Tanggal: {data['tanggal_menginap']}")
        print(f"Total Tagihan: {total_tagihan}")
        print("------------------------")

# Fungsi rata_rata_menginap: Generator untuk menghitung rata-rata jumlah orang yang menginap tiap hari
def rata_rata_menginap(data_penginapan):
    tanggal_group = {}
    for data in data_penginapan:
        tanggal = data['tanggal_menginap']
        if tanggal not in tanggal_group:
            tanggal_group[tanggal] = []
        tanggal_group[tanggal].append(data['jumlah_orang'])

    for tanggal, jumlah_orang in tanggal_group.items():
        yield tanggal, sum(jumlah_orang) / len(jumlah_orang)

# Fungsi total_pendapatan: Menghitung total pendapatan dan jumlah customer per tanggal
def total_pendapatan(data_penginapan):
    tanggal_group = {}
    for data in data_penginapan:
        tanggal = data['tanggal_menginap']
        if tanggal not in tanggal_group:
            tanggal_group[tanggal] = []
        tanggal_group[tanggal].append(data['expenses'])

    hasil = [{"tanggal": tanggal, "jumlah_customer": len(expenses), "total_pendapatan": sum(expenses)}
             for tanggal, expenses in tanggal_group.items()]
    
    return hasil

# Fungsi main untuk menjalankan program berdasarkan pilihan user
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Cari customer dan hitung total tagihan")
        print("2. Hitung rata-rata jumlah orang yang menginap tiap hari")
        print("3. Hitung total pendapatan per tanggal")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            nama_customer = input("Masukkan nama customer: ")
            hasil = cari_customer(data_penginapan, nama_customer)
            print(hasil)
        
        elif pilihan == '2':
            print("\nRata-rata jumlah orang yang menginap tiap hari:")
            for tanggal, rata2 in rata_rata_menginap(data_penginapan):
                print(f"{tanggal}: {rata2} orang")
        
        elif pilihan == '3':
            print("\nTotal pendapatan per tanggal:")
            pendapatan_per_tanggal = total_pendapatan(data_penginapan)
            for data in pendapatan_per_tanggal:
                print(f"Tanggal: {data['tanggal']}, Jumlah Customer: {data['jumlah_customer']}, Total Pendapatan: {data['total_pendapatan']}")
        
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Panggil fungsi main untuk menjalankan program
main()
