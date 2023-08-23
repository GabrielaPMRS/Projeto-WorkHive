# Manager class
from User import User
from Ad import Ad

class Manager():
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

    def start(self):
        while True:

            if self.logged_username == None:
                print('\n*** MENU ***')
                print('1 para criar usuario.')
                print('2 para fazer login.')
                print('999 para mostrar usuarios cadastrados.')


                option = int(input ('\nSelect option: '))

                if option == 1:
                    username = input('Digite seu nome de usuario: ')
                    cpf = input('Digite seu cpf (apenas números): ')
                    password = input('Crie sua senha (apenas números): ')

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
                print('6 para mostrar anúncios existentes')
                print('999 para mostrar usuarios cadastrados.')
                

                option = int(input ('\nSelect option: '))

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
                    price = float(input('Qual o preço do serviço? R$'))

                    user.create_ad(self.ads_dict, category, description, price)

                elif option == 5:
                    id = int(input('Digite o ID do anúncio a ser deletado! '))
                    user = self.users[self.logged_username]

                    user.delete_ad(id, self.ads_dict, self.logged_username)

                    
                    

                elif option == 6:
                    for id, ad in self.ads_dict.items():
                        print(f"ID: {id}")
                        print(f"Username: {ad.username}")
                        print(f"Categoria: {ad.category}")
                        print(f"Description: {ad.description}")
                        print(f"Price: R${ad.price}\n")
                        
                        
                        

                elif option == 999:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")

                 


    def login(self, username, password):
        user = self.users.get(username,None)
        if user:
            if user.password == password:
                self.logged_username = username
            else:
                print('Senha incorreta! ')
        else:
            print('Usuario nao encontrado! ')
        

    def create_user(self, username, cpf, password):
        if username in self.users:
            print('Este usuario ja existe!')
        else:
            user = User(username, cpf, password)
            self.users.update({username: user})
            print('Usuario criado com sucesso!')
        

    def edit_user(self):
        print('\nO que deseja mudar?')
        print('1 para usuario')
        print('2 para senha\n')
        option = int(input("Digite sua opção: "))

        if option == 1:
            self.users[self.logged_username].username = input('Digite um novo nome de usuario: ')
        if option == 2:
            self.users[self.logged_username].password = input('Digite uma nova senha: ')


    def delete_user(self):
        self.users.pop(self.logged_username)
        print(f"Usuario {self.logged_username} removido com sucesso!")
        self.logged_username = None
        
        
    def logout(self):
        self.logged_username = None



if __name__ == "__main__":
    manager = Manager()
    manager.start()
