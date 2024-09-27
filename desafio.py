menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input(f'Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print(f'Operação falhou! O valor informado é inválido.')

    elif opcao == '2':
        valor = float(input(f'Informe o valor do saque: '))
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        passou_saques = numero_saques >= LIMITE_SAQUES
        if passou_saldo:
            print(f'Operação falhou! Você não tem saldo suficiente.')
        elif passou_limite:
            print(f'Operação falhou! O valor do saque excede o limite.')
        elif passou_saques:
            print(f'Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print(f'Operação falhou! O valor informado é inválido.')

    elif opcao == '3':
        print(f'================ EXTRATO ================')
        print(f'Não foram realizados movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=' * 44)

    elif opcao == '4':
        print(f'Programa encerrado!')
        break

    else:
        print(f'Operação inválida, por favor selecione novamente a operação desejada.')

    