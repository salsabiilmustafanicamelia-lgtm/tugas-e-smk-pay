from akun import AkunSiswa, AkunKantin

def cetak_riwayat(akun):
    print(f"Riwayat transaksi untuk {akun.nama}:")
    for transaksi in akun._riwayat:
        print(transaksi)
        
def hitung_saldo(akun):
    print(f"Hitungan Saldo untuk {akun.nama}:")
    saldo = akun.get_saldo_awal()
    print(f"\t {saldo}")
    no = 1
    for i in akun.list_transaksi:
        print(f"{no}. {i}")
        no += 1
    print(f"Saldo Akhir: {akun.get_saldo()}")