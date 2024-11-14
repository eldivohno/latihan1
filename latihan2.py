def count_characters(s):
        stringW = {}
 
        for i in s:
            if i in stringW :
                stringW[i] += 1
            else:
                stringW[i] = 1
 
        print("Output : ", end=''+str(stringW)+"\n")

s = str(input('Masukkan kata : '))

count_characters(s)