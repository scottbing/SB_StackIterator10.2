# importing copy module
import copy


class Stack(object):
    "An iterable object."

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

        # Debugging only
        # for n in self.items:
        #     if n != 0:
        #         print(str(n) + " in == ", end='')
        # print()

        if self.size() == other.size():
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

    s1 = Stack(7)

    for i in range(1, 5):
        s1.push(i)

    # Debugging only
    # for n in s1.items:
    #     if n != 0:
    #         print(str(n) + " ", end='')
    # print()

    """Duplicate the stacks inot different objects"""
    s2 = copy.deepcopy(s1)
    s3 = copy.deepcopy(s1)
    s4 = copy.deepcopy(s1)
    s5 = copy.deepcopy(s1)

    # Debugging only
    # for n in s2.items:
    #     if n != 0:
    #         print(str(n) + " ", end='')
    # print()

    s3.pop()

    # Debugging only
    # for n in s3.items:
    #     if n != 0:
    #         print(str(n) + " ", end='')
    # print()

    s4.push(9)

    # Debugging only
    # for n in s4.items:
    #     if n != 0:
    #         print(str(n) + " ", end='')
    # print()

    s5.pop()
    s5.pop()
    s5.push(6)

    # Debugging only
    # for n in s5.items:
    #     if n != 0:
    #         print(str(n) + " ", end='')
    # print()

    """Compare stacks"""
    print("1 == 2", (s1 == s2))
    print("1 == 3", (s1 == s3))
    print("1 == 4", (s1 == s4))
    print("1 == 5", (s1 == s5))
