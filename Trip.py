from http.client import PAYMENT_REQUIRED
from tokenize import Double
from user import user


class Trip:
    id          =str
    user        =user
    car         =str
    route       =str
    amount      =str
    payment     =str
    progress    =str
    completed   =str
    
    print       = print(vars())