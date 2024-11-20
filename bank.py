class transaksi:
    def __init__(self, sal):
        self.sal = sal

    def setorTunai(self):
        a = int(input("Masukkan jumlah Setoran : "))
        self.sal += a
        print("saldo anda sekarang", {self.sal})
        main()

    def tarikTunai(self):
        a = int(input("Masukkan jumlah Setoran : "))
        if (a<=self.sal):
            self.sal -= a
            print("saldo anda sekarang", self.sal)
        else : print("salso anda kurang")

    def cekSaldo(self):
        print(self.sal)
    

def main():
    print("Selamat datang di bank, silakan masukkan transaksi anda")
    test = transaksi(0)
    try:
        n = int(input("Pilih Transaksi anda"))
        if n==1: test.setorTunai()
        elif n==2: test.tarikTunai()
        elif n==3: test.cekSaldo()
    except:print("Menu tidak Valid")


if __name__=='__main__':
    main()