from Ad import Ad

class User():
    
    def __init__(self, username, cpf, password):
        self.username = username
        self.cpf = cpf
        self.password = password

        self.favorite = []
        self.feedbacks = []

    def create_ad(self, ads_dict, category, description, price):
        ad = Ad(self.username, category, description, price)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id} criado com sucesso!\n")

    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            if ads_dict[id].username == logged_username:
                ads_dict.pop(id)
                print(f"Anúncio de id: {id} removido com sucesso!\n")
            else:
                print("Usuário não tem acesso para remover o anúncio!\n")
        else:
            print(f"O id: {id} não exite!\n")


    def print_favs(self, logged_username):
        print(f"Lista de favoritos de {logged_username}: {self.favorite}")


    def print_fb_by_user(self, username, fb_master_list):
        print(f"Lista de feedbacks de {username}: ")
        for feedback in self.feedbacks:
            print(f"Anúncio: {fb_master_list[feedback - 1].ad_id}: {fb_master_list[feedback - 1].feedback}")

if __name__ == "__main__":
    user1 = User('Gabi', '06348242447', '123')
    print(user1.username)    


    user2 = User('Arthur', '0634824xxx7', '123')
    print(user2.username)  
