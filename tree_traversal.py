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
        """ a.k.a DFS (depth first search) """
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
        """ a.k.a BFS (breadth first search) """
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            yield node.data

    def size(self):
        def count(node):
            if not node: return 0

            return 1 + count(node.left) + count(node.right)

        return count(self.root)

    def max_depth(self):

        paths = []

        def all_paths(node, path=[]):
            if not node: return

            path = path + [node.data]

            if not node.left and not node.right:
                paths.append(path)

            all_paths(node.left, path)
            all_paths(node.right, path)

        all_paths(self.root)

        return len(max(paths, key=len))

    def is_balanced(self):

        def height(node):

            if not node: return (True, 0)

            left_height = height(node.left)
            right_height = height(node.right)

            _is_balanced = abs(right_height[1] - left_height[1]) <= 1
            tree_height = max(left_height[1], right_height[1]) + 1

            return (_is_balanced, tree_height)

        return height(self.root)[0]

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
print "Size ->", tree.size()
print "Max depth ->", tree.max_depth()
print "Is balanced ->", tree.is_balanced()
