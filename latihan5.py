def shopping_list(listA):
    listB = {}

    for i in listA:
        if i in listB:
            listB[i] += 1
        else:
            listB[i] = 1    
    
    print("Output : ", end=''+str(listB)+"\n")

listA = []
n = str(input("Tulis Mulai untuk mengisi list"))

while True:
    
    n=str(input("Masukkan barang: "))  
    if(n!="selesai"): listA.append(n)
    else : break
    
        
shopping_list(listA)

