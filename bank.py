from payment import payment

class Bank(payment):
    bank            =str
    identification  =str
    numberAccount   =int
      
    def _init_(self, id, ammount, bank, identification, numberAccount):
        super()._init_(id, ammount)
        self.bank           =bank
        self.identification =identification
        self.numberAccount  =numberAccount