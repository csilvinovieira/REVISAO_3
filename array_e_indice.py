def imprimir_primeiro_ultimo_nome():
    
    nomes = ['João', 'Maria', 'Pedro', 'Beltrano']

    
    print(f"1-{nomes[0]}")

    
    print(f"4-{nomes[-1]}")


imprimir_primeiro_ultimo_nome()


def imprimir_segundo_terceiro_nome():
    
    nomes = ['João', 'Maria', 'Pedro', 'Beltrano']

    
    print(f"2-{nomes[1]}")

    
    print(f"3-{nomes[2]}")


imprimir_segundo_terceiro_nome()


def substituir_alimentos():
    
    array_inicial = ["Macarrão", "Pepino", "Batata"]

    
    alimentos = []
    for i in range(3):
        alimento = input(f"Digite o {i + 1}º alimento: ")
        alimentos.append(alimento)

    
    for i in range(3):
        array_inicial[i] = alimentos[i]

    
    for i, alimento in enumerate(array_inicial, start=1):
        print(f"{i} - {alimento}")


substituir_alimentos()