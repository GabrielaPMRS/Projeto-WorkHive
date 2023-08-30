class Ad():
    def __init__(self, username, category, description, price):
        self._username = username
        self._category = category
        self._description = description
        self._price = price

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
    
    @property
    def price(self):
        return self._price
        
    def print_fb_by_ad(self, ad_id, fb_master_list):
        if len(self.feedbacks) != 0:
            print(f"Lista de feedbacks do anúncio {ad_id}: ")
            for feedback in self.feedbacks:
                print(f"Usuário: {fb_master_list[feedback - 1].username}: {fb_master_list[feedback - 1].feedback}")
        else:
            print("Esse anúncio não possui feedbacks\n")