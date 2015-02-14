class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self):
        self.front = None
        self.rear  = None
        self.length = 0

    def append(self, data):

        node = Node(data)

        if not self.rear:
            self.rear = node
            self.front = self.rear
        else:
            self.rear.next = node
            self.rear = node

        self.length += 1

    def popleft(self):

        if not self.front:
            self.front, self.rear = None, None

            raise IndexError("pop from an empty queue")

        curr = self.front

        self.front = self.front.next

        return curr.data

    def __str__(self):
        data = []
        curr = self.front

        while curr:
            data.append(curr.data)
            curr = curr.next

        return "Queue ->{0}".format(data)

    def __iter__(self):
        curr = self.front

        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self):
        return self.length

q = Queue()

q.append(10)
q.append(1)
q.append(12)
q.append(8)
q.append(9)
q.append(15)

print(q)

print([data for data in q])
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
