__author__ = 'Saturn'

'''

the same like factory design pattern
difference is that factory class is also an abstract class.

'''


class HamburgBase:
    def getName(self):
        pass

class ChickenBurg(HamburgBase):
    def getName(self):
        print "Chicken Burg"

class FishBurg(HamburgBase):
    def getName(self):
        print "Fish Burg"

class BeefBurg(HamburgBase):
    def getName(self):
        print "Beef Burg"

class UndefBurg(HamburgBase):
    def getName(self):
        print "Undefined Hamburg"

class DrinkingBase:
    def getName(self):
        pass

class Coke(DrinkingBase):
    def getName(self):
        print "Coke"

class Pepsi(DrinkingBase):
    def getName(self):
        print "pepsi"

class Tea(DrinkingBase):
    def getName(self):
        print "Black Tea"

class UndefDrinking(DrinkingBase):
    def getName(self):
        print "Undefined Drinking"

class FactoryBase:
    def getHamburg(self, typeofburg):
        pass
    def getDrinking(self, typeofdrink):
        pass

class HamburgFactory(FactoryBase):
    def getHamburg(self, typeofburg):
        if typeofburg == "chicken":
            return ChickenBurg()
        if typeofburg == "fish":
            return FishBurg()
        if typeofburg == "beef":
            return BeefBurg()
        return  UndefBurg()

class DrinkingFactory(FactoryBase):
    def getDrinking(self, typeofdrink):
        if typeofdrink == "coke":
            return Coke()
        if typeofdrink == "pepsi":
            return Pepsi()
        if typeofdrink == "tea":
            return Tea()
        return  UndefDrinking()

class FactoryProducer:
    def getFactory(self, typeoffactory):
        if typeoffactory == "drinking":
            return DrinkingFactory()
        if typeoffactory == "hamburg":
            return HamburgFactory()

        print "Factory Undefined"

if "__main__" == __name__:
    factoryProducer = FactoryProducer()

    hamburgFactory = factoryProducer.getFactory("drinking")
    cock = hamburgFactory.getDrinking("coke")
    cock.getName()