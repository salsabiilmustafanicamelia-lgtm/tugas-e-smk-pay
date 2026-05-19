from abc import ABC, abstractmethod

class Akun(ABC):
    @abstractmethod
    def get_saldo(self):
        pass
    
    @abstractmethod
    def set_saldo(self, jumlah):
        pass
    
    @abstractmethod
    def keluar_saldo(self, jumlah):
        pass
    
class Menu_c(ABC):
    def __init__(self):
        self._pass_siswa = "123123"
        self._pass_kantin = "321321"
        
    @abstractmethod
    def menu(self):
        pass