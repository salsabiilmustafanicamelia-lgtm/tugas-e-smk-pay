from esmkpay.akun import AkunSiswa, AkunKantin

def cetak_riwayat(akun):
    print(f"Riwayat transaksi untuk {akun.nama}:")
    no = 1
    for transaksi in akun._riwayat:
        print(f"{no}. {transaksi}")
        no += 1

def hitung_saldo(akun):
    print(f"Hitungan Saldo untuk {akun.nama}:")
    for i in akun.list_transaksi:
        print(f"{i}")
    print("-------------------------")
    print(f" \t{akun.get_saldo()}")