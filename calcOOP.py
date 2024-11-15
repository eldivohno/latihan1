class kalkulator:
    def tambah(self, num1, num2):
        return num1+num2
    

    def kurang(self, num1, num2):
        sub = num1-num2
        return sub
    
    def kali(self, num1, num2):
        self.a = num1
        self.b = num2
        tim = self.a*self.b
        return tim

    def bagi(self, num1, num2):
        self.a = num1
        self.b = num2
        if(self.b!=0):
            div = self.a/self.b
            return div
        else: return "tidak bisa membagi dengan 0"
    


def main():
    calc = kalkulator()
    print("Tambah :", calc.tambah(10, 5))
    print("Kurang :", calc.kurang(10, 5))
    print("Kali :", calc.kali(10, 5))
    print("Bagi :", calc.bagi(10, 0))

if __name__ == "__main__":
    main()