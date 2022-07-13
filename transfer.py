from payment import payment
from bank import bank

class tranfer(payment, bank):
    def _init_(self, id, ammount, bank, identification, numberAccount):
        super()._init_(id, ammount, bank, identification, numberAccount)