# importing copy module
import copy
import itertools


class Stack(object):
    "An iterable object."

    """I used the stack implementation from the PYTHONDS library"""
    """https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html"""
    """The module can be downloaded from GitHub. or installed from """
    """the command line using pip install pythonds."""
    """Scott Bing  04/01/2020"""

    items = []

    def __init__(self, maximum):
        self.maximum = maximum
        self.items = []
        # self.items = [0] * 10

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __iter__(self):
        return StackIterator(self)

    def createIterator(self):
        return StackIterator(self)

    def __eq__(self, other):
        # print("I'm in the overloaded '==' function.")
        itl = self.createIterator()
        itr = other.createIterator()

        """use the iterator to comapre the stacks"""
        if self.size() == other.size():
            for s, o in itertools.zip_longest(self.items, other.items):
                if s != o:
                    return False
            return True
        else:
            return False


class StackIterator(object):
    """An iterator."""

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 1
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def currentItem(self):
        return self.n

    def __iter__(self):
        return self


if __name__ == '__main__':

    """Establish an initial stack"""
    s1 = Stack(7)

    for i in range(1, 5):
        s1.push(i)

    """Duplicate the stacks into different objects"""
    s2 = copy.deepcopy(s1)
    s3 = copy.deepcopy(s1)
    s4 = copy.deepcopy(s1)
    s5 = copy.deepcopy(s1)

    """Perform some stack operations to alter the original stack"""
    s3.pop()
    s4.push(9)
    s5.pop()
    s5.pop()
    s5.push(6)

    """Compare stacks and print the results"""
    print("1 == 2", (s1 == s2))
    print("1 == 3", (s1 == s3))
    print("1 == 4", (s1 == s4))
    print("1 == 5", (s1 == s5))
