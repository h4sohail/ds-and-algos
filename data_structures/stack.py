class Stack():
    def __init__(self):
        self._count = 0
        self._stack = []
    
    def __str__(self):
        return str(self._stack)

    def count(self):
        return count

    def peek(self):
        if (len(self._stack) != 0):
            return self._stack[0]
        else:
            return []

    def push(self, data):
        self._count += 1
        self._stack.append(data)

    def pop(self):
        if len(self._stack) != 0:
            self._count -= 1
            temp = self._stack[-1]
            del self._stack[-1]
            return temp

    def free(self):
        self._count = 0
        del self._stack[:]

    def contains(self, item):
       return item in self._stack

