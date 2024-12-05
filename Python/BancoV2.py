users = [] # nome, data de nascimento, cpf e endereço + senha(eu mesma inclui)
contas = [{}] #agencia, numero da conta e usuário, num de conta é sequencial (inicia em 1) e agencia é fixa em 0001
user_logado = None
LIMITE = 500.0

def main():
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


def saque(user, conta):
    saldo = contas[conta]['saldo']
    numero_saques = 1
    while(numero_saques > 0):
        if(contas[conta]['limite_saques'] > 0):
            valor = input('\nDigite o valor que deseja sacar: ')

            if(isFloat(valor)):
                valor = float(valor)
                if(valor <= saldo and valor < LIMITE and valor > 0):
                    transacao = f'SAQUE: R${saldo:.2f} - R${valor:.2f} = R${(saldo-valor):.2f} CONTA: {contas[conta]['num_conta']}'
                    users[user]['extrato'].append(transacao)
                    saldo -= valor
                    contas[conta]['saldo'] = saldo
                    print('\nSaque realizado com sucesso')
                    contas[conta]['numero_saques'] -= 1
                    
                else:
                    print('\nValor inválido')
                        
            else:
                print('\nValor inválido!')

        else:
            print('\nLimite de saques atingido')

        numero_saques -= 1

    return saldo

def deposito(conta, user):
    saldo = contas[conta]['saldo']
    valor = input('\nDigite o valor que deseja depositar: ')
    if(isFloat(valor)):
        valor = float(valor)
        if(valor > 0):
            transacao = f'DEPOSITO: R${saldo:.2f} + R${valor:.2f} = R${(saldo+valor):.2f} CONTA: {contas[conta]['num_conta']}'
            users[user]['extrato'].append(transacao)
            saldo += valor
            contas[conta]['saldo'] = saldo
            print('\nDeposito realizado com sucesso')

        else:
            print('\nValor inválido!')
    else:
        print('\nValor inválido!')

def extrato(user):
    if users[user]['extrato'] == []:
        print('\nNão foram realizadas movimentações')
        return
    for elemento in users[user]['extrato']:
        print(f'\n{elemento}')
    return

def buscaCpf(cpf):
    if users == []:
        return True
    for i ,item in enumerate(users):
        if item['cpf'] == cpf:
            print('\nCPF já cadastrado!')
            return i
    return None

def buscaConta(user, num_conta):
    num_conta = int(num_conta)
    for c in contas:
        if c['user'] == users[user]['cpf']:
            if(num_conta == c['num_conta']):
                return num_conta
    print('\nConta não encontrada')
    return None

def criarUser():
    print('\nMenu de criação de usuário: ')
    nome = input('\nDigite seu nome: ')
    data = input('\nDigite sua data de nascimento: ')
    cpf = input('\nDigite seu cpf (sem caracteres especiais): ')
    senha = input('Digite uma senha: ')
    if len(cpf) != 11:
        print('\nCPF inválido!')
        return 
    if not buscaCpf(cpf): return
    
    user = {'nome' : nome, 'data' : data, 'cpf' : cpf, 'senha' : senha, 'extrato' : []}
    users.append(user)
    print(users)
    return

def criarConta():
    print('\nMenu de criação de conta')
    agencia = '0001'
    num_conta = len(contas) + 1
    user = user_logado
    saldo = 0.0
    nova_conta = {'agencia' : agencia, 'num_conta': num_conta, 'user' : user, 'saldo' : saldo, 
    'limite': 500.0, 'limite_saques' : 3}
    contas.append(nova_conta)
    return

def login():
    global user_logado
    print('\nInserir CPF:')
    cpf = input('\nDigite seu cpf (sem caracteres especiais): ')
    user = buscaCpf(cpf)
    if user is None:
        print('\nCPF inválido')
        return False
    senha = input('\nDigite a senha: ')
    if(senha == users[user]['senha']):
        print('\nLogin realizado com sucesso!')
        user_logado = user
        menu_login(user, True)
        return True
    else:
        print('\nSenha incorreta!')
        return False


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
        
    op = input('\nDigite a opção: ')

    return op

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
                login = False

            case _:
                print('\nOpção inválida')


main()