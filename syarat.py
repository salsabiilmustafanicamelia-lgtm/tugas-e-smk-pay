from abc import ABC, abstractmethod

class Akun(ABC):
    @abstractmethod
    def get_saldo(self):
        pass
    
    @abstractmethod
    def set_saldo(self, jumlah):
        pass
    
    def keluar_saldo(self, jumlah):
        pass