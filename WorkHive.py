users = []
anuncios = []
logged = False
def criar_usuario():
    usuario = input('digite seu usuario:')
    cpf = input('digite seu cpf:')
    senha = input('digite sua senha:')

    users.append({'usuario': usuario, 'cpf':cpf, 'senha':senha})

def editar_usuario():

    usuario = input('digite seu usuario:')

    for i in range(len(users)):
        if users[i]['usuario'] == usuario:
            if users[i]['senha'] != input('digite sua senha:'):
                print('senha incorreta')
                return
            else:
                print('o que deseja mudar?')
                print('1 para usuario')
                print('2 para senha')
                opt = int(input("digite sua opcao:"))
                if opt == 1:
                    users[i]['usuario'] = input('digite um novo usuario:')
                if opt == 2:
                    users[i]['senha'] = input('digite a nova senha:')
                return
    print('usuario nao encontrado')

def deletar_usuario():

    usuario = input('digite seu usuario:')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != input('digite sua senha:'):
                print('senha incorreta')
                return
            else:
                users.remove(i)
                logged == False
                return
    print('usuario nao encontrado')

def login():
    usuario = input('digite seu usuario:')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != input('digite sua senha:'):
                print('senha incorreta')
                return False
            else:
                return True

def novo_anuncios():

    produto = input('produto: ')
    descricao = input('descricao: ')
    valor = input('valor: ')

    id = len(anuncios)+1

    new_anuncios = {
        'Name' : produto,
        'Descricao' : descricao,
        'Valor' : valor,
        'ID' : id
    }
    anuncios.append(new_anuncios)

print('bem vindo ao nosso site :)')

while True:

    print('0 para logar em uma conta')
    print('1 para criar conta')
    

    if logged == True:
        print('2 para editar conta')
        print('3 para deletar conta')
        print('5 para criar anuncios')
        print('6 visualizar ids de anuncios')

    print('9 para mostrar as contas existentes')
    print('99 para sair')
    opt = input('digite uma opcao: ')

    try:
        opt = int(opt)
    except Exception:
        print('digite apenas numeros')

    if opt == 0:
        logged = login()
    if opt == 1:
        criar_usuario()
    elif opt == 9:
        for i in range(len(users)):
            print(users[i])

    elif logged == True:
        
        if opt == 2:
            editar_usuario()
        elif opt == 3:
            deletar_usuario()
        if opt == 5:
            novo_anuncios()
        if opt == 6:
            for i in anuncios:
                print(i)

    elif opt == 99:
        break

    else:
        print('opcao invalida')

print('ate logo ^^')

   