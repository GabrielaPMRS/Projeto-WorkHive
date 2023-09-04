class Ad():
    def __init__(self, username, category, description):
        self._username = username
        self._category = category
        self._description = description

        self.feedbacks = []

    @property
    def username(self):
        return self._username  
    
    @property
    def category(self):
        return self._category  
    
    @property
    def description(self):
        return self._description
    
        
    def print_fb_by_ad(self, ad_id, fb_master_list):
        if len(self.feedbacks) != 0:
            print(f"Lista de feedbacks do anúncio {ad_id}: ")
            for feedback in self.feedbacks:
                print(f"Usuário: {fb_master_list[feedback - 1].username}: {fb_master_list[feedback - 1].feedback}")
        else:
            print("Esse anúncio não possui feedbacks\n")

    def PrintAds(self, ad_id):
        return None
            
        
class OfferAd(Ad):
    def __init__(self, username, category, description, price):
        super().__init__(username, category, description)
        self._price = price

    @property
    def price(self):
        return self._price
    
    def PrintAds(self, ad_id):
        print("Anúncio de oferta de serviço:")
        print(f"ID: {ad_id}")
        print(f"Username: {self.username}")
        print(f"Categoria: {self.category}")
        print(f"Description: {self.description}")
        print(f"Price: R${self.price}\n")


class LookingForAd(Ad):
    def __init__(self, username, category, description):
        super().__init__(username, category, description)

    def PrintAds(self, ad_id):
        print("Anúncio de procura por serviço:")
        print(f"ID: {ad_id}")
        print(f"Username: {self.username}")
        print(f"Categoria: {self.category}")
        print(f"Description: {self.description}\n")