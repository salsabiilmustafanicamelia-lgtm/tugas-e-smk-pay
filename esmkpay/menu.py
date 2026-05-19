from .akun import AkunSiswa, AkunKantin
from .syarat import Menu_c
from .cetak_n_hitung import cetak_riwayat, hitung_saldo

akun_tersimpan_siswa = {}
akun_tersimpan_kantin = {}

class Menu(Menu_c):
    def menu(self):
        while True:
            print("\n===Menu E-SMK Pay===")
            print("1. Login akun siswa")
            print("2. Login akun kantin")
            print("3. Keluar")

            pilihan = input("Pilih Menu: ")
            
            match pilihan:
                case "1":
                    print("\n===Login Akun Siswa===")
                    nama = input("Nama Siswa: ")
                    kelas = input("Kelas: ")
                    password = input("Password: ")
                    if password != self._pass_siswa:
                        print("Password salah. Silakan coba lagi.")
                        continue
                    akun_siswa = AkunSiswa(nama, kelas, 0)
                    if nama + kelas not in akun_tersimpan_siswa:
                        akun_tersimpan_siswa[nama + kelas] = akun_siswa
                        print(f"\nLogin berhasil sebagai {nama} dari kelas {kelas}.")
                        menu = MenuAkunSiswa()
                        menu.menu(akun_siswa)
                    else:
                        print(f"\nLogin berhasil sebagai {nama} dari kelas {kelas}.")
                        menu = MenuAkunSiswa()
                        menu.menu(akun_tersimpan_siswa[nama + kelas])

                case "2":
                    print("\n===Login Akun Kantin===")
                    nama_toko = input("Nama Toko: ")
                    password = input("Password: ")
                    if password != self._pass_kantin:
                        print("Password salah. Silakan coba lagi.")
                        continue
                    kantin = AkunKantin(nama_toko, 0)
                    if nama_toko not in akun_tersimpan_kantin:
                        akun_tersimpan_kantin[nama_toko] = kantin
                        print(f"\nLogin berhasil sebagai {nama_toko}.")
                        menu = MenuAkunKantin()
                        menu.menu(kantin)
                    else:
                        print(f"\nLogin berhasil sebagai {nama_toko}.")
                        menu = MenuAkunKantin()
                        menu.menu(akun_tersimpan_kantin[nama_toko])
                
                case "3":
                    print("Terima kasih telah menggunakan E-SMK Pay. Sampai jumpa!")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
                    
class MenuAkunKantin(Menu_c):
    def menu(self, akun_kantin):
        while True:
            print("\n===Menu Akun Kantin===")
            print("1. Cek saldo")
            print("2. Deposit saldo")
            print("3. Riwayat transaksi")
            print("4. Hitung saldo")
            print("5. Logout")

            pilihan = input("Pilih Menu: ")
            
            match pilihan:
                case "1":
                    print(f"Saldo kantin saat ini: {akun_kantin.get_saldo()}")
                case "2":
                    jumlah = input("Masukkan jumlah deposit: ")
                    if jumlah.isdigit():
                        akun_kantin.set_saldo(int(jumlah))
                    else:
                        print("Jumlah deposit harus berupa angka.")
                case "3":
                    cetak_riwayat(akun_kantin)
                case "4":
                    hitung_saldo(akun_kantin)
                case "5":   
                    print("Logout berhasil. Kembali ke menu utama.")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

class MenuAkunSiswa(Menu_c):
    def menu(self, akun_siswa):
        while True:
            print("\n===Menu Akun Siswa===")
            print("1. Cek saldo")
            print("2. Deposit saldo")
            print("3. Bayar ke kantin")
            print("4. Riwayat transaksi")
            print("5. Hitung saldo")
            print("6. Logout")

            pilihan = input("Pilih Menu: ")
            
            match pilihan:
                case "1":
                    print(f"Saldo Anda saat ini: {akun_siswa.get_saldo()}")
                case "2":
                    jumlah = input("Masukkan jumlah deposit: ")
                    if jumlah.isdigit():
                        akun_siswa.set_saldo(int(jumlah))
                    else:
                        print("Jumlah deposit harus berupa angka.")
                case "3":
                    nama_kantin = input("Masukkan nama kantin: ")
                    self.bayar_kantin(akun_siswa, nama_kantin)
                case "4":
                    cetak_riwayat(akun_siswa)
                case "5":
                    hitung_saldo(akun_siswa)
                case "6":
                    print("Logout berhasil. Kembali ke menu utama.")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
                    
    def bayar_kantin(self, akun_siswa, nama_kantin):
        if nama_kantin not in akun_tersimpan_kantin:
            print("Akun kantin tidak ditemukan.")
            return
        akun_kantin = akun_tersimpan_kantin[nama_kantin]
        jumlah = input("Masukkan jumlah pembayaran: ")
        if jumlah.isdigit():
            akun_siswa.bayar(akun_kantin, int(jumlah))