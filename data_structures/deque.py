class Deque():
    def __init__(self):
        self._deque = []
        self._count = 0

    def __str__(self):
        return str(self._deque)


    def count(self):
        return count

    def push_back(self, item):
        self._count += 1
        self._deque.append(item)
        return item

    def push_front(self, item):
        self._count += 1
        self._deque.insert(0, item)
        return item

    def pop_back(self):
        if(len(self._deque) != 0):
            self._count -= 1
            temp = self._deque[-1]
            del self._deque[-1]
            return temp

    def pop_front(self):
        if(len(self._deque) != 0):
            self._count -= 1
            temp = self._deque[0]
            del self._deque[0]
            return temp

    def contains(self, item):
        return item in self._deque

    def copy(self):
        return [item for item in self._deque]

    def clear(self):
        del self._deque[:]
