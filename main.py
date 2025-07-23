def calcular_valor_multa(localidade, velocidade):
    if localidade == 1:  # Localidade
        if velocidade >= 120:
            return 320
        elif velocidade >= 90:
            return 120
        elif velocidade > 50:
            return 60
        else:
            return 0
        
    elif localidade == 2:  # Fora da localidade
        if velocidade >= 120:
            return 120
        elif velocidade > 90:
            return 60
        else:
            return 0
        
    elif localidade == 3:  # Autoestrada
        if velocidade > 175:
            return 360
        elif velocidade > 150:
            return 120
        elif velocidade > 120:
            return 60
        else:
            return 0
        
    else:
        return None

while True:
    print('Onde circulava o veiculo?')
    print('Escolha uma das opcoes abaixo:')
    print('1 - Localidade')
    print('2 - Fora da localidade')
    print('3 - Autoestrada')
    print()
    
    try:
        localidade = int(input('Introduza o local: '))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        continue

    if localidade not in [1, 2, 3]:
        print('Localidade inválida. Tente novamente.')
        continue

    try:
        velocidade = float(input('Introduza a velocidade do veiculo: '))
    except ValueError:
        print("Entrada inválida. Por favor, insira a velocidade em número real.")
        continue

    multa = calcular_valor_multa(localidade, velocidade)
    if multa is None:
        print('Localidade inválida.')
    elif multa == 0:
        print('Sem multa')
    else:
        print(f'Multa de {multa} euros')

    continuar = input("Deseja calcular se Tem Multa (s/n): ").lower()
    if continuar != 's':
        print("Seguranca em primeiro!")
        break