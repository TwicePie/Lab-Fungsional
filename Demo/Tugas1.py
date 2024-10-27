equipments = [
    ('Mouse', 'Fun Tek'),
    ('Monitor', 'Samsul'),
    ('Keyboard', 'Rexus'),
    ('Mouse', 'Lucitik'),
    ('Keyboard', 'Gamen'),
]

# Pure function for registering an account
def register(accounts, profiles, borrowings, friends, nim, password):
    if nim in accounts:
        return accounts, profiles, borrowings, friends, "NIM sudah terdaftar!"
    new_accounts = {**accounts, nim: password}
    new_profiles = {**profiles, nim: {}}
    new_borrowings = {**borrowings, nim: []}
    new_friends = {**friends, nim: []}
    return new_accounts, new_profiles, new_borrowings, new_friends, f"Registrasi berhasil untuk NIM: {nim}"

# Pure function for logging in
def login(accounts, profiles, nim, password):
    if nim in accounts and accounts[nim] == password:
        return True, f"Login berhasil, selamat datang {profiles[nim][0]}!"
    return False, "NIM atau password salah!"

# Pure function for updating profile
def update_profile(profiles, nim, name, semester, email):
    new_profiles = {**profiles, nim: (name, semester, email)}
    return new_profiles, "Profil berhasil disimpan!"

# Pure function for viewing profile
def view_profile(profiles, borrowings, nim):
    if nim in profiles:
        return profiles[nim], borrowings.get(nim, [])
    return None, []

# Pure function for borrowing equipment
def borrow_equipment(borrowings, nim, equipment_index):
    if nim not in borrowings:
        borrowings[nim] = []
    
    if 0 <= equipment_index < len(equipments):
        new_borrowings = {**borrowings, nim: borrowings[nim] + [equipments[equipment_index]]}
        return new_borrowings, f"Alat '{equipments[equipment_index][0]}' berhasil dipinjam!"
    return borrowings, "Pilihan tidak valid!"

# Pure function for returning borrowed equipment
def return_equipment(borrowings, nim, equipment_index):
    if nim in borrowings and 0 <= equipment_index < len(borrowings[nim]):
        new_borrowings = {**borrowings, nim: borrowings[nim][:equipment_index] + borrowings[nim][equipment_index + 1:]}
        return new_borrowings, f"Alat berhasil dikembalikan!"
    return borrowings, "Pilihan tidak valid!"

# Pure function for adding friends
def add_friend(friends, profiles, nim, friend_nim):
    if friend_nim == nim:
        return friends, "Anda tidak bisa menambahkan diri sendiri sebagai teman!"
    if friend_nim in profiles:
        if friend_nim not in friends[nim]:
            new_friends = {**friends, nim: friends[nim] + [friend_nim]}
            return new_friends, f"Teman dengan NIM {friend_nim} berhasil ditambahkan!"
        return friends, "Teman sudah ada di daftar teman!"
    return friends, "NIM teman tidak ditemukan!"

# Pure function for viewing friends
def view_friends(friends, profiles, nim):
    if nim not in friends:
        return []
    return [(friend_nim, profiles[friend_nim][0]) for friend_nim in friends[nim]]

# Main interaction loop (imperative due to input/output handling)
def main():
    accounts, profiles, borrowings, friends = {}, {}, {}, {}
    
    while True:
        print("\n=== Menu Utama ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            accounts, profiles, borrowings, friends, message = register(accounts, profiles, borrowings, friends, nim, password)
            print(message)
            if "berhasil" in message:
                name = input("Masukkan nama: ")
                semester = input("Masukkan semester: ")
                email = input("Masukkan email: ")
                profiles, _ = update_profile(profiles, nim, name, semester, email)

        elif choice == '2':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            success, message = login(accounts, profiles, nim, password)
            print(message)
            if success:
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
                        profile, borrowed = view_profile(profiles, borrowings, nim)
                        if profile:
                            print(f"Nama: {profile[0]}, Semester: {profile[1]}, Email: {profile[2]}")
                            print("Alat yang dipinjam:", borrowed)
                        else:
                            print("Profil tidak ditemukan.")
                    elif choice == '2':
                        print("\n")
                        for idx, equipment in enumerate(equipments):
                            print(f"{idx + 1}. {equipment[0]} by {equipment[1]}")
                        equipment_index = int(input("Pilih nomor alat yang ingin dipinjam: ")) - 1
                        borrowings, message = borrow_equipment(borrowings, nim, equipment_index)
                        print(message)
                    elif choice == '3':
                        _, borrowed = view_profile(profiles, borrowings, nim)
                        print("Alat yang dipinjam:", borrowed)
                    elif choice == '4':
                        name = input("Nama baru: ")
                        semester = input("Semester baru: ")
                        email = input("Email baru: ")
                        profiles, _ = update_profile(profiles, nim, name, semester, email)
                    elif choice == '5':
                        for idx, equipment in enumerate(borrowings[nim]):
                            print(f"{idx + 1}. {equipment[0]} by {equipment[1]}")
                        equipment_index = int(input("Pilih nomor alat yang ingin dikembalikan: ")) - 1
                        borrowings, message = return_equipment(borrowings, nim, equipment_index)
                        print(message)
                    elif choice == '6':
                        friend_nim = input("Masukkan NIM teman: ")
                        friends, message = add_friend(friends, profiles, nim, friend_nim)
                        print(message)
                    elif choice == '7':
                        friend_list = view_friends(friends, profiles, nim)
                        if friend_list:
                            for idx, friend in enumerate(friend_list):
                                print(f"{idx + 1}. {friend[1]} ({friend[0]})")
                        else:
                            print("Belum ada teman.")
                    elif choice == '8':
                        print("Logout berhasil.")
                        break
        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Run the program
main()
