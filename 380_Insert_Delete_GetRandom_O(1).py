class RandomizedSet(object):
    """ The amortized time complexity of add/remove from array/hashmap is O(1).
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.array = list()
        self.size = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = self.size
        if self.size < len(self.array):
            self.array[self.size] = val
        else:
            self.array.append(val)
        self.size += 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        index = self.map[val]
        del self.map[val]
        if index != self.size-1:
            tail_val = self.array[self.size-1]
            self.array[index] = tail_val
            self.map[tail_val] = index #
        self.size -= 1
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.size:
            return None
        from random import randint
        index = randint(0, self.size-1)
        return self.array[index]
