class User():
    def __init__(self, username, cpf, password):
        self.username = username
        self.cpf = cpf
        self.password = password




if __name__ == "__main__":
    user1 = User('Gabi', '06348242447', '123')
    print(user1.username)    


    user2 = User('Arthur', '0634824xxx7', '123')
    print(user2.username)  
