from Ad import Ad
from Ad import OfferAd
from Ad import LookingForAd
from Notification import Notification

class User():
    
    def __init__(self, username, cpf, password):
        self._username = username
        self._cpf = cpf
        self._password = password

        self.favorite = []
        self.feedbacks = []
        self.notification = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    @property
    def cpf(self):
        return self._cpf
   

    def create_OfferAd(self, ads_dict, category, description, price):
        ad = OfferAd(self._username, category, description, price)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id} criado com sucesso!\n")

        return ad_id
    
    def create_LookingForAd(self, ads_dict, category, description):
        ad = LookingForAd(self._username, category, description)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id} criado com sucesso!\n")

        return ad_id

    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            if ads_dict[id].username == logged_username:
                ads_dict.pop(id)
                print(f"Anúncio de id: {id} removido com sucesso!\n")
            else:
                print("Usuário não tem acesso para remover o anúncio!\n")
        else:
            print(f"O id: {id} não exite!\n")

    def print_favs(self, logged_username, ads_dict):
        if len(self.favorite) != 0:
            print(f"\nLista de favoritos de {logged_username}:")
            for fav in self.favorite:
                fav_ad = ads_dict[fav]
                print(f"ID: {fav}")
                print(f"Username: {fav_ad.username}")
                print(f"Categoria: {fav_ad.category}")
                print(f"Description: {fav_ad.description}")
                print(f"Price: R${fav_ad.price}\n")

        else:
            print("Esse usuário não possui anúncios favoritados\n")

    def print_fb_by_user(self, username, fb_master_list):
        if len(self.feedbacks) != 0:
            print(f"Lista de feedbacks de {username}: ")
            for feedback in self.feedbacks:
                print(f"Anúncio: {fb_master_list[feedback - 1].ad_id}: {fb_master_list[feedback - 1].feedback}")
        else:
            print("Esse usuário não fez nenhum feedback\n")

    def show_notifications(self, ads_dict):
        if len(self.notification) == 0: 
            print("Você tem 0 notificações\n")
            return
        else:
            print(f"Você tem {len(self.notification)} notificação(ões)")

            for notification in self.notification:
                print(f"Usuário: {ads_dict[notification].username}\nDescrição: {ads_dict[notification].description}\n")

        self.notification.clear()

if __name__ == "__main__":
    user1 = User('Gabi', '06348242447', '123')
    print(user1.username)    

    user2 = User('Arthur', '0634824xxx7', '123')
    print(user2.username)  
