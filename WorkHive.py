users = []
anuncios = []
logged = False
logged_user = ''

def criar_usuario():
    usuario = input('digite seu usuario:')
    cpf = input('digite seu cpf:')
    senha = input('digite sua senha:')

    users.append({'usuario': usuario, 'cpf':cpf, 'senha':senha, 'feedback': [], 'notificacoes': []})
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

    usuario = input('digite seu usuario: ')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != input('digite sua senha: '):
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
                global logged_user
                logged_user = usuario
                return True

def novo_anuncios():

    produto = input('produto: ')
    descricao = input('descricao: ')
    valor = input('valor: ')
    categoria = input('Categoria: ')
    id = len(anuncios)+1
    feedbacks = []

    anuncios.append({'Usuario': logged_user, 'Nome': produto, 'Descrição': descricao, 'Valor': valor, 'ID': id, 'Categoria': categoria, 'Feedbacks': feedbacks})
    for user in users:
        if user['usuario'] != logged_user:
            user['notificacoes'].append('Novo anúncio disponível: ' + produto)
def deletar_anuncio():
    identificador = int(input('Digite o "ID" do seu auncio: '))

    #print(type(identificador))
    for i in anuncios:
        if i['ID'] == identificador:
            current_user = input('Confirme seu usuário: ')
            if current_user == logged_user:
                anuncios.remove(i)
                return
            else:
                print('Não foi possivel deletar o anúncio.')
                return
    print('Anúncio não encontrado.')

def listar_anuncios_por_categoria():
    categoria = input('Digite a categoria: ')

    for anuncio in anuncios:
        if anuncio['Categoria'].lower() == categoria.lower():
            print(anuncio)

def adicionar_feedback_anuncio():
    identificador = int(input('Digite o ID do anúncio: '))
    feedback = input('Digite seu feedback: ')

    for anuncio in anuncios:
        if anuncio['ID'] == identificador:
            anuncio['Feedbacks'].append(feedback)
            print('Feedback adicionado com sucesso!')
            return

    print('Anúncio não encontrado.')

def visualizar_feedbacks():
    for anuncio in anuncios:
        if anuncio['Usuario'] == logged_user:
            feedbacks = anuncio['Feedbacks']
            if len(feedbacks) > 0:
                print("Feedbacks do anúncio", anuncio['ID'], ":")
                for feedback in feedbacks:
                    print(feedback)
            else:
                print("Não há feedbacks para o anúncio", anuncio['ID'])
            return
    print("Nenhum anúncio encontrado para o usuário", logged_user)

def mostrar_notificacoes():
    for user in users:
        if user['usuario'] == logged_user:
            notificacoes = user['notificacoes']
            if notificacoes:
                print("Você tem", len(notificacoes), "notificação(ões):")
                for notificacao in notificacoes:
                    print(notificacao)
                user['notificacoes'] = []  # Limpa as notificações após exibi-las
            else:
                print("Você não possui notificações.")
            return
    print('Usuário não encontrado.')

print('bem vindo ao nosso site :)')

while True:

    print('0 para logar em uma conta')
    print('1 para criar conta')
    

    if logged == True:
        print('2 para editar conta')
        print('3 para deletar conta')
        print('4 para adicionar feedback a um anúncio')
        print('5 para criar anuncios')
        print('6 para deletar anúncios')
        print('7 visualizar ids de anuncios')
        print('8 para listar anuncios por categoria')
        print('10 para visualizar feedbacks')
        print('11 para visualizar notificações')
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
        if opt == 4:
            adicionar_feedback_anuncio()     
        if opt == 5:
            novo_anuncios()
        if opt == 6:
            deletar_anuncio()
        if opt == 7:
            for i in anuncios:
                print(i)
        if opt == 8:
            listar_anuncios_por_categoria()
        if opt == 10:
            visualizar_feedbacks()
        if opt == 11:
            mostrar_notificacoes()
            
    elif opt == 99:
        break
    else:
        print('opcao invalida')

print('ate logo ^^')