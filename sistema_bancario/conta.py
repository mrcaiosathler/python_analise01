class ContaCorrente:
    def __init__(self, senha, num_conta, saldo):
        self.num_conta = num_conta
        self.saldo = saldo
        self.senha = senha
    
    def consultar_saldo(self):
        print(f'O saldo da conta {self.num_conta} é R${self.saldo:.2f}')
    
    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado com sucesso!\nO saldo atual da conta é de R${self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou inválido!')
    
    def deposito(self, valor):
        if 0 < valor:
            self.saldo += valor
            print(f'Depósito realizado com sucesso!\nO saldo atual da conta é de R${self.saldo:.2f}')    
        else:
            print('Operação inválida!')
    
    def transferencia(self, destinatario, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            print(f'Transferência realizada com sucesso!\nO saldo atual da conta é de R${self.saldo:.2f}')
        else:
            print('Operação inválida!')
