



from datetime import date


class card:
    
    id          =str
    number      =int
    cvv         =int
    date        =str
    
    def __init__(self, id, number, cvv, date):
        self.id         = id
        self.number     =number
        self.cvv        =cvv
        self.date       =date