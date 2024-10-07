def menu():    
    menu = '''
    ========== PyBank ==========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [7] Sair

    => '''
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'\nDepósito realizado com sucesso!')

    else:
        print(f'\nOperação falhou! O valor informado é inválido.')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f'Operação falhou! Você não tem saldo suficiente.')

    elif excedeu_limite:
        print(f'Operação falhou! O valor do saque excede o limite.')

    elif excedeu_saques:
        print(f'Operação falhou! Número máximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print(f'\nSaque realizado com sucesso!')

    else:
        print(f'Operação falhou! O valor informado é inválido.')

    return saldo, extrato


def extrato(saldo, /, *, extrato):
    print(f'============= EXTRATO =============')
    print(f'Não foram raelizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print(f'===================================')


def criar_usuario(usuarios):
    cpf = str(input(f'Informe o CPF (somente número, sem espaços, pontos e "-"): ')).strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'\nJá existe usuário com esse CPF!')
        return
    
    nome = str(input(f'Informe o nome completo: ')).strip()
    data_de_nascimento = str(input(f'Informe a data de nascimento (dd-mm-aaaa): ')).strip()
    endereco = str(input(f'Informe o endereço (bairro - nº - cidade/sigla do estado): ')).strip()

    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereço': endereco})

    print(f'Usuário criado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input(f'Informe o CPF do usuário (somente número, sem espaços, pontos e "-"): ')).strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print(f'\nUsuário não encontrado. Criação de conta encerrada!')


def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência: {conta['agencia']}
        Nº: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(linha)


def main():    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:
        opcao = menu()
        if opcao == '1':
            valor = float(input(f'Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input(f'Informe o valor do saque: '))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
                )

        elif opcao == '3':
            extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)    

        elif opcao == '7':
            print(f'Programa encerrado!')
            break

        else:
            print(f'Operação inválida, por favor selecione novamente a operação desejada.')


main()