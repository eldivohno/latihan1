class kalkulator:
    def tambah(self, a, b):
        return a+b
    
    def kurang(self, a, b):
        return a-b
    
    def kali(self, a, b):
        return a*b

    def bagi(self, a, b):
        if(b!=0):return a/b
        else: return "tidak bisa membagi dengan 0"
    


def main():
    calc = kalkulator()
    print("Tambah :", calc.tambah(100, 27))
    print("Kurang :", calc.kurang(130, 3))
    print("Kali :", calc.kali(127, 1))
    print("Bagi :", calc.bagi(635, 5))

if __name__ == "__main__":
    main()