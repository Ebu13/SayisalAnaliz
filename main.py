import math

def fact(fac):
    if fac == 1:
        return 1
    return fac * fact(fac - 1)


def ust(sayi, us):
    if us == 0:
        return 1
    return sayi * ust(sayi, us - 1)


x=math.radians(int(input("Hangi değere göre:")))

terim = int(input("Kaçıncı terime kadar:"))



result = 1
i = 1
j = 2
if terim != 0:
    while i <= terim:
        if i%2 == 0:
            result += (ust(x, j)) / fact(j)
        else:
            result -= (ust(x, j)) / fact(j)
        i +=1
        j +=2

print(round(result, 16))
