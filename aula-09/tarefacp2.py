# Artur Henrique Siqueira

input_alunos_qnt = int(input("Quantidade de alunos: "))
count = 1
medias_sum = 0
aprovados = 0
reprovados = 0

while count < input_alunos_qnt + 1:
    print(f"Aluno {count}/{input_alunos_qnt} \n ")

    #Pede as notas, e verifica as erradas
    input_nota1 = float(input("Nota 1:"))
    while input_nota1 < 0 or input_nota1 > 10:
        input_nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        
    input_nota2 = float(input("Nota 2:"))
    while input_nota2 < 0 or input_nota2 > 10:
        input_nota2 = int(input("Digite uma nota válida entre 0 e 10. Nota:"))
        
    
    # Calcula a média e quem foi reprovado e aprovado
    print()
    media_alun = (input_nota1 + input_nota2) / 2
    if media_alun >= 6:
        print(f"Aprovado com média {media_alun}")
        aprovados += 1
    else:
        print(f"Reprovado com média {media_alun}")
        reprovados += 1
    count += 1
    medias_sum += media_alun
    print()


# Faz o calculo das médias, e printa a % de aprovados e reprovados
print("DADOS CONSOLIDADOS \n")
media_turma = medias_sum / input_alunos_qnt
print(f"Média da turma: {media_turma:.1f}")

if reprovados:
    reprovados_porcent =  (reprovados / input_alunos_qnt) * 100
    print(f"Reprovados: {reprovados_porcent:.1f}%")
else:
    print(f"Reprovados: 0.0%")
    
if aprovados:
    aprovados_porcent =  (aprovados / input_alunos_qnt) * 100
    print(f"Aprovados: {aprovados_porcent:.1f}%")
else:
    print(f"Aprovados: 0.0%")

