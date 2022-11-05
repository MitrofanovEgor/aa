for i in range(3 + 1):
    for s in range(3 - i):
        print(end = " ")
    for j in range(i):
        print("*", end = " ")
    print()
if i == 3:
    for i in range(3 - 1,0, -1):
        for s in range(3 - i):
            print(end = " ")
        for j in range(i):
            print("*", end = " ")
        print()
