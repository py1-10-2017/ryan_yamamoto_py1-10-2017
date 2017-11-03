class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Animal's health:", self.health

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        print self.health
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        print self.health
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"



animal = Animal("Peanut", 100)
animal.walk().walk().walk().run().run().display_health()
dog = Dog("Butter", 50)
dog.pet()
dog.walk().walk().walk().run().run().pet().display_health()
dragon = Dragon("Jelly", 
