mas = []
s = 0
for i in range(10) :
    mas.append(int(input("Введите элемент массива:")))
    if mas[-1] > 5 :
        s += mas[-1]
print(s)

