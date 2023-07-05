users = []
logged = False
def criar_usuario():
    usuario = input('digite seu usuario:')
    cpf = input('digite seu cpf:')
    senha = input('digite sua senha:')

    users.append({'usuario': usuario, 'cpf':cpf, 'senha':senha})

def editar_usuario():

    usuario = input('digite seu usuario:')
    senha = input('digite sua senha:')

    for i in range(len(users)):
        if users[i]['usuario'] == usuario:
            if users[i]['senha'] != senha:
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
    senha = input('digite sua senha:')

    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != senha:
                print('senha incorreta')
                return
            else:
                users.remove(i)
                return
    print('usuario nao encontrado')

def login():
    usuario = input('digite seu usuario:')
    senha = input('digite sua senha:')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != senha:
                print('senha incorreta')
                return False
            else:
                return True

print('bem vindo ao nosso site :)')

while True:

    print('0 para logar em uma conta')
    print('1 para criar conta')
    print('2 para editar conta')
    print('3 para deletar conta')
    print('4 para mostrar as contas existentes')
    print('99 para sair')
    opt = input('digite uma opcao: ')

    try:
        opt = int(opt)
    except Exception:
        print('digite apenas numeros')

    if opt == 0:
        logged()
    if opt == 1:
        criar_usuario()
    elif opt == 2:
        editar_usuario()
    elif opt == 3:
        deletar_usuario()
    elif opt == 4:
        for i in range(len(users)):
            print(users[i])

    elif opt == 99:
        break

    else:
        print('opcao invalida')

print('ate logo ^^')

   