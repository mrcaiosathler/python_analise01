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
        print('Seja bem-vindo (a), {conta.num_conta}!')


def exibir_menu():
    print('\n\n\n\nBem-Vindo ao seu Banco!\n\n1: Consultar Saldo\n2: Fazer Depósito\n3: Sacar Dinheiro\n4: Transferência\n5: Sair')

while True:
    exibir_menu()

    op_menu = int(input('Escolha uma Opção: '))

    if op_menu==1:
        conta1.consultar_saldo()
    elif op_menu==2:
        valor = float(input('Informe o valor a ser depositado: '))
        conta1.deposito(valor)
    elif op_menu==3:
        valor = float(input('Informe o valor para saque: '))
        conta1.saque(valor)
    elif op_menu==4:
        valor = float(input('Informe o valor a ser transferido: '))
        conta1.transferencia(conta2, valor)
    elif op_menu==5:
        print('Obrigado por escolher nosso banco, até logo!')
        break
    else:
        print('Operação inválida!')