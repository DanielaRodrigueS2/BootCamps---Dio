from abc import ABC, abstractmethod
users = []
user_logado = None

class Conta:

    def __init__(self, cliente, historico):
        self._cliente = cliente
        self._saldo = 0.0
        self._agencia = '0001'
        self._numero = len(cliente.contas) + 1
        self._historico = historico

    def novaConta(cliente, numero):
        conta = Conta(cliente, numero)
        return conta

    def sacar(valor):
        pass

    def depositar(valor):
        pass

    @property
    def saldo(self):
        return self._saldo
    
class ContaCorrente(Conta):
    def __init__(self, cliente, historico, limite, limite_saques):
        super().__init__(cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:

    def adicionar_transacao(transacao):
        pass

class Transacao(ABC):

    @abstractmethod
    def registrar(conta):
        return conta
    
class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(conta):
        return super().registrar()
    
class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(conta):
        return super().registrar()   
    
class PessoaFisica:

    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Cliente(PessoaFisica):

    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(conta, transacao):
        pass

    def adicionar_conta(conta):
        pass

def main():
    #implementação de operacoes
    sistema = True
    while(sistema):
        op = textoMenu(1)
        match(op):
            case '1':
                login()
                print(f'\nTESTE user logado: {user_logado}')
            case '2':
                criarUser()
            case '3':
                sistema = False

            case _:
                print('\nOpção inválida')
            
    return

def textoMenu(tipo):
    
    if tipo == 1:
        print("""
    --- Menu Banco ---

    1 - Realizar Login
    2 - Realizar Cadastro
    3 - Sair do sistema 
    """)
        
        
    elif tipo == 2:
        print("""
    --- Menu Banco ---

    1 - Sacar
    2 - Depositar
    3 - Visualizar extrato 
    4 - Abrir nova conta
    5 - Suas informações
    6 - Sair 
    """)
        
    op = input('\nDigite a opção: ')

    return op


def login():
    pass

def criarUser():
    pass

