#Unique type class to decipher between attributes
class Helper:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return str(self.value)
