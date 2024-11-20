class persegi:
    def __init__(self, sisi):
        self.sisi=sisi

    def keliling(self):
        return 4*self.sisi
    
    def luas(self):
        return self.sisi*self.sisi

    def print(self):
        k = self.keliling()
        a = self.luas()
        print("Keliling", k) 
        print("Luas", a) 
        

def main():
    p=persegi(3)
    p.print()

if __name__=='__main__':
    main()