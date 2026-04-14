# def calc_soma(n1: float, n2: float):
#     s = n1 + n2
#     return s

# n1 = 6
# n2 = 8

# soma = calc_soma(n1,n2)
# print(soma)


def saudacao(nome: str = "Artur", hora: int = 20):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg} {nome}")

# saudacao(hora=10)


def calc_soma(*args):
    s = 0
    for num in args:
        s += num
    return s

def montar_frase(*args) -> str:
    s = 0
    for palavra in args:
        s += palavra
    return s.strip()

n1 = 6
n2 = 8

soma = calc_soma(n1,n2,10,20,30,50)
print(soma)