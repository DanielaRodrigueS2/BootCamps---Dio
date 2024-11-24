LIMITE = 500.0
saques_diarios = 3
login = True

saldo = 0
valor_saque = 0
extrato = []

def isFloat(numero):
    try:
        float(numero)
        return True
    
    except:
        return False


while(login):
    print("""
    --- Menu Banco V1 ---
        
    1 - Sacar valor
    2 - Depositar valor
    3 - Visualizar extrato
    4 - Sair do sistema """)
    
    opcao = input('\nDigite a opção: ')

    match(opcao):
        case '1':
            if(saques_diarios > 0):
                valor = input('\nDigite o valor que deseja sacar: ')

                if(isFloat(valor)):
                    valor = float(valor)
                    if(valor <= saldo and valor < LIMITE and valor > 0):
                        transacao = f'SAQUE: R${saldo:.2f} - R${valor:.2f} = R${(saldo-valor):.2f}'
                        extrato.append(transacao)
                        saldo -= valor
                        print('\nSaque realizado com sucesso')
                        saques_diarios -= 1
                    
                    else:
                        print('\nValor inválido')
                        
                else:
                    print('\nValor inválido!')

            else:
                print('\nLimite de saques atingido')
            

        case '2':
            
            valor = input('\nDigite o valor que deseja depositar: ')
            if(isFloat(valor)):
                valor = float(valor)
                if(valor > 0):
                    transacao = f'DEPOSITO: R${saldo:.2f} + R${valor:.2f} = R${(saldo+valor):.2f}'
                    extrato.append(transacao)
                    saldo += valor
                    print('\nDeposito realizado com sucesso')

                else:
                    print('\nValor inválido!')
            else:
                print('\nValor inválido!')

            
        case '3':
            if(extrato == []):
                print('\nNão foram realizadas movimentações')

            else:
                print('\nEXTRATO:')
                for x in extrato:
                    print(f'\n{x}')
                    
    
        case '4':
            print('\nSaindo do sistema')
            login = False
            
        case _:
            print('\nOpção inválida')
