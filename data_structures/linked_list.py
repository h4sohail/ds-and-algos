class Node():
    def __init__(self, _data=None, _next=None):
        self.data = _data
        self.next = _next
    

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = []
        current = self.head
        while(current != None):
            if (current.data != None):
                nodes.append(current.data)
            current = current.next
        nodes.append("None")
        return "->".join(nodes)

    def insert(self, data):
        node = Node(data)
        if self.head != None:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node
        else:
            self.head = node
    
    def reverse(self):
        current = self.head
        prev = None
        while(current != None):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
