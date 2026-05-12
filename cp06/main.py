import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cadastrar_funcionario(lista_funcionarios: list, cpf: str, nome: str, salario: float) -> bool:
        salario_formatado = float(salario)
        lista_funcionarios.append({"cpf": cpf, "nome": nome, "salario": salario_formatado})
        return True
    

def checar_funcionario_existe(lista_funcionarios: list,cpf: str) -> bool:
    for i in lista_funcionarios:
        if i["cpf"] == cpf:
            return True
    return False


def listar_funcionarios(lista: list) -> None:

    print(f"{'CPF':<10} {'NOME':<30} {'SALARIO':>12}")
    print("=" * 54)

    for f in lista:
        cpf = f['cpf']
        nome = f['nome']
        salario = f"{f['salario']:>12.2f}"
        
        print(f"{cpf:>10} | {nome:<28} | {salario}")
    print()
    input("Pressione alguma tecla para continuar...")

lista_funcionarios = [
    {"cpf": "123", "nome": "Ana", "salario": 1000.0},
    {"cpf": "456", "nome": "Maria", "salario": 2000.0}
]

def listar_funcionario_cpf(lista: list, cpf: str) -> None:
    funcionario = ""
    for i in lista:
        if i["cpf"] == cpf:
            funcionario = i
    print(f"CPF......: {funcionario["cpf"]:<5}")
    print(f"Nome.....: {funcionario["nome"]:<5}")
    print(f"Salário..: {funcionario["salario"]:<5.2f}")
            
            

while True:
    print("M E N U")
    print("=" * len("M E N U"))
    print("0 - SAIR")
    print("1 - Cadastrar funcionários")
    print("2 - Consultar funcionários")
    print("5 - Listar funcionários")

    input_escolha = input("Escolha: ")

    match input_escolha:
        case "1":
            print("CADASTRANDO FUNCIONÁRIO:")
            print("========================")
            print()

            # Dados do Funcionário
            input_cpf = input("CPF.....: ")
            if checar_funcionario_existe(lista_funcionarios, input_cpf):
                print("Funcionario já existe!")
                print()
                input("Digite qualquer tecla para continuar...")
                limpar_tela()
                continue
            input_nome = input("Nome....: ")
            input_salario = input("Salário.: ")
            print()

            cadastrar_funcionario(lista_funcionarios, input_cpf, input_nome, input_salario)
            print("!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Cadastrado com sucesso!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!")
            print()

            input("Pressione alguma tecla para continuar...")
            limpar_tela()
        
        case "2":
            limpar_tela()
            
            print("CONSULTANDO FUNCIONÁRIO:")
            print("========================\n")
            input_cpf_consulta = input("CPF.....: ")
            if not checar_funcionario_existe(lista_funcionarios, input_cpf_consulta):
                print("\n"+"-"*24)
                print("Funcionário inexistente!")
                print("-"*24 + "\n")
                input("Pressione alguma tecla para continuar...")
                limpar_tela()
                continue
            print()
            listar_funcionario_cpf(lista_funcionarios, input_cpf_consulta)
            print()
            input("Pressione alguma tecla para continuar...")
            
        case "5":
            listar_funcionarios(lista_funcionarios)
        
        case "0":
            print("Saindo...")
            break

