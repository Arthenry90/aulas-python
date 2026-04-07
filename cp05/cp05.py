# Artur Henrique Siqueira RM: 566986
# Guilherme De Oliveira Scremin RM: 564788

import os
os.system("cls" if os.name == "nt" else "clear")

def isfloat(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    v = v.replace('.','',1)
    return v.isdigit()   

def isint(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    return v.isdigit()

def is_valor_numerico(valor) -> bool:
    if(not isfloat(valor) and not isint(valor)):
        return False
    valor = float(valor)
    return True

def somar_total_palavras(frase: str) -> int:
    total_palavras = 1

    for i in frase:
        if i == " ":
            total_palavras += 1
    return total_palavras

def somar_total_vogais(frase: str) -> int:
    vogais = "aeiou"
    num_vogais = 0
    frase_formatada = frase.lower()
    for i in frase_formatada:
        if vogais.count(i):
            num_vogais += 1
    return num_vogais

def somar_total_digitos(frase: str) -> int:
    num_digitos = 0
    for i in frase:
        if i.isdigit():
            num_digitos += 1
    return num_digitos

def somar_total_carac_special(frase: str) -> int:
    num_especial = 0
    frase_formatada = frase.lower()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for i in frase_formatada:
        if i.isdigit() or alfabeto.count(i):
            continue
        num_especial += 1
    return num_especial

def pegar_maior_valor(lista: list) -> float:
    maior_valor = lista[0]
    for i in lista:
        if i > maior_valor:
            maior_valor = i
    return maior_valor

def pegar_menor_valor(lista: list) -> float:
    menor_valor = lista[0]
    for i in lista:
        if i < menor_valor:
            menor_valor = i
    return menor_valor

def retorna_mais_proximo(lista : list, valor: float) -> float:
    mais_proximo = lista[0]
 
    if mais_proximo > valor:
        menor_distancia = mais_proximo - valor
    else:
        menor_distancia = valor - mais_proximo
 
    for i in lista:
        if i> valor:
            distancia_atual = i - valor
        else:
            distancia_atual = valor - i
 
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            mais_proximo = i
    return mais_proximo
 

Lista_completa = []
lista_numerica = []
lista_outros = []
 
 
while True:
    print("0 - SAIR")
    print("1 - Exercicio Lista")
    print("2 - Exercicio String")
 
    opcao = input("Escolha: ")
 
 
    match opcao:
        case "0":
            break
        
        case "1":
            print("Digite os elementos da lista ou '.' Para finalizar...")
            while True:
                elemento = input("")
                if elemento == ".":
                    break
                Lista_completa.append(elemento)
                if(is_valor_numerico(elemento)):
                    novo_elem = float(elemento)
                    lista_numerica.append(novo_elem)
                else:
                    lista_outros.append(elemento)
            print ()
            print ("a.")
            print("Lista completa =","[",", ".join(Lista_completa),"]")
            print ("Lista Númerica =", lista_numerica)
            print ("Lista outros =","[",", ".join(lista_outros), "]")
 
            print()
            print("b.")
            soma_numeros = sum(lista_numerica)            
            media_numeros = sum(lista_numerica) / len (lista_numerica)
            print("Soma da lista númerica =", soma_numeros)
            print("Media da lista númerica =", media_numeros)
            print("Maior valor =", pegar_maior_valor(lista_numerica))
            print("Menor valor =", pegar_menor_valor(lista_numerica))

            print("\nc.")
            input_valor_proximo = float(input("Digite um número: "))
            print("Encontrou o número: ", retorna_mais_proximo(lista_numerica, input_valor_proximo))
 
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            input_frase = input("Digite uma frase... ")
            while input_frase == "" or input_frase == " ":
                input_frase = input("Digite uma frase valida.")

            print("a. ",somar_total_palavras(input_frase), " palavras")
            print("b. ",somar_total_vogais(input_frase), " vogais (maiúsculas ou minúsculas)")
            print("c. ",somar_total_digitos(input_frase), " digitos.")
            print("d. ",somar_total_carac_special(input_frase)," caractes especiais.\n")




