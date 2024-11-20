class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk=merk
        self.model=model
        self.tahun=tahun

    def info_mobil(self):
        print("Mobil", self.merk, self.model, "keluaran tahun", self.tahun)
    
    def ubah_tahun(self, ubah):
        if(ubah>=self.tahun):
            self.tahun=ubah
        else: print("Error")



def main():
    mobil = Mobil("Toyota", "Avanza", 2015)
    mobil.info_mobil()
    mobil.ubah_tahun(2023)
    mobil.info_mobil()
    mobil.ubah_tahun(2010)

if __name__ == '__main__':
    main()