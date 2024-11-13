def compare_numbers(a,b):
    if(a>b):
        print("a lebih besar")
    elif(a<b):
        print("b lebih besar")
    elif(a==b):
        print("sama")

a=int(input("Masukkan nilai a : "))
b=int(input("Masukkan nilai b : "))
compare_numbers(a,b)