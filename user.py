from account import Account

class user(Account):
    id = int
    
    def __init__(self, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)
        self.id      =id