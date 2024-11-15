class Thruster:
    def __init__(self):
        self.t1 = 1500
        self.t2 = 1500
        self.t3 = 1500
        self.t4 = 1500
    
    def set(self, val):
        self.t1=val
        self.t2=val
        self.t3=val
        self.t4=val 
    
    def prinNilai(self):
        print("Nilai PWM Thruster1 = ", self.t1)
        print("Nilai PWM Thruster2 = ", self.t2)
        print("Nilai PWM Thruster3 = ", self.t3)
        print("Nilai PWM Thruster4 = ", self.t4)
        
class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()
    
    def stop(self):
        print("Thruster berhenti")
        self.thruster.prinNilai()

    def gerakMaju(self):
        self.thruster.set(1700)
        print("Thruster bergerak maju")
        self.thruster.prinNilai()

    def gerakMundur(self):
        self.thruster.set(1300)
        print("Thruster bergerak mundur")
        self.thruster.prinNilai()
        
      

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__=='__main__':
    main()
