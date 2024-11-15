class Thruster:
    
    def dispStop(self):
        self.pwmt1 = 1500
        self.pwmt2 = 1500
        self.pwmt3 = 1500
        self.pwmt4 = 1500
        print("Nilai PWM Thruster1", self.pwmt1)
        print("Nilai PWM Thruster2", self.pwmt2)
        print("Nilai PWM Thruster3", self.pwmt3)
        print("Nilai PWM Thruster4", self.pwmt4)


    def dispMaju(self):
        self.pwmt1 = 1700
        self.pwmt2 = 1700
        self.pwmt3 = 1700
        self.pwmt4 = 1700
        print("Nilai PWM Thruster1", self.pwmt1)
        print("Nilai PWM Thruster2", self.pwmt2)
        print("Nilai PWM Thruster3", self.pwmt3)
        print("Nilai PWM Thruster4", self.pwmt4)

    def dispMundur(self):
        self.pwmt1 = 1300
        self.pwmt2 = 1300
        self.pwmt3 = 1300
        self.pwmt4 = 1300
        print("Nilai PWM Thruster1", self.pwmt1)
        print("Nilai PWM Thruster2", self.pwmt2)
        print("Nilai PWM Thruster3", self.pwmt3)
        print("Nilai PWM Thruster4", self.pwmt4)
        

    



class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()
    
    def stop(self):
        print("Thruster berhenti")
        self.thruster.dispStop()

    def gerakMaju(self):
        print("Thruster bergerak maju")
        self.thruster.dispMaju()

    def gerakMundur(self):
        self.thruster.dispMundur()
        print("Thruster bergerak mundur")
      

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__=='__main__':
    main()
