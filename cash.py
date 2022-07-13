from payment import payment

class cash(payment):
    def _init_(self, id, ammount):
        super()._init_(id, ammount)