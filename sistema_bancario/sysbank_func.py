#Funções
def exibir_menu():
    print('\n\n\n\nBem-Vindo ao seu Banco!\n\n1: Consultar Saldo\n2: Abrir Nova Conta\n3: Fazer Depósito\n4: Sacar Dinheiro\n5: Transferência\n6: Sair')

def saque(valor):
    global saldo 
    saldo -= valor
    print(f'Saque realizado com sucesso!\nO saldo atual da conta é de R${saldo}')
    
def deposito(valor):
    global saldo 
    saldo += valor
    print(f'Depósito realizado com sucesso!\nO saldo atual da conta é de R${saldo}')    

def transferencia(valor):
    global saldo, destinatario 
    saldo += valor
    destinatario += valor
    print(f'Transferência realizada com sucesso!\nO saldo atual da conta é de R${saldo}')
    

#Variáveis Independentes
conta1 = 100
saldo1 = 50000

conta2 = 0
saldo2 = 0
       

while True:
    exibir_menu()

    op_menu = int(input('Escolha uma Opção: '))

    match op_menu:
        case 1:
            num_conta_consulta = int(input('Informe o número da conta para consulta: '))
            if num_conta_consulta == conta1:
                print(f'O saldo da conta {conta1} é de R${saldo1}')
            elif num_conta_consulta == conta2:
                print(f'O saldo da conta {conta2} é de R${saldo2}')
            else:
                print('Essa conta não existe!')
        case 2:
            print('Obrigado por escolher nosso banco! Agora, informe os dados para abertura de conta.')
            conta2 = int(input('Informe o número da conta, com três dígitos: '))
            saldo2 = int(input('Informe o valor do depósito de abertura da conta: '))
            print('Conta aberta com sucesso!')
        case 3:
            print('Iremos cuidar muito bem do seu dinheiro, pode deixar.')
            valor = float(input('Informe o valor a ser depositado: '))
            deposito(valor)
        case 4:
            print('Okay! Vamos prosseguir com seu saque!')
            valor = float(input('Informe o número da conta para saque: '))
            saque(valor)
        case 5:
            print('Okay! Vamos prosseguir com a transferência!')
            valor = float(input('Informe o valor a ser transferido: '))
            transferencia(valor)
        case 6:
            print('Obrigado por escolher nosso banco, até logo!')
            break







