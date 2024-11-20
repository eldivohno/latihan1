class Buku:
    def __init__(self, judul, pengarang, tahun, status):
        self.judul=judul
        self.pengarang=pengarang
        self.tahun=tahun
        self.status=status       
            
    def info_buku(self):
        if(self.status==False):
            show="tidak dipinjam"
        elif(self.status==True):
            show="dipinjam"
        print(self.judul, "oleh", self.pengarang,", diterbitkan pada tahun", self.tahun, ", Status : ", show)
        
    def pinjam_buku(self):
        if(self.status==False):
            self.status=True
            print("Buku berhasil dipinjam")
        elif(self.status==True):
            print("Buku sudah dipinjam")
        
    def kembalikan_buku(self):
        self.status=False
        print("Buku berhasil dikembalikan")
            



def main():
    # False -> tidak dipinjam
    # True -> dipinjam
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
    buku1.info_buku()
    print()
    buku1.pinjam_buku()
    print()
    buku1.info_buku()
    print()
    buku1.pinjam_buku()
    print()
    buku1.info_buku()
    print()
    buku1.kembalikan_buku()
    print()
    buku1.info_buku()
    print()

if __name__ == '__main__':
    main()