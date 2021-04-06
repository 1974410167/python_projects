import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        self.list_size = 0
        self.dict = defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        self.list_size += 1

        if val in self.dict.keys():
            self.dict[val].append(self.list_size - 1)
            return False
        else:
            self.dict[val].append(self.list_size - 1)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dict.keys():
            t = self.dict[val].pop()
            if len(self.dict[val]) == 0:
                del self.dict[val]
            self.list.pop(t)

            return True

        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """

        t = random.choice(self.list)
        return t

s = RandomizedCollection()

print(s.insert(2))
print(s.list)
print(s.dict)
print(s.insert(3))
print(s.insert(4))
print(s.insert(2))
print(s.list)
print(s.dict)
print(s.remove(2))
print(s.list)
print(s.dict)
print(s.remove(2))
print(s.list)
print(s.dict)

print(s.getRandom())



