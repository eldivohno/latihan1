def kali(a,b) :
    c=a*b
    print(a,"*",b,"=",c)

def bagi(a,b):
    if (b!=0):
        c=a/b
        print(a,"/",b,"=",c)
    else:
        print("MATH ERROR")

def tambah(a,b):
    c=a+b
    print(a,"+",b,"=",c)

def kurang(a,b):
    c=a-b
    print(a,"/",b,"=",c)

def pangkat(a,b):
    c=a**b
    print(a,"^",b,"=",c)

def akar(a,b):
    c=a//b
    print("sqrt", b,"(",a,")","=", c)

def mod(a,b):
    c=a%b
    print(a,"%",b,"=",c)

a = float(input("Masukkan bilangan pertama : "))
b = float(input("Masukkan bilangan kedua : "))

print("Pilih operasi \n1. Kali\n2. Bagi\n3. Tambah\n4. Kurang\n5. Pangkat\n6. Akar\n7. Modulus")
n = int(input("Pilih operator (1-7) : "))

if(n==1):
    kali(a,b)
elif(n==2):
    bagi(a,b)
elif(n==3):
    tambah(a,b)
elif(n==4):
    kurang(a,b)
elif(n==5):
    pangkat(a,b)
elif(n==6):
    akar(a,b)
elif(n==7):
    mod(a,b)