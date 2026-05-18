from akun import AkunSiswa, AkunKantin
from syarat import Menu_c
from cetak_n_hitung import cetak_riwayat

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
                    print(f"\nLogin berhasil sebagai {nama} dari kelas {kelas}.")
                    MenuAkunSiswa().menu_akun(akun_siswa)
                    
                case "2":
                    print("\n===Login Akun Kantin===")
                    nama_toko = input("Nama Toko: ")
                    password = input("Password: ")
                    if password != self._pass_kantin:
                        print("Password salah. Silakan coba lagi.")
                        continue
                    kantin = AkunKantin(nama_toko, 0)
                    MenuAkunKantin().menu_akun(kantin)
                
                case "3":
                    print("Terima kasih telah menggunakan E-SMK Pay. Sampai jumpa!")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
                    
class MenuAkunKantin(Menu_c):
    def menu_akun(self, akun_kantin):
        while True:
            print("\n===Menu Akun Kantin===")
            print("1. Cek saldo")
            print("2. Riwayat transaksi")
            print("3. Logout")

            pilihan = input("Pilih Menu: ")
            
            match pilihan:
                case "1":
                    print(f"Saldo kantin saat ini: {akun_kantin.get_saldo()}")
                case "2":
                    cetak_riwayat(akun_kantin)
                case "3":
                    print("Logout berhasil. Kembali ke menu utama.")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

class MenuAkunSiswa(Menu_c):
    def menu_akun(self, akun_siswa):
        while True:
            print("\n===Menu Akun Siswa===")
            print("1. Cek saldo")
            print("2. Deposit saldo")
            print("3. Bayar ke kantin")
            print("4. Riwayat transaksi")
            print("5. Logout")

            pilihan = input("Pilih Menu: ")
            
            match pilihan:
                case "1":
                    print(f"Saldo Anda saat ini: {akun_siswa.get_saldo()}")
                case "2":
                    jumlah = int(input("Masukkan jumlah deposit: "))
                    akun_siswa.set_saldo(jumlah)
                case "3":
                    kantin = input("Masukkan nama kantin: ")
                    self.bayar_kantin(akun_siswa, kantin)
                case "4":
                    cetak_riwayat(akun_siswa)
                case "5":
                    print("Logout berhasil. Kembali ke menu utama.")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
                    
    def bayar_kantin(self, akun_siswa, akun_kantin):
        jumlah = int(input("Masukkan jumlah pembayaran: "))
        akun_siswa.bayar(akun_kantin, jumlah)
    
# def main():
#     while True:
#         print("\n===Menu E-SMK Pay===")
#         print("1. Login akun siswa")
#         print("2. Login akun kantin")
#         print("3. Keluar")

#         pilihan = input("Pilih Menu: ")
        
#         match pilihan:
#             case "1":
#                 print("\n===Login Akun Siswa===")
#                 nama = input("Nama Siswa: ")
#                 kelas = input("Kelas: ")
#                 akun_siswa = AkunSiswa(nama, kelas, 0)
#                 menu_akun_siswa (akun_siswa, kantin)
#                 print(f"\nLogin berhasil sebagai {nama} dari kelas {kelas}.")

#             case "2":
#                 menu_akun_kantin(kantin)
            
#             case "3":
#                 print("Terima kasih telah menggunakan E-SMK Pay. Sampai jumpa!")
#                 break
#             case _:
#                 print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# def menu_akun_siswa(akun_siswa, akun_kantin):
#     while True:
#         print("\n===Menu Akun Siswa===")
#         print("1. Cek saldo")
#         print("2. Deposit saldo")
#         print("3. Bayar ke kantin")
#         print("4. Riwayat transaksi")
#         print("5. Logout")

#         pilihan = input("Pilih Menu: ")
        
#         match pilihan:
#             case "1":
#                 print(f"Saldo Anda saat ini: {akun_siswa.get_saldo()}")
#             case "2":
#                 jumlah = int(input("Masukkan jumlah deposit: "))
#                 akun_siswa.set_saldo(jumlah)
#             case "3":
#                 jumlah = int(input("Masukkan jumlah pembayaran: "))
#                 akun_siswa.bayar(akun_kantin, jumlah)
#             case "4":
#                 cetak_riwayat(akun_siswa)
#             case "5":
#                 print("Logout berhasil. Kembali ke menu utama.")
#                 break
#             case _:
#                 print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# def menu_akun_kantin(akun_kantin):
#     while True:
#         print("\n===Menu Akun Kantin===")
#         print("1. Cek saldo")
#         print("2. Riwayat transaksi")
#         print("3. Logout")

#         pilihan = input("Pilih Menu: ")
        
#         match pilihan:
#             case "1":
#                 print(f"Saldo kantin saat ini: {akun_kantin.get_saldo()}")
#             case "2":
#                 cetak_riwayat(akun_kantin)
#             case "3":
#                 print("Logout berhasil. Kembali ke menu utama.")
#                 break
#             case _:
#                 print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")