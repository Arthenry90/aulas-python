def retorna_indices(nome: str, char: str):
    return nome.find(char)


nome = "Ola meu amigo"
print(retorna_indices(nome, "O"))