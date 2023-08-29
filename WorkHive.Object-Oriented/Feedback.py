class Feedback():
    def __init__(self, ad_id, username, feedback):
        self._feedback = feedback
        self._ad_id = ad_id
        self._username = username

    @property
    def feedback(self):
        return self._feedback
    
    @property
    def ad_id(self):
        return self._ad_id

    @property
    def username(self):
        return self._username
    
    