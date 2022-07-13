from lib2to3.pgen2 import driver
from pyexpat import model


class UberPool:
    id          =str
    license     =str
    driver      =str
    passengers  =int
    brand       =str
    model       =str
    
    print       =print(vars())