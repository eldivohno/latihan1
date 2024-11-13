def sum_odd_numbers(n) :
    num = 0
    for i in range(1, n+1):
        if (i % 2 != 0):
            num  =  num+i
    print("Output = ", num)

n = int(input("Masukkan Bilangan : "))
sum_odd_numbers(n)