from lib2to3.pgen2 import driver
from pprint import pprint
from PayPal import PayPal
from Trip import Trip
from UberBlack import UberBlack
from UberPool import UberPool
from UberVan import UberVan
from car import car
from card import card
from cash import cash
from route import route
from uberX import uberX
from user import user


if __name__ == "_main_":
    print("hola mundo")
    

    
    carro = car()
    car.id          = 5
    car.brand       ="toyota"
    car.driver      ="Adrian"
    car.passager    = 5
    car.printAll(car)

pprint(vars(car))

car2 = car()
car2.id           = 5
car2.brand        ="kya"
car2.driver       ="sad"
car2.passager     = 4

pprint((car2))

users = user()
user.id           =10
user.name         ="Muñoz"
user.document     ="Carpeta"
user.email        ="adrianmesias0@gmail.com"
user.password     ="12345"

pprint(vars(user))

routes  =   route()
route.id        =3
route.start     ="go"
route.end       ="Fin"

pprint(vars(route))

Trips =   Trip()
Trip.id         =12
Trip.user       ="Carlos"
Trip.car        ="Aveo"
Trip.route      ="Routes"
Trip.amount     ="$20"
Trip.payment    ="Efectivo"
Trip.progress   ="largo"
Trip.completed  ="Excelent"

pprint(vars(Trip))

ubersX =   uberX()
uberX.id         =50
uberX.license    ="militar"
uberX.driver     ="auto"
uberX.passengers =45
uberX.brand      ="GH"
uberX.model      ="chica"

pprint(vars(uberX))

UbersPool =   UberPool()
UberPool.id         =100
UberPool.license    ="Policia"
UberPool.driver     ="coche"
UberPool.passengers =22
UberPool.brand      ="Aveo"
UberPool.model      ="chico"

pprint(vars(UberPool))

UbersBlack =   UberBlack()
UberBlack.id         =112
UberBlack.license    ="Licenciada"
UberBlack.driver     ="bus"
UberBlack.passengers =39

pprint(vars(UberBlack))

UbersVan =   UberVan()
UberVan.id         =110
UberVan.license    ="Coach"
UberVan.driver     ="auto bus"
UberVan.passengers =34

pprint(vars(UberVan))

cards =   card()
card.id         =200
card.number     =44
card.cvv        ="Adrian"
card.date       ="22-04-2022"

pprint(vars(card))

PayPals =   PayPal()
PayPal.id         =200
PayPal.email      ="das.munoz@yavirac.edu.ec"

pprint(vars(PayPal))


cashs =   cash()
cash.id         =2

pprint(vars(cash))