class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        print self.miles + 10
        return self
    def reverse(self):
        print "Reversing"
        print self.miles - 10
        return self

red = Bike("$20", "25mph", 50)
white = Bike("$30", "30mph", 20)
blue = Bike("40", "35mph", 15)

red.ride().ride().ride().reverse().displayInfo()
white.ride().ride().reverse().reverse().displayInfo()
blue.reverse().reverse().reverse().displayInfo()
