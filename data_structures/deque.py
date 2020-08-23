class Deque():
    def __init__(self):
        self._deque = []
        self._count = 0

    def __str__(self):
        return str(self._deque)

    def __len__(self):
        return len(self._deque)

    def count(self):
        return self._count

    def push_back(self, item):
        self._count += 1
        self._deque.append(item)
        return item

    def push_front(self, item):
        self._count += 1
        self._deque.insert(0, item)
        return item

    def pop_back(self):
        if self.count() > 0:
            self._count -= 1
            temp = self._deque[-1]
            del self._deque[-1]
            return temp

    def pop_front(self):
        if self.count() > 0:
            self._count -= 1
            temp = self._deque[0]
            del self._deque[0]
            return temp

    def contains(self, item):
        return item in self._deque

    def copy(self):
        return [item for item in self._deque]

    def clear(self):
        self._count = 0
        del self._deque[:]
