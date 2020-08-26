class Queue():
    def __init__(self):
        self._queue = []

    def __str__(self):
        return str(self._queue)
    
    def __len__(self):
        return len(self._queue)
    
    def peek(self):
        if len(self._queue) > 0:
            return self._queue[-1]

    def enqueue(self, item):
        self._queue.insert(0, item)
    
    def dequeue(self):
        if len(self._queue) > 0:
            return self._queue.pop()
    
    def contains(self, item): 
        return item in self._queue
    
    def copy(self):
        return [item for item in self._queue]

    def clear(self):
        self._queue = []
    