__author__ = 'Saturn'

'''
Creational design pattern

Unlike Factory design patter, builder can create more complex composite object
    Factory Design Patter tends to create single item
    Builder tends to create a composite of items, to make code flexible

'''

class Item:
    def getPrice(self):
        pass
    def getPacked(self):
        pass
    def getName(self):
        pass

class Packing:
    def getPackType(self):
        pass

class Bottle(Packing):
    def getPackType(self):
        return "Bottle"

class Warp(Packing):
    def getPackType(self):
        return "Warp"

class HamburgBase(Item):
    def getPackingType(self):
        return Warp().getPackType()

class DrinkingBase(Item):
    def getPackingType(self):
        return Bottle().getPackType()

class ChickenBurg(HamburgBase):
    def getName(self):
        return "Chicken Burg"
    def getPrice(self):
        return 12

class FishBurg(HamburgBase):
    def getName(self):
        return "Fish Burg"
    def getPrice(self):
        return 14

class BeefBurg(HamburgBase):
    def getName(self):
        return "Beef Burg"
    def getPrice(self):
        return 10

class Coke(DrinkingBase):
    def getName(self):
        return "coke"
    def getPrice(self):
        return 10

class Pepsi(DrinkingBase):
    def getName(self):
        return "pepsi"
    def getPrice(self):
        return 10

class Tea(DrinkingBase):
    def getName(self):
        return "black tea"
    def getPrice(self):
        return 14

class Meal:
    def __init__(self, name):
        self.items = []
        self.mealName = name
    def additem(self, i):
        self.items.append(i)
    def displayItems(self):
        print self.mealName , " :"
        for i in self.items:
            print "item ", i.getName()
            print "\tprice ", i.getPrice()
            print "\tpacking ", i.getPackingType()
    def getTotalCosts(self):
        print "Cost of ", self.mealName
        total = 0
        for i in self.items:
            total += i.getPrice()

        print total

class MealBuilder:
    def getChickenSet(self):
        hamburg = ChickenBurg()
        drinking = Coke()
        drinking2 = Tea()
        chichenMeal = Meal("Chicken Meal")
        chichenMeal.additem(hamburg)
        chichenMeal.additem(drinking)
        chichenMeal.additem(drinking2)
        return chichenMeal

    def getBeefSet(self):
        hamburg = BeefBurg()
        hamburg2 = BeefBurg()
        drinking = Pepsi()
        beefMeal = Meal("Beef Meal")
        beefMeal.additem(hamburg)
        beefMeal.additem(hamburg2)
        beefMeal.additem(drinking)
        return beefMeal

if "__main__" == __name__:
    mealMaker = MealBuilder()
    chickenMeal = mealMaker.getBeefSet()
    chickenMeal.displayItems()
    chickenMeal.getTotalCosts()