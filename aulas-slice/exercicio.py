# Exercicio
# 1. Crie uma função que passe uma frase por parametro e substtitua todas as vogais por pontos de interrogação
# retornando a frase modificado


def troca_vogais(frase: str) -> str:
    vogais = ["a","e","i","o","u"]
    frase_mod = ""
    for char in frase:
        # print(char)
        char_add = char
        if vogais.count(char.lower()):
            char_add = "?"
            print(char)
        frase_mod += char_add
    frase = frase_mod
    return frase

frase = "Edson de Oliveira"
new_frase = troca_vogais(frase)
print(new_frase)
print(frase)