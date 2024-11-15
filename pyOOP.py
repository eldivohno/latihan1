class mahasiswa:

    jenis = "Mahasiswa Aktif" #class variable

    def __init__(self, nama, jurusan, angkatan): # konstruksi __init()
        #instance var
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan
    
    def deskripsi_mahasiswa(self): #object
        print(self.nama, "dari", self.jurusan, ", Angkatan", self.angkatan, self.jenis)

def main():
    mahasiswa1 = mahasiswa("Fathir", "S1 Teknik Elektro", 2022)
    mahasiswa2 = mahasiswa ("Aswangga", "S1 Teknik Elektro", 2022)
    mahasiswa1.deskripsi_mahasiswa()
    mahasiswa2.deskripsi_mahasiswa()

if __name__=='__main__':
    main()

        

