### IMPORTACAO DE BIBLIOTECAS ###
import textwrap

### FUNÇÕES ###
def sacar (*,valor, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor >saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('Operacão falhou! Você não possui saldo suficiente')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido')
    elif valor >0:
        saldo -= valor
        extrato += f'Saque: \t R${valor:.2f}\n'
        numero_saques += 1
        print('Saque Realizado com Sucesso!')
    else:
        print('Operação falhou! Valor informado não é válido')

    return saldo, extrato

def depositar (saldo,valor, extrato,/):
    if valor >0:
       saldo += valor
       extrato += f'Deposito: \t R${valor:.2f}\n'
       print('Deposito Realizado com Sucesso!')
    else:
       print('Operacao Invalida!')
    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print('----- Extrato ------')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'Saldo: \t\t R$ {saldo:.2f}')
    print('--------------------')

def criar_usuario (usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuario ja existe')
        return
    
    nome = input('Insira o Nome Completo:')
    data_nascimento = input('Informa a Data de Nascimento (dd-mm-aaaa): ')
    endereco = input('Informa o endereco (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data-nascimento': data_nascimento, 'CPF': cpf, 'Endereco': endereco})

    print('Usuario Cadastrado com Sucesso!')

def filtrar_usuario (cpf, usuarios):
   usuario_filtrado = [i for i in usuarios if i['CPF'] == cpf ]
   return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {'Agencia': agencia, 'Numero Conta': numero_conta, 'Usuario': usuario}
    
    print('Usuario nao encontrado! Fluxo de criacao de conta encerrado!')

def listar_contas (contas):
    for conta in contas:
        linha = f'''\
            Agencia: \t {conta['Agencia']}
            C/C: \t\t {conta['Numero Conta']}
            Titular:\t {conta['Usuario']['nome']}

        '''
        print('='*100)
        print(textwrap.dedent(linha))

def menu():

    menu ='''\n
    ### Banco Will ###
         Selecione a Opcao Desejada!
          1 - Depositar
          2 - Sacar
          3 - Extrato
          4 - Novo Usuario
          5 - Nova Conta
          6 - Lista Usuarios
          7 - Sair                   
         '''
    return int(input(textwrap.dedent(menu)))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:

        entrada = menu()

        if entrada == 1:
            try:
                valor = int(input('Digite o valor do deposito:'))
                
                saldo, extrato = depositar(saldo, valor, extrato)
            except:
                print('Digite um Valor Válido!')
        
        elif entrada == 2:
            try:
                valor = int(input('Digite o valor do saque:'))
                saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    limite_saques= LIMITE_SAQUES,
                )
            except:
                print('Digite um Valor Válido!')
        
        elif entrada == 3:
            exibir_extrato(saldo, extrato=extrato)
            
        elif entrada == 4:
            criar_usuario(usuarios)

        elif entrada == 5:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif entrada == 6:
            listar_contas(contas)

        elif entrada == 7:
            break
        else:
            print('Digite uma opção válida!!')
        

main()
