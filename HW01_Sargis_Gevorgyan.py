from abc import ABC, abstractmethod
from time import time
import random as rand

class IndexableSet(ABC):
    @abstractmethod
    def add(self, element):
        pass
    @abstractmethod
    def remove(self, element):
        pass
    @abstractmethod
    def contains(self, element):
        pass
    @abstractmethod
    def get(self, index):
        pass
    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def elements(self):
        pass

# first of all inherit from the abstract class "IndexableSet" in order to force implementation of methods

class ListIndexableSet(IndexableSet):
    #initializer taking a list as an input (if not a list then error message is raised),
    #iterating over it, adding elements to our object through .add() method which handles
    #uniqueness of a new element
    def __init__(self, listIndexableSet):
        if not isinstance(listIndexableSet, list):
            raise "Wrong type, enter a list"
        self.__listIndexableSet = list()
        for i in listIndexableSet:
            self.add(i)

    #checks if an element is contained in our object through .contains() method
    #if it is not contained then we will append internal list with our element
    #using built in .append() method
    def add(self, element):
        if not self.contains(element):
            self.__listIndexableSet.append(element)
    #if element is in our object then it will remove it from our internal list
    #through .remove() built in method
    def remove(self, element):
        if not self.contains(element):
            raise "Provided argument is not in the listIndexableSet"
        self.__listIndexableSet.remove(element)
    #.elements() returns a list. if element in this list -> True
    #else -> False
    def contains(self, element):
        return element in self.elements()
    #.elements() returns a list take needed element using indexing
    def get(self, index):
        return self.elements()[index]
    #returns length of internal list
    def size(self):
        return len(self.elements())
    #returns internal list
    def elements(self):
        return self.__listIndexableSet

#further I will not include comments as all of it is almost the same.
#from the differences which I can outline is that indexing in dictionary is handled through a counter and
#for both tuples and dictionaries I create temporary variables holding the object after modification

class DictIndexableSet(IndexableSet):
    def __init__(self, dictIndexableSet):
        if not isinstance(dictIndexableSet, dict):
            raise "Wrong type enter a dictionary"
        self.__dictIndexableSet = dict()
        self.__counter = 0
        for i in dictIndexableSet.values():
            self.add(i)

    def add(self, element):
        if not self.contains(element):
            self.__dictIndexableSet[self.__counter] = element
            self.__counter += 1

    def remove(self, element):
        if not self.contains(element):
            raise "Provided argument is not in the dictIndexableSet"
        temp = {}
        index = 0
        for i in self.elements():
            if i != element:
                temp[index] = i
                index += 1
        self.__dictIndexableSet = temp
        self.__counter -= 1

    def contains(self, element):
        return element in self.elements()

    def get(self, index):
        return self.__dictIndexableSet[index]

    def size(self):
        return self.__counter

    def elements(self):
        return self.__dictIndexableSet.values()

class TupleIndexableSet(IndexableSet):
    def __init__(self, tupleIndexableSet):
        if not isinstance(tupleIndexableSet, tuple):
            raise "Wrong type enter a tuple"
        self.__tupleIndexableSet = tuple()
        for i in tupleIndexableSet:
            self.add(i)

    def add(self, element):
        if not self.contains(element):
            self.__tupleIndexableSet += (element,)

    def remove(self, element):
        if not self.contains(element):
            raise "Provided argument is not in the tupleIndexableSet"
        temp = tuple()
        for i in self.elements():
            if element != i:
                temp += (i,)
        self.__tupleIndexableSet = temp

    def contains(self, element):
        return element in self.elements()

    def get(self, index):
        return self.elements()[index]

    def size(self):
        return len(self.elements())

    def elements(self):
        return self.__tupleIndexableSet

rand_list = [rand.randint(1,10000000) for _ in range(10000)]
rand_dict = {_: rand.randint(1, 10000000) for _ in range(10000)}
rand_tuple = tuple(rand.randint(1, 10000000) for _ in range(10000))
random_500_values = [None, "string", 1.23, False] + [rand.randint(1,1789435) for _ in range(496)]

a = time()
l = ListIndexableSet(rand_list) # We call __init__ which uses .add() on each element
b = time()
print(f"ListIndexableSet for .add() {b - a} s")

a=time()
d = DictIndexableSet(rand_dict)
b=time()
print(f"DictIndexableSet for .add() {b - a} s")

a=time()
t = TupleIndexableSet(rand_tuple)
b=time()
print(f"TupleIndexableSet for .add() {b - a} s")

a=time()
for i in random_500_values:
    l.contains(i)
b=time()
print(f"ListIndexableSet for .contains() {b - a} s")

a=time()
for i in random_500_values:
    d.contains(i)
b=time()
print(f"DictIndexableSet for .contains() {b - a} s")

a=time()
for i in random_500_values:
    t.contains(i)
b=time()
print(f"TupleIndexableSet for .contains() {b - a} s")

a=time()
for i in range(0,500):
    l.get(i)
b=time()
print(f"ListIndexableSet for .get() {b - a} s")

a=time()
for i in range(0,500):
    d.get(i)
b=time()
print(f"DictIndexableSet for .get() {b - a} s")

a=time()
for i in range(0,500):
    t.get(i)
b=time()
print(f"TupleIndexableSet for .get() {b - a} s")

unq = rand.sample(list(set(rand_list)), k = 500)
a=time()
for i in unq:
    l.remove(i)
b=time()
print(f"ListIndexableSet for .remove() {b - a} s")

unq = rand.sample(list(set(rand_dict.values())), k = 500)
a=time()
for i in unq:
    d.remove(i)
b=time()
print(f"DictIndexableSet for .remove() {b - a} s")

unq = rand.sample(list(set(rand_tuple)), k =500)
a=time()
for i in unq:
    t.remove(i)
b=time()
print(f"TupleIndexableSet for .remove() {b - a} s")
