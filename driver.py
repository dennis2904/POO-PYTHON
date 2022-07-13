from account import Account

class driver(Account):
    id          = int
    license     = str
    
    def _init_(self, name, document, mail, Password, gender, numberCell, age):
        super()._init_(name, document, mail, Password, gender, numberCell, age)
        
        self.id             = id
        self.license        = license