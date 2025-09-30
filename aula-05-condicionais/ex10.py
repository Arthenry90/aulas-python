input_string = input("Digite um dia da semana: ")

match input_string:
    case "segunda-feira":
        print("Dia da semana")
    case "terça-feira":
        print("Dia da semana")
    case "quarta-feira":
        print("Dia da semana")
    case "quinta-feira":
        print("Dia da semana")
    case "sexta-feira":
        print("Dia da semana")
    case "sabado":
        print("Final de semana")
    case "domingo":
        print("Final de semana")
    case _:
        print("Não é nenhum dia da semana")