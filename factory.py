__author__ = 'Saturn'

'''

Hamburg Factory to make kinds of burg:

    -ChickenBurg
    -FishBurg
    -BeefBurg

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

class HamburgFactory:
    def makeHamburg(self, typeofburg):
        if typeofburg == "chicken":
            return ChickenBurg()
        if typeofburg == "fish":
            return FishBurg()
        if typeofburg == "beef":
            return BeefBurg()
        return  UndefBurg()

if "__main__" == __name__:
    burgFactory = HamburgFactory()
    hamburg = burgFactory.makeHamburg("chicken")
    hamburg.getName()
    hamburg = burgFactory.makeHamburg("fish")
    hamburg.getName()
    hamburg = burgFactory.makeHamburg("beef2")
    hamburg.getName()
