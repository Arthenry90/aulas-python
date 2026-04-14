import os
os.system("cls")

def saudacao(usuario: str = "Edson", hora: int = 8) -> None:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"

    print(f"{usuario}, {msg}! Seja bem-vindo!")

# Uso
saudacao()
saudacao("Maria")
saudacao("Joao", 14)
saudacao(hora =  20)

x.sorted(reverse = True)