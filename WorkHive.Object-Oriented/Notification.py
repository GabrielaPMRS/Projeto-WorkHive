import time

class Notification():
    def __init__(self, ad_id):
        self._ad_id = ad_id
        self._created_at = time.time()
        
    @property
    def ad_id(self):
        return self._ad_id
    
    @property
    def created_at(self):
        return self._created_at
