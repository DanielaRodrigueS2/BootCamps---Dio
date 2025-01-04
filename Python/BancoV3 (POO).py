from abc import ABC, abstractmethod
users = []
user_logado = None

class Conta:

    def __init__(self, cliente):
        self._cliente = cliente
        self._saldo = 0.0
        self._agencia = '0001'
        self._numero = len(cliente.contas) + 1
        self._historico = Historico()

    def novaConta(self,cliente, numero):
        conta = Conta(cliente, numero)
        return conta

    def sacar(self,valor):
        pass

    def depositar(self,valor):
        self._saldo += valor

    @property
    def saldo(self):
        return self._saldo
    
class ContaCorrente(Conta):
    def __init__(self, cliente, historico, limite, limite_saques):
        super().__init__(cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:

    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self,transacao):
        self._transacoes.append(transacao)
        pass

class Transacao(ABC):

    @abstractmethod
    def registrar(conta):
        return conta
    
class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        valor = input('\nDigite o valor que deseja depositar: ')
    
        if isFloat(self.valor):
            valor = float(self.valor)
            if valor > 0:
                conta.depositar(valor)
                conta._historico.adicionar_transacao(self)
            else:
                print('\nValor inválido.')
        else:
            print('\nValor inválido.')
    
class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(conta):
        return super().registrar()   
    
class PessoaFisica:

    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Cliente(PessoaFisica):

    def __init__(self, cpf, nome, data_nascimento, endereco, contas,senha):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = contas
        self._senha = senha

    def realizar_transacao(conta, transacao):
        pass

    def adicionar_conta(conta):
        pass

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def contas(self):
        return self._contas

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
    global user_logado
    print('\nInserir CPF:')
    cpf = input('\nDigite seu cpf (sem caracteres especiais): ')
    user = buscaCpf(cpf)
    if user is None:
        print('\nCPF inválido')
        return False
    senha = input('\nDigite a senha: ')
    if(senha == user.senha):
        print('\nLogin realizado com sucesso!')
        user_logado = user
        menu_login(user, True)
        return True
    else:
        print('\nSenha incorreta!')
        return False

def criarUser():
    print('\nMenu de criação de usuário: ')
    nome = input('\nDigite seu nome: ')
    data = input('\nDigite sua data de nascimento: ')
    cpf = input('\nDigite seu cpf (sem caracteres especiais): ')
    endereco = input('\nDigite seu endereço: ')
    senha = input('Digite uma senha: ')
    if len(cpf) != 11:
        print('\nCPF inválido!')
        return 
    if buscaCpf(cpf) != None: 
        print('\nCPF já cadastrado!') 
        return
    contas = []
    user = Cliente(cpf, nome, data,endereco, contas, senha)
    users.append(user)
    print(users)
    return
    
def buscaCpf(cpf):
    if users == []:
        return None
    
    for user in users:
        if(user.cpf == cpf):
            return user
    
    return None

def menu_login(user, login):
    while(login):
        op = textoMenu(2)
        match(op):
            case '1':
                num_conta = input('\nDigite o número da conta: ')
                num_conta = buscaConta(user, num_conta)
                if(num_conta != None):
                    saque(user, num_conta)
                
            case '2':
                num_conta = input('\nDigite o número da conta: ')
                num_conta = buscaConta(user, num_conta)
                if(num_conta != None):
                    deposito(user, num_conta)
                
            case '3':
                extrato(user)

            case '4':
                criarConta()

            case '5':
                print(users[user])

            case '6':
                login = False    

            case _:
                print('\nOpção inválida')

def isFloat(numero):
    try:
        float(numero)
        return True
    
    except:
        return False

main()
