from conta import ContaCorrente

contas = {
    '1234-5': ContaCorrente('abcd1234', '1234-5', 100.0),
    '9876-5': ContaCorrente('1234abcd', '9876-5', 2000.0)
}

def login():
    num_conta = input('Digite o número da conta: ')
    senha = input('Digite sua senha: ')

    conta = contas.get(num_conta)
    if conta and conta.senha == senha:
        print(f'Seja bem-vindo (a), {conta.num_conta}!')
        return conta
    else:
        print('Conta e/ou senha inválida:')
        login()

def exibir_menu():
    print('\n\n\n\nBem-Vindo ao seu Banco!\n\n1: Consultar Saldo\n2: Fazer Depósito\n3: Sacar Dinheiro\n4: Transferência\n5: Sair')

conta_logada = login()

while True:
    exibir_menu()

    op_menu = int(input('Escolha uma Opção: '))

    if op_menu==1:
        conta_logada.consultar_saldo()
    elif op_menu==2:
        valor = float(input('Informe o valor a ser depositado: '))
        conta_logada.deposito(valor)
    elif op_menu==3:
        valor = float(input('Informe o valor para saque: '))
        conta_logada.saque(valor)
    elif op_menu==4:
        valor = float(input('Informe o valor a ser transferido: '))
        num_conta_destino = input('Digite a conta do destinatário: ')
        if num_conta_destino in contas and num_conta_destino != conta_logada.num_conta:
            conta_logada.transferencia(contas[num_conta_destino], valor)
        else:
            print('Conta destino não encontrada')
    elif op_menu==5:
        print('Obrigado por escolher nosso banco, até logo!')
        break
    else:
        print('Operação inválida!')