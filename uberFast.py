from pyexpat import model
from car import car
from cash import cash 

class uberFast(car):
    
   brand           =str
   model           =str
   loadSize        =[]
   loadWeight      =int

def __init__(self, license, driver, brand, model, loadSize, loadWeight):
        super.__init__(license, driver)
        self.brand        =brand
        self.model        =model
        self.loadSize     =loadSize
        self.loadWeight   =loadWeight