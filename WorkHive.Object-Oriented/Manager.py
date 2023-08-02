# Manager class
from User import User

class Manager():
    def __init__(self):
        self.logged_username = None

        self.users = {
            'Gabi': User('Gabi', '1234556', '123'),
            'Lara': User('Lara', '9876543', '321')
        }

    def start(self):
        while True:

            if self.logged_username == None:
                print('\n*** MENU ***')
                print('1 para criar usuario.')
                print('2 para fazer login.')
                print('3 para mostrar usuarios cadastrados.')


                option = int(input ('\nSelect option: '))

                if option == 1:
                    username = input('Digite seu nome de usuario: ')
                    cpf = input('Digite seu cpf: ')
                    password = input('Crie sua senha: ')

                    self.create_user(username, cpf, password)

                elif option == 2:
                    username = input('Digite seu nome de usuario: ')
                    password = input('Confirme sua senha: ')

                    self.login(username, password)

                elif option == 3:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")

            else:

                print('\n*** MENU ***')
                print('1 para editar usuario.')
                print('2 para remover usuario.')
                print('3 para deslogar.')
                print('4 para mostrar usuarios cadastrados.')
                

                option = int(input ('\nSelect option: '))

                if option == 1:
                    self.edit_user()
                
                elif option == 2:
                    self.delete_user()
                
                elif option == 3:
                    self.logout()

                elif option == 4:
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
