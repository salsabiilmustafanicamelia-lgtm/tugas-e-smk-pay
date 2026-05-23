from .syarat import Akun

MAX_SALDO_SISWA = 500000

class AkunSiswa(Akun):
    def __init__ (self, nama, kelas, saldo):
        self.nama = nama
        self.kelas = kelas
        self.__saldo = saldo
        self._riwayat = []
        self.list_transaksi = []
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, jumlah):
        if self.__saldo + jumlah <= MAX_SALDO_SISWA and jumlah > 0:
            self.__saldo += jumlah
            self._riwayat.append(f"Deposit: \t+{jumlah}")
            self.list_transaksi.append(f"+ \t{jumlah}")

        elif jumlah < 0:
            print("Jumlah deposit tidak boleh negatif.")
        else:
            print("Jumlah deposit melebihi batas maksimum saldo.")
            
    def keluar_saldo(self, jumlah):
        if self.__saldo >= jumlah:
            self.__saldo -= jumlah
            self._riwayat.append(f"Penarikan: \t-{jumlah}")
            self.list_transaksi.append(f"- \t{jumlah}")
        else:
            print("Saldo tidak cukup untuk melakukan transaksi.")
            
    def bayar(self, akunkantin, jumlah):
        if self.__saldo >= jumlah:
            self.keluar_saldo(jumlah)
            self.list_transaksi.append(f"- \t{jumlah}")
            akunkantin.siswa_bayar(jumlah)
        else:
            print("Saldo tidak cukup untuk melakukan pembayaran.")
            
class AkunKantin(Akun):
    def __init__ (self, nama_toko, saldo):
        self.nama = nama_toko 
        self.__saldo = saldo
        self._riwayat = []
        self.list_transaksi = []

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            self._riwayat.append(f"Deposit: \t+{jumlah}")
            self.list_transaksi.append(f"+ \t{jumlah}")
        else:
            print("Jumlah deposit tidak boleh negatif.")
            
    def keluar_saldo(self, jumlah):
        if self.__saldo >= jumlah:
            self.__saldo -= jumlah
            self._riwayat.append(f"Penarikan: \t-{jumlah}")
            self.list_transaksi.append(f"- \t{jumlah}")
        else:
            print("Saldo tidak cukup untuk melakukan transaksi.")
            
    def siswa_bayar(self, jumlah):
        jumlah_baru = round(jumlah * 0.1) # Potongan biaya admin 10%
        self._riwayat.append(f"Pembayaran dari siswa: \t+{jumlah}")
        self._riwayat.append(f"Potongan biaya admin: \t-{jumlah_baru}")
        self.list_transaksi.append(f"+ \t{jumlah}")
        self.list_transaksi.append(f"- \t{jumlah_baru}")
        jumlah -= jumlah_baru # Potongan biaya admin
        self.__saldo += jumlah
        
