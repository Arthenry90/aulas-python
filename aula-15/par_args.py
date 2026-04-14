import os
os.system("cls")

def calc_soma(*args) -> float:
    s = 0
    for num in args:
        s += num
    return s

# Uso
n1 = 6
n2 = 8
soma = calc_soma(n1, n2, 78, 66, 54)
print(soma)