from queue import Queue

class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root=None):
        self.root = Node(root)

    def dfs(self, tree):
        return self.dfs_helper(tree.root, [])
    
    def dfs_helper(self, node, traversal):
        if node:
            traversal.append(node.value)
            self.dfs_helper(node.left, traversal)
            self.dfs_helper(node.right, traversal)
        return traversal

    def bfs(self, tree):
        return self.bfs_helper(tree.root)
    
    def bfs_helper(self, node):
        queue = Queue()
        if node:
            queue.enqueue(node)
            traversal = []
            while len(queue) > 0:
                node = queue.peek()
                queue.dequeue()
                traversal.append(node.value)
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        return traversal
        
#               1
#           /       \  
#          2          3  
#        /  \       /   \
#       4    5     6     7 

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.dfs(tree))
print(tree.bfs(tree))