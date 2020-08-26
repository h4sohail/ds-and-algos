class Deque():
    def __init__(self):
        self._deque = []

    def __str__(self):
        return str(self._deque)

    def __len__(self):
        return len(self._deque)

    def push_back(self, item):
        self._deque.append(item)
        return item

    def push_front(self, item):
        self._deque.insert(0, item)
        return item

    def pop_back(self):
        if len(self._deque) > 0:
            return self._deque.pop()

    def pop_front(self):
        if len(self._deque) > 0:
            return self._deque.pop(0)

    def contains(self, item):
        return item in self._deque

    def copy(self):
        return [item for item in self._deque]

    def clear(self):
        self._deque = []
