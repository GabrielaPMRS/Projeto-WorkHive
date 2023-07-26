import SendGmail
import MockData

DEBUG = True
users = []
anuncios = []
favoritos = []
logged = False
logged_user = ''

def criar_usuario():
    usuario = input('Digite seu usuario:')
    cpf = input('Digite seu cpf:')
    senha = input('Digite sua senha:')

    users.append({'usuario': usuario, 'cpf':cpf, 'senha':senha, 'feedback': [], 'notificacoes': []})

def editar_usuario():
    usuario = input('digite seu usuario:')

    for i in range(len(users)):
        if users[i]['usuario'] == usuario:
            if users[i]['senha'] != input('Digite sua senha:'):
                print('Senha incorreta')
                return
            else:
                print('O que deseja mudar?')
                print('1 para usuario')
                print('2 para senha')
                opt = int(input("Digite sua opção:"))
                if opt == 1:
                    users[i]['usuario'] = input('Digite um novo usuario:')
                if opt == 2:
                    users[i]['senha'] = input('Digite a nova senha:')
                return
    print('Usuário não encontrado')

def deletar_usuario():
    usuario = input('Digite seu usuario: ')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != input('Digite sua senha: '):
                print('Senha incorreta')
                return
            else:
                users.remove(i)
                logged == False
                return
    print('usuario nao encontrado')

def login():
    usuario = input('Digite seu usuario:')
    for i in users:
        if i['usuario'] == usuario:
            if i['senha'] != input('Digite sua senha:'):
                print('Senha incorreta')
                return False
            else:
                global logged_user
                logged_user = usuario
                return True

def novo_anuncios():
    produto = input('Produto: ')
    descricao = input('Descricao: ')
    valor = input('Valor: ')
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

def favoritar():
    id_anuncio = int(input('Qual o ID do anúncio que deseja favoritar? '))
    for i in anuncios:
        if i['ID'] == id_anuncio:
            favoritos.append(id_anuncio)
            break

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

print('\nBem vindo ao WorkHive :)\n')

if DEBUG:
    MockData.mock_data(users, anuncios)

while True:
    print('\n**** MENU ****\n')
    print('0 para logar em uma conta')
    print('1 para criar conta')
    print('2 para mostrar as contas existentes') #retirar no código final
    print('3 para listar anuncios por categoria')
    
    if logged == True:
        print('4 para editar conta')
        print('5 para deletar conta')
        print('6 para adicionar feedback a um anúncio')
        print('7 para criar anuncios')
        print('8 para deletar anúncios')
        print('9 visualizar ids de anuncios')
        print('10 para favoritar um anúncio')
        print('11 visualizar aba de favoritos')
        print('12 para visualizar feedbacks')
        print('13 para visualizar notificações')
        print('14 para enviar email para o prestador de serviço')

    print('99 para sair')
    
    opt = input('\nDigite uma opção: ')

    try:
        opt = int(opt)
    except Exception:
        print('Digite apenas numeros')

    if opt == 0:
        logged = login()
    elif opt == 1:
        criar_usuario()
    elif opt == 2:
        for i in range(len(users)):
            print(users[i])
    elif opt == 3:
        listar_anuncios_por_categoria()

    elif logged == True:
        
        if opt == 4:
            editar_usuario()
        if opt == 5:
            deletar_usuario()
        if opt == 6:
            adicionar_feedback_anuncio()     
        if opt == 7:
            novo_anuncios()
        if opt == 8:
            deletar_anuncio()
        if opt == 9:
            for i in anuncios:
                print(i)
        if opt == 10:
            favoritar()
        if opt == 11:
            print('Aba de favoritos: ',end=' ')
            for favorito in favoritos:
                print(favorito, end=' ')       
        if opt == 12:
            visualizar_feedbacks()
        if opt == 13:
            mostrar_notificacoes()
        if opt == 14:
            SendGmail.send_email()
            
    elif opt == 99:
        break
    else:
        print('Opção inválida')

print('Até logo ^^')
