from collections import deque

class Tree(object):

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data, node=None):

        def _rec_insert(node, data):
            # recursively insert
            if not node:
                return self.Node(data)

            if data > node.data:
                node.right = _rec_insert(node.right, data)
            else:
                node.left = _rec_insert(node.left, data)

            return node

        if not self.root:
            # First node
            self.root = self.Node(data)
        else:
            # Remaining inserts
            self.root = _rec_insert(self.root, data)

        return self.root

    def level_order(self):
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            yield node.data

tree = Tree()
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(3)
tree.insert(6)
tree.insert(2)
tree.insert(9)

print[node for node in tree.level_order()]
