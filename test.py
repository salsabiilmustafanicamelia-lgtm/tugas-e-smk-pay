from akun import AkunSiswa, AkunKantin
from cetak_n_hitung import cetak_riwayat, hitung_saldo
from menu import main, menu_akun_siswa, menu_akun_kantin

siswa = AkunSiswa("Budi", "10A", 50000)
kantin = AkunKantin("Kantin SMK", 100000)

print(siswa.get_saldo())
siswa.set_saldo(20000)
print(siswa.get_saldo())

siswa.bayar(kantin, 15000)
print(siswa.get_saldo())

print(kantin.get_saldo())

print(siswa._riwayat)
print(kantin._riwayat)

cetak_riwayat(siswa)
cetak_riwayat(kantin)

hitung_saldo(siswa)
hitung_saldo(kantin)