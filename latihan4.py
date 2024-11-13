def filter_even_numbers(numbers):
    out = []
    
    for i in numbers:
        if(i%2==0):
            out.append(i)
    
    print("Output : [ ",end='')
    for a in range(0, len(out)) :
        print(int(out[a]), end = ' ')
    print("]")
    
numbers = []
n = int(input("Masukkan panjang list : "))
for i in range(0, n):
    isi = int(input("Isi list :"))
    numbers.append(isi)

print(numbers)
filter_even_numbers(numbers)

