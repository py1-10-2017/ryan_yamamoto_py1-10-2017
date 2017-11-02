class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price is:", "$", str(self.price)
        print "MPH is:", self.speed, "miles per hour"
        print "Tank is:", self.fuel
        print "Mileage is:", str(self.mileage), "miles per gallon"
        print "Tax is:", str(self.tax * 100), "%"

car1 = Car(11000, "120mph", "empty", 50000)
car1.display_all()
car2 = Car(6000, "115mph", "half tank", 40000)
car2.display_all()
car3 = Car(9000, "130mph", "full tank", 100000)
car3.display_all()
car4 = Car(14000, "140mph", "empty", 20000)
car4.display_all()
car5 = Car(15000, "150mph", "half tank", 10000)
car5.display_all()
car6 = Car(16000, "160mph", "full tank", 8000)
car6.display_all()
