__author__ = 'Saturn Lee'

'''
Prototype pattern refers to creating 'DUPLICATE object' while keeping performance in mind.

This type of design pattern comes under creational pattern
    as this pattern provides one of the best way to create an object.

This pattern involves implementing a prototype interface
    which tells to create a clone of the current object.

This pattern is used when creation of object directly is costly.
    For example, a object is to be created after a costly database operation.

We can cache the object, returns its clone on next request
    and update the database as as and when needed thus reducing database calls.

Implementation
    We're going to create an abstract class Hamburg and concrete classes extending the Hamburgbase class.
    A class BurgCache is defined as a next step which stores hamburg objects
        in a Hashtable and returns their clone when requested.
'''

import copy

id = 1

class HamburgBase:
    def __init__(self):
        global id
        self.id = id
        id += 1

    def getName(self):
        pass
    def getID(self):
        return self.id

class ChickenBurg(HamburgBase):

    def __init__(self):
        HamburgBase.__init__(self)
        self.name = "Chicken Burg"

    def getName(self):
        return self.name

    def getID(self):
        return self.id

class FishBurg(HamburgBase):

    def __init__(self):
        HamburgBase.__init__(self)
        self.name = "Fish Burg"

    def getName(self):
        return self.name

class BeefBurg(HamburgBase):

    def __init__(self):
        HamburgBase.__init__(self)
        self.name = "Beef Burg"

    def getName(self):
        return self.name

class UndefBurg(HamburgBase):
    def __init__(self):
        HamburgBase.__init__(self)
        self.name = "Undefined Burg"

    def getName(self):
        return "Undefined Burg"

class HamburgCache:
    def __init__(self):
        self.cache = {}
        self.cache["chicken"] = ChickenBurg()
        self.cache["beef"] = BeefBurg()
        self.cache["fish"] = FishBurg()
        self.cache["undef"] = UndefBurg()

    def makeHamburg(self, typeofburg):

        if typeofburg in self.cache:
            return copy.copy(self.cache[typeofburg])
            # if typeofburg == "chicken":
            #     return ChickenBurg()
            # if typeofburg == "fish":
            #     return FishBurg()
            # if typeofburg == "beef":
            #     return BeefBurg()
        return  copy.copy(self.cache["undef"])

if "__main__" == __name__:

    burgFactory = HamburgCache()
    hamburg = burgFactory.makeHamburg("chicken")
    print hamburg.getName()
    print hamburg.getID()
    hamburg = burgFactory.makeHamburg("fish")
    print hamburg.getName()
    print hamburg.getID()
    hamburg = burgFactory.makeHamburg("beef2")
    print hamburg.getName()
    print hamburg.getID()