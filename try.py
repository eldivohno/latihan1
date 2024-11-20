class Transaksi:
    def __init__(self, sal=0):
        self.sal = sal

    def setorTunai(self):
        a = int(input("Masukkan jumlah Setoran: "))
        self.sal += a
        print(f"Saldo Anda sekarang: {self.sal}")

    def tarikTunai(self):
        a = int(input("Masukkan jumlah Penarikan: "))
        if a > self.sal:
            print("Saldo tidak mencukupi.")
        else:
            self.sal -= a
            print(f"Saldo Anda sekarang: {self.sal}")

    def cekSaldo(self):
        print(f"Saldo Anda: {self.sal}")


def main():
    print("Selamat datang di bank, silakan pilih transaksi Anda:")
    transaksi = Transaksi()

    while True:
        print("\nMenu Transaksi:")
        print("1. Setor Tunai")
        print("2. Tarik Tunai")
        print("3. Cek Saldo")
        print("4. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
            if pilihan == 1:
                transaksi.setorTunai()
            elif pilihan == 2:
                transaksi.tarikTunai()
            elif pilihan == 3:
                transaksi.cekSaldo()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan layanan kami!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

if __name__ == "__main__":
    main()
