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

    def pre_order(self):
        queue = []

        def _rec_pre_order(node):
            if not node: return
            queue.append(node.data)
            _rec_pre_order(node.left)
            _rec_pre_order(node.right)

            return queue

        return _rec_pre_order(self.root)

    def in_order(self):
        queue = []

        def _rec_in_order(node):
            if not node: return
            _rec_in_order(node.left)
            queue.append(node.data)
            _rec_in_order(node.right)

            return queue

        return _rec_in_order(self.root)

    def post_order(self):
        queue = []

        def _rec_post_order(node):
            if not node: return

            _rec_post_order(node.left)
            _rec_post_order(node.right)

            queue.append(node.data)

            return queue

        return _rec_post_order(self.root)

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

print "Level order ->", [node for node in tree.level_order()]
print "Pre order ->", tree.pre_order()
print "Inorder (sorted) ->", tree.in_order()
print "Post order->", tree.post_order()
