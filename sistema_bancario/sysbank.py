#Contas
conta1 = 100
saldo1 = 50000

conta2 = 0
saldo2 = 0

while True:
    print('\n\n\n\nBem-Vindo ao seu Banco!\n\n1: Consultar Saldo\n2: Abrir Nova Conta\n3: Fazer Depósito\n4: Sacar Dinheiro\n5: Transferência\n6: Sair')

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
            num_conta_deposito = int(input('Informe o número da conta para depósito: '))
            if num_conta_deposito == conta1:
                saldo_dep = int(input(f'Bacana. Agora, informe o valor a ser depositado na conta {conta1}: R$'))
                saldo1 += saldo_dep
                print(f'Tudo certo! O novo saldo da conta {conta1} é: R$', saldo1)
            elif num_conta_deposito == conta2:
                saldo_dep = int(input(f'Bacana. Agora, informe o valor a ser depositado na conta {conta2}: R$'))
                saldo2 += saldo_dep
                print(f'Tudo certo! O novo saldo da conta {conta2} é: R$', saldo2)
            else:
                print('Essa conta não existe!')
        case 4:
            print('Okay! Vamos prosseguir com seu saque!')
            num_conta_saque = int(input('Informe o número da conta para saque: '))
            if num_conta_saque == conta1:
                saldo_saque = int(input(f'Bacana. Agora, informe o valor a ser sacado da conta {conta1}: R$'))
                saldo1 -= saldo_saque
                print(f'Tudo certo! O novo saldo da conta {conta1} é: R$', saldo1)
            elif num_conta_saque == conta2:
                saldo_saque = int(input(f'Bacana. Agora, informe o valor a ser sacado da conta {conta2}: R$'))
                saldo2 += saldo_saque
                print(f'Tudo certo! O novo saldo da conta {conta2} é: R$', saldo2)
        case 5:
            print('Okay! Vamos prosseguir com a transferência!')
            num_conta_origem = int(input('Informe o número da conta de origem: '))
            num_conta_destino = int(input('Informe agora o número da conta de destino:'))
            if num_conta_origem == conta1 and num_conta_destino == conta2:
                saldo_transf = int(input(f'Bacana. Agora, informe o valor a ser transferido entre as contas {num_conta_origem} e {num_conta_destino}: R$'))
                saldo1 -= saldo_transf
                saldo2 += saldo_transf
                print(f'Tudo certo! O dinheiro foi transferido com sucesso. O novo saldo da conta {conta1} é: R$', saldo1)
            elif num_conta_origem == conta2 and num_conta_destino == conta1:
                saldo_transf = int(input(f'Bacana. Agora, informe o valor a ser transferido entre as contas {num_conta_origem} e {num_conta_destino}: R$'))
                saldo2 -= saldo_transf
                saldo1 += saldo_transf
                print(f'Tudo certo! O dinheiro foi transferido com sucesso. O novo saldo da conta {conta2} é: R$', saldo2)
            else:
                print('Essa operação não é permitida!')
        case 6:
            print('Obrigado por escolher nosso banco, até logo!')
            break