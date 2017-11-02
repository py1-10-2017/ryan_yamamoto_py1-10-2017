class Product(object):
    def __init__(self, price, item_name, weight, brand, status = "For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def display_all(self):
        print "Price:", "$", self.price
        print "Item name:", self.item_name
        print "Weight:", self.weight, "lbs"
        print "Brand:", self.brand
        print "Status:", self.status
        return self

    def sell(self):
        print "SOLD!"
        return self

    def add_tax(self, tax):
        tax = tax * self.price
        print "With tax:", "$", self.price + tax
        return self

    def returns(self, condition):
        if condition == "defective":
            self.status = "defective"
            self.price = 0
            print self.status, self.price
        else:
            if condition == "like new":
                self.status = "For Sale"
                print self.status
            elif condition == "used":
                self.status = "Used"
                discount = self.price * 0.2
                self.price = self.price - discount
                print self.status, self.price
        return self



prod = Product(25, "Toaster", 5, "Black & Decker")
prod.display_all()
