a = int(input("Введите высоту прямоугольника:"))
b = int(input("Введите ширину прямоугольника:"))
for i in range(a):
    for e in range(b):
        print("*", end = "")
    if e == b - 1:
        print()
