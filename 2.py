import math
a, b, c=int(input()), int(input()), int(input())
if a > b and a > c:
    a1=math.sin(a)
    print(a1)
elif b > a and b>c:
    b1 = math.sin(b)
    print(b1)
elif c > a and c > b:
    c1 = math.sin(c)
    print(c1)

    