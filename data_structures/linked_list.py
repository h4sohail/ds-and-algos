class Node:
    def __init__(self, data=None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
  
    def __str__(self):
        node = self.head
        nodes = []
        while(node != None):
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

    def insert(self, data):
        node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node

    def reverse(self): 
        prev = None
        current = self.head 
        while(current != None): 
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node
        self.head = prev

if __name__ == '__main__':
    node_data = ['a', 'b', 'c']
    linked_list = LinkedList()

    for data in node_data:
        linked_list.insert(data)
    
    print(linked_list)
    linked_list.reverse()
    print(linked_list)