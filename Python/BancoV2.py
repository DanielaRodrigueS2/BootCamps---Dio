users = [{}] # nome, data de nascimento, cpf e endereço + senha(eu mesma inclui)
contas = [{}] #agencia, numero da conta e usuário, num de conta é sequencial (inicia em 1) e agencia é fixa em 0001

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    return saldo, extrato

def deposito(saldo, valor, extrato, /):

    return saldo, extrato

def extrato(saldo, /, extrato):
    return 

def criarUser():
    print('\nMenu de criação de usuário: ')
    nome = input('\nDigite seu nome: ')
    data = input('\nDigite sua data de nascimento: ')
    cpf = input('\nDigite seu cpf (sem caracteres especiais): ')
    senha = input('Digite uma senha: ')
    if len(cpf) != 11:
        print('\nCPF inválido!')
        return 
    for item in users:
        if item['cpf'] == cpf:
            print('\nCPF já cadastrado!')
            return
        
    user = {'nome' : nome, 'data' : data, 'cpf' : cpf, 'senha' : senha, 'extrato' : []}
    users.append(user)
    return

def criarConta():
    print('\nMenu de criação de conta')
    agencia = '0001'
    num_conta = len(contas) + 1
    user = ...
    return

def login():
    print('\n')

def isFloat(numero):
    try:
        float(numero)
        return True
    
    except:
        return False

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
    5 - Sair 
    """)

    return

def main():
    return