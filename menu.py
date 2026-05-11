from akun import AkunSiswa, AkunKantin

def main():
    while True:
        print("\n===Menu E-SMK Pay===")
        print("1. Login akun siswa")
        print("2. Login akun kantin")
        print("3. Keluar")

        pilihan = input("Pilih Menu: ")
        
        match pilihan:
            case "1":
                print("\n===Login Akun Siswa===")
                nama = input("Masukkan nama siswa: ")
                kelas = input("Masukkan kelas siswa: ")
                print(f"\nLogin berhasil sebagai {nama} dari kelas {kelas}.")

            case "2":
                print("\n===Login Akun Kantin===")
                nama_toko = input("Masukkan nama toko: ")
                print(f"\nLogin berhasil sebagai {nama_toko}.")
            
            case "3":
                print("Terima kasih telah menggunakan E-SMK Pay. Sampai jumpa!")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

def menu_akun_siswa(akun_siswa, akun_kantin):
    while True:
        print("\n===Menu Akun Siswa===")
        print("1. Cek saldo")
        print("2. Deposit saldo")
        print("3. Bayar ke kantin")
        print("4. Keluar")

        pilihan = input("Pilih Menu: ")
        
        match pilihan:
            case "1":
                print(f"Saldo Anda saat ini: {akun_siswa.get_saldo()}")
            case "2":
                jumlah = int(input("Masukkan jumlah deposit: "))
                akun_siswa.set_saldo(jumlah)
            case "3":
                jumlah = int(input("Masukkan jumlah pembayaran: "))
                akun_siswa.bayar(akun_kantin, jumlah)
            case "4":
                print("Kembali ke menu utama.")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

def menu_akun_kantin(akun_kantin):
    while True:
        print("\n===Menu Akun Kantin===")
        print("1. Cek saldo")
        print("2. Keluar")

        pilihan = input("Pilih Menu: ")
        
        match pilihan:
            case "1":
                print(f"Saldo kantin saat ini: {akun_kantin.get_saldo()}")
            case "2":
                print("Kembali ke menu utama.")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

