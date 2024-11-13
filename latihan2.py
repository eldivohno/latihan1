def count_characters(s):
        all_freq = {}
 
        for i in s:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
 
        print("Output : ", end=''+str(all_freq)+"\n")

s = str(input('Enter your string: '))

count_characters(s)