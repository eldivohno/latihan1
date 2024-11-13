
def test_list() :
    test = []
    for i in range(0, 3):
        print(type(i))
        g = int(input(f"{i}. test input : "))
        test.append(g)

    print("isi list : ", end='')
    for i in range(0, 3) :
        print(int(test[i]), end = ' ')

    print()

test_list()


