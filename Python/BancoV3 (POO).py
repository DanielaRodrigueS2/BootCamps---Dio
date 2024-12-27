class Conta:

    LIMITE = 500.0
    limite_saques = 3
    
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def isFloat(numero):
        try:
            float(numero)
            return True
        
        except:
            return False

    def nova_conta(self, cliente, numero):
        print('\nMenu de criação de conta')
        agencia = '0001'
        num_conta = self.numero
        user = cliente
        saldo = 0.0
        nova_conta = {'agencia' : agencia, 'num_conta': num_conta, 'user' : user, 'saldo' : saldo, 
        'limite': 500.0, 'limite_saques' : 3}
        return nova_conta
    
    def sacar(self, valor):
        
        saldo = self.saldo
        valor = input('\nDigite o valor que deseja sacar: ')
        
        if self.isFloat(valor):
            valor = float(valor)
            if 0 < valor <= saldo and valor <= self.LIMITE:
                saldo -= valor
                limite_saques -= 1
                transacao = f'SAQUE: R${valor:.2f} - Saldo Atual: R${conta_data["saldo"]:.2f}'
                users[user]['extrato'].append(transacao)
                print('\nSaque realizado com sucesso.')
            else:
                print('\nValor inválido ou saldo insuficiente.')
        else:
            print('\nValor inválido.')

# Diagrama de classes muito confuso