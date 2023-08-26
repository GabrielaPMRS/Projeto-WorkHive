class Ad():
    def __init__(self, username, category, description, price):
        self.username = username
        self.category = category
        self.description = description
        self.price = price
        
        self.feedbacks = []


    def print_fb_by_ad(self, ad_id, fb_master_list):
        print(f"Lista de feedbacks de {ad_id}: ")
        for feedback in self.feedbacks:
            print(f"Usuário: {fb_master_list[feedback - 1].username}: {fb_master_list[feedback - 1].feedback}")
