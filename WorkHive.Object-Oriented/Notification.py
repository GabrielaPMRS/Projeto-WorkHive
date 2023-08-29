class Notification():
    def __init__(self, username, feedback):
        self._username = username
        self._feedback = feedback

    @property
    def username(self):
        return self._username
    
    @property
    def feedback(self):
        return self._feedback
    