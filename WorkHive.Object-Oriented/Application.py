from User import User
from Ad import Ad
from Feedback import Feedback
from GmailHandler import GmailHandler
from email.message import EmailMessage


class Application():
    def __init__(self):
        self.logged_username = None

        self.users = {
            'Gabi': User('Gabi', '1234556', '123'),
            'Lara': User('Lara', '9876543', '321')
        }
        
        self.ads_dict = {
            1: Ad('Gabi', 'tecnologia', 'crio sites', '76543'),
            2: Ad('Gabi', 'Marcenaria', 'mesas artesanais', '123'),
            3: Ad('Lara', 'Hidráulico', 'conserto canos', '45'),
            4: Ad('Lara', 'eletricista', 'crio tomadas', '150'),
        }

        self.category = ['tecnologia', 'consultoria juridica','consultoria engenharia' 'ensino']

        self.fb_master_list = []
        self.logged_username = 'Lara'
        self.add_feedback(1, 'Muito bem feito')
        self.logged_username = 'Gabi'
        self.add_feedback(4, 'Me salvou muito')

        self.logged_username = None
        

    def start(self):
        while True:
            if self.logged_username == None:
                print('\n*** MENU ***')
                print('1 para criar usuario.')
                print('2 para fazer login.')
                print('999 para mostrar usuarios cadastrados.')

                try:
                    option = int(input ('\nSelect option: '))
                except ValueError:
                    print("Opção inválida.\n")
                    continue

                if option == 1:
                    username = input('Digite seu nome de usuario: ')
                    cpf = input('Digite seu cpf: ')
                    password = input('Crie sua senha: ')

                    self.create_user(username, cpf, password)
                    

                elif option == 2:
                    username = input('Digite seu nome de usuario: ')
                    password = input('Confirme sua senha: ')

                    self.login(username, password)

                elif option == 999:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")

            else:
                print('\n*** MENU ***')
                print('1 para editar usuario.')
                print('2 para remover usuario.')
                print('3 para deslogar.')
                print('4 para criar um anúncio')
                print('5 para deletar um anúncio')
                print('6 para mostrar anúncios existentes.')
                print('7 para favoritar um anúncio.')
                print('8 para mostrar lista de favoritos de um usuário.')
                print('9 para escrever um feedback.')
                print('10 para listar os feedbacks de um usuário.')
                print('11 para listar os feedbacks de um anúncio.')
                print('12 para ver suas notificações.')
                print('13 para enviar um email ao prestador de serviço.')


                print('999 para mostrar usuarios cadastrados.')
                
                try:
                    option = int(input ('\nSelect option: '))
                except ValueError:
                    print("Opção inválida.\n")
                    continue


                if option == 1:
                    self.edit_user()
                
                elif option == 2:
                    self.delete_user()
                
                elif option == 3:
                    self.logout()

                elif option == 4:
                    user = self.users[self.logged_username]
                    category = input('Qual a categoria do serviço? ')
                    description = input('Descreva o serviço: ')

                    try:
                        price = float(input('Qual o preço do serviço? R$'))
                    except ValueError:
                        print("Valor deve ser numérico.\n")
                        continue

                    ad_id = user.create_ad(self.ads_dict, category, description, price)

                    for user in self.users:
                        if self.users[user].username != self.logged_username:
                            self.users[user].notification.append(ad_id)

                elif option == 5:
                    try:
                        id = int(input('Digite o ID do anúncio a ser deletado: '))
                    except ValueError:
                        print("O ID deve ser numérico!")
                        continue

                    user = self.users[self.logged_username]
                    user.delete_ad(id, self.ads_dict, self.logged_username)
                elif option == 6:
                    for id, ad in self.ads_dict.items():
                        print(f"ID: {id}")
                        print(f"Username: {ad.username}")
                        print(f"Categoria: {ad.category}")
                        print(f"Description: {ad.description}")
                        print(f"Price: R${ad.price}\n")
                             
                elif option == 7:
                    self.add_favorite()    

                elif option == 8:
                    user = self.users[self.logged_username]
                    user.print_favs(self.logged_username)         

                elif option == 9:
                    try:
                        ad_id = int(input('Digite o ID do anúncio que você deseja dar um feedback: '))
                    except ValueError:
                        print("O ID deve ser numérico!")
                        continue

                    if self.ads_dict.get(ad_id, None):
                        feedback = input('Digite seu feedback: ')
                        self.add_feedback(ad_id, self.logged_username, feedback)
                    else:
                        print('Este anúncio não existe!\n')

                elif option == 10:
                    username = input('De qual usuário deseja ver os feedbacks?: ')
                    self.users[username].print_fb_by_user(username, self.fb_master_list)

                elif option == 11:
                    try:
                        ad_id = int(input('Qual o id do anúncio que deseja ver os feedbacks?: '))
                    except ValueError:
                        print("O ID deve ser numérico!")
                        continue

                    self.ads_dict[ad_id].print_fb_by_ad(ad_id, self.fb_master_list)

                elif option == 12:
                   self.users[self.logged_username].show_notifications(self.ads_dict, self.logged_username)

                elif option == 13:
                    email_receiver = input('Email do destinatario: ')
                    subject = input('Qual o assunto do seu email? ')
                    print('\nLembre de informar uma forma de contato pessoal para futuro contato com o prestador de serviço.\n')
                    body = input('Digite sua mensagem: ')

                    email = GmailHandler()
                    email.send_email(email_receiver, subject, body)

                elif option == 999:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")
    
    def login(self, username, password):
        user = self.users.get(username, None)
        if user:
            if user.password == password:
                self.logged_username = username
            else:
                print('Senha incorreta! ')
        else:
            print('Usuário nao encontrado! ')
        

    def create_user(self, username, cpf, password):
        if username in self.users:
            print('Este usuário já existe!')
        else:
            user = User(username, cpf, password)
            self.users.update({username: user})
            print('Usuário criado com sucesso!')
        

    def edit_user(self):
        while True:
            print('\nO que deseja mudar?')
            print('1 para usuario')
            print('2 para senha\n')

            try:
                option = int(input("Digite sua opção: "))
                break
            except ValueError:
                print("Opção inválida!")
                continue

        if option == 1:
            self.users[self.logged_username].username = input('Digite um novo nome de usuário: ')
        elif option == 2:
            self.users[self.logged_username].password = input('Digite uma nova senha: ')

            

    def delete_user(self):
        self.users.pop(self.logged_username)
        print(f"Usuário {self.logged_username} removido com sucesso!")
        self.logged_username = None
        
    def logout(self):
        self.logged_username = None

    def add_favorite(self):
        try:
            id = int(input('Digite o ID do anúncio que deseja favoritar: '))
        except ValueError:
            print("O ID deve ser numérico!")
            return None
        
        if self.ads_dict.get(id, None):
            self.users[self.logged_username].favorite.append(id)
            print(self.users[self.logged_username].favorite)
        else:
            print('Esse ID não existe!\n')


    def add_feedback(self, ad_id, feedback):
        feedback = Feedback(ad_id, self.logged_username, feedback)
        fb_id = len(self.fb_master_list) + 1

        self.fb_master_list.append(feedback) # adicionar o feedback na lista master de feedbacks
        # print(', '.join([fb.feedback for fb in self.fb_master_list]))

        self.users[self.logged_username].feedbacks.append(fb_id)
        
        self.ads_dict[ad_id].feedbacks.append(fb_id)
        
        
if __name__ == "__main__":
    app = Application()
    app.start()
