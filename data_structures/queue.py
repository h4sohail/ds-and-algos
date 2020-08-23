class Queue():
    def __init__(self):
        self._queue = []
        self._count = 0

    def __str__(self):
        return str(self._queue)
    
    def __len__(self):
        return len(self._queue)
    
    def count(self):
        """The count of items in the queue

        Returns:
            (int): The number of items in the array
        """
        return self._count

    def peek(self):
        """Return the last element in the queue

        Returns:
            item (any): Last element in the queue
        """
        if self.count() > 0:
            return self._queue[-1]

    def enqueue(self, item):
        """Add an item to the end of the queue

        Args:
            item (any): The item from the end of the queue
        """
        self._count += 1
        self._queue.append(item)
    
    def dequeue(self):
        """Remove an element from the start of the queue

        Returns:
            (any): The item from the start of the queue
        """
        if self.count() > 0:
            self._count -= 1
            temp = self._queue[0]
            del self._queue[0]
            return temp
    
    def contains(self, item):
        """Check if an item exists in the queue

        Args:
            item (any): Item to check

        Returns:
            (boolean): True if the item exists else False
        """
        return item in self._queue
    
    def copy(self):
        """Copy the contents of the queue to a list

        Returns:
            (list): List of all the items in the queue
        """
        return [item for item in self._queue]

    def clear(self):
        """Delete all items in the queue
        """
        self._count = 0
        del self._queue[:]
    