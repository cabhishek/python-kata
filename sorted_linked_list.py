class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.list = None

    def insert(self, data):

        node = Node(data)

        # First node
        if not self.list:
            self.list = node
        else:
            curr = self.list
            prev = None

            # Move ahead
            while curr:
                if data < curr.data:
                    prev = curr
                    curr = curr.next
                else:
                    break

            # if not curr:
            #     curr = node
            #     prev.next = curr
            # If two elements or swap second with first
            if not prev:
                node.next = self.list
                self.list = node
            else:
                # General case
                node.next = curr
                prev.next = node
                prev = node

    def __repr__(self):
        curr = self.list
        queue = []

        while curr:
            queue.append(curr.data)
            curr = curr.next

        return str(queue)

    def __len__(self):
        return self.count

list = LinkedList()

list.insert(10)
list.insert(4)
list.insert(6)
list.insert(2)
list.insert(7)
list.insert(1)

print(list)
