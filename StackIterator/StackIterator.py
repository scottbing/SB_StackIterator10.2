class Stack(object):
    "An iterable object."

    def __init__(self, maximum):
        self.maximum = maximum

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


class StackIterator(object):
    "An iterator."

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


if __name__ == '__main__':

    numbers = Stack(7)

    for n in numbers:
        print(n)
