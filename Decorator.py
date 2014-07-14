__author__ = 'Saturn'

'''
Hamburg -> subclass -> Chicken Hamburg & Fish Hamburg

and

its Decorator -> Kithcup & Cheese
'''
class Hamburg:
    '''Component Interface'''
    def getContent(self):
        pass

    def getPrice(self):
        pass

class ChickenHamburg(Hamburg):
    '''Concrete Component'''
    def __init__(self):
        self.content = "Ordinary Chicken Hamburg"
        self.price = 12

    def getContent(self):
        #print "Consisting of: " + self.content
        return self.content

    def getPrice(self):
        print self.content + ", " + str( self.price )
        return self.price

class FishHamburg(Hamburg):
    '''Concrete Component'''
    def __init__(self):
        self.content = "Ordinary Fish Hamburg"
        self.price = 14

    def getContent(self):
        #print "Consisting of: " + self.content
        return self.content

    def getPrice(self):
        print self.content + ", " + str( self.price )
        return self.price

class HamburgDecorator(Hamburg):
    '''Decorator Interface'''
    def __init__(self, target):
        self.hamburg = target

    def getContent(self):
        pass
    def getPrice(self):
        pass

class Kethcup(HamburgDecorator):
    '''Concrete Decorator'''
    def __init__(self, target):
        HamburgDecorator.__init__(self, target)
        self.addcontent = "kethcup"
        self.addprice = 2

    def getContent(self):
        #print "Consisting of: " + self.hamburg.getContent() + "; " + self.addcontent
        return self.hamburg.getContent() + "; " + self.addcontent

    def getPrice(self):
        #print "Price is " + str( self.hamburg.getPrice() + self.addprice )
        print self.addcontent + ", " + str(self.addprice)
        return self.hamburg.getPrice() + self.addprice

class Cheese(HamburgDecorator):
    '''Concrete Decorator'''
    def __init__(self, target):
        HamburgDecorator.__init__(self, target)
        self.addcontent = "cheese"
        self.addprice = 3

    def getContent(self):
        #print "Consisting of: " + self.hamburg.getContent() + "; " + self.addcontent
        return self.hamburg.getContent() + "; " + self.addcontent

    def getPrice(self):
        # print "Price is " + str( self.hamburg.getPrice() + self.addprice )
        print self.addcontent + ", " + str(self.addprice)
        return self.hamburg.getPrice() + self.addprice

if "__main__" == __name__:
    hamburg = ChickenHamburg()

    cheeseadd = Cheese(hamburg)
    cheeseadd2 = Cheese(cheeseadd)

    kethcupadd = Kethcup(cheeseadd2)
    kethcupadd2 = Kethcup(kethcupadd)

    print "Contents : \n" , kethcupadd2.getContent()
    print "Price : \n", kethcupadd2.getPrice()


    fish = FishHamburg()
    cheeseadd = Cheese(fish)

    print "Contents : \n", cheeseadd.getContent()
    print "Price: \n", cheeseadd.getPrice()

# class Person:
#     def __init__(self,tname):
#         self.name = tname
#     def Show(self):
#        print "dressed %s" %(self.name)
#
# class Finery(Person):
#     componet = None
#     def __init__(self):
#         pass
#     def Decorate(self,ct):
#         self.componet = ct
#     def Show(self):
#         if(self.componet!=None):
#             self.componet.Show()
#
# class TShirts(Finery):
#     def __init__(self):
#         pass
#     def Show(self):
#         print "Big T-shirt "
#         self.componet.Show()
#
# class BigTrouser(Finery):
#     def __init__(self):
#         pass
#     def Show(self):
#         print "Big Trouser "
#         self.componet.Show()
#
# if __name__ == "__main__":
#     p = Person("somebody")
#     bt = BigTrouser()
#     ts = TShirts()
#     bt.Decorate(p)
#     ts.Decorate(bt)
#     ts.Show()
