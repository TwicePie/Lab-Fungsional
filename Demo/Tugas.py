accounts = {}   
profiles = {}   
borrowings = {} 
friends = {}
equipments = [
    ('Mouse', 'Fun Tek'),
    ('Monitor', 'Samsul'),
    ('Keyboard', 'Rexus'),
    ('Mouse', 'Lucitik'),
    ('Keyboard', 'Gamen'),
] 

# Function register
def register(nim, password):
    if nim in accounts:
        print("NIM sudah terdaftar!")
    else:
        accounts[nim] = password
        profiles[nim] = {}  
        borrowings[nim] = [] 
        friends[nim] = [] 
        print(f"Registrasi berhasil untuk NIM: {nim}")
        biodata_menu(nim)

# Function login
def login(nim, password):
    if nim in accounts and accounts[nim] == password:
        print(f"Login berhasil, selamat datang {profiles[nim][0]}!")
        user_menu(nim)
    else:
        print("NIM atau password salah!")

# Biodata menu
def biodata_menu(nim):
    print("Isi biodata profil:")
    name = input("Masukkan nama: ")
    semester = input("Masukkan semester: ")
    email = input("Masukkan email: ")
    
    profiles[nim] = (name, semester, email)
    print("Profil berhasil disimpan!")

# Function for user menu
def user_menu(nim):
    while True:
        print("\n=== User Menu ===")
        print("1. Lihat profil")
        print("2. Pinjam alat lab")
        print("3. Lihat alat yang dipinjam")
        print("4. Edit profil")
        print("5. Kembalikan alat lab")
        print("6. Tambah teman")
        print("7. Lihat daftar teman")
        print("8. Logout")
        choice = input("Pilih opsi: ")

        if choice == '1':
            lihat_profil(nim)
        elif choice == '2':
            pinjam_alat(nim)
        elif choice == '3':
            lihat_alat_pinjam(nim)
        elif choice == '4':
            edit_profil(nim)
        elif choice == '5':
            kembalikan_alat(nim)
        elif choice == '6':
            tambah_teman(nim)
        elif choice == '7':
            lihat_teman(nim)
        elif choice == '8':
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

# Function profile
def lihat_profil(nim):
    if nim in profiles:
        print(f"\nProfil {nim}:")
        print(f"Nama: {profiles[nim][0]}")
        print(f"Semester: {profiles[nim][1]}")
        print(f"Email: {profiles[nim][2]}")
        lihat_alat_pinjam(nim)
    else:
        print("Profil tidak ditemukan!")

# Function pinjam
def pinjam_alat(nim):
    print("\n=== Daftar Alat Lab yang Tersedia ===")
    for idx, equipment in enumerate(equipments):
        print(f"{idx + 1}. {equipment[0]} by {equipment[1]}")
    
    choice = int(input("Pilih nomor alat yang ingin dipinjam: ")) - 1
    if 0 <= choice < len(equipments):
        borrowings[nim].append(equipments[choice])
        print(f"Alat '{equipments[choice][0]}' berhasil dipinjam!")
    else:
        print("Pilihan tidak valid!")

# Function barang dipinjam
def lihat_alat_pinjam(nim):
    if borrowings[nim]:
        print("\nAlat yang sedang dipinjam:")
        for idx, equipment in enumerate(borrowings[nim]):
            print(f"{idx + 1}. {equipment[0]} by {equipment[1]}")
    else:
        print("Belum ada alat yang dipinjam.")

# Function mengemballikan barang
def kembalikan_alat(nim):
    if borrowings[nim]:
        print("\n=== Daftar Alat yang Dipinjam ===")
        for idx, equipment in enumerate(borrowings[nim]):
            print(f"{idx + 1}. {equipment[0]} by {equipment[1]}")
        
        choice = int(input("Pilih nomor alat yang ingin dikembalikan: ")) - 1
        if 0 <= choice < len(borrowings[nim]):
            returned_equipment = borrowings[nim].pop(choice)
            print(f"Alat '{returned_equipment[0]}' berhasil dikembalikan!")
        else:
            print("Pilihan tidak valid!")
    else:
        print("Tidak ada alat yang dipinjam.")

# Function edit profile
def edit_profil(nim):
    print("\nEdit Profil:")
    name = input(f"Nama baru (saat ini: {profiles[nim][0]}): ")
    semester = input(f"Semester baru (saat ini: {profiles[nim][1]}): ")
    email = input(f"Email baru (saat ini: {profiles[nim][2]}): ")
    
    profiles[nim] = (
        name if name else profiles[nim][0],
        semester if semester else profiles[nim][1],
        email if email else profiles[nim][2]
    )
    
    print("Profil berhasil diperbarui!")

# Function tambah teman
def tambah_teman(nim):
    teman_nim = input("Masukkan NIM teman yang ingin ditambahkan: ")
    
    if teman_nim == nim:
        print("Anda tidak bisa menambahkan diri sendiri sebagai teman!")
    elif teman_nim in profiles:
        if teman_nim not in friends[nim]:
            friends[nim].append(teman_nim)
            print(f"Teman dengan NIM {teman_nim} berhasil ditambahkan!")
        else:
            print("Teman sudah ada di daftar teman!")
    else:
        print("NIM teman tidak ditemukan!")

# Function liat list teman
def lihat_teman(nim):
    if nim not in friends:
        friends[nim] = []  

    if friends[nim]:  
        print("\nDaftar Teman:")
        for idx, teman_nim in enumerate(friends[nim]):
            print(f"{idx + 1}. {teman_nim} - {profiles[teman_nim][0]}")
    else:
        print("Belum ada teman yang ditambahkan.")

# Main program
def main():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            register(nim, password)
        elif choice == '2':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            login(nim, password)
        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Main program
main()
