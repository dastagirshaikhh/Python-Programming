class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="->")
                n = n.ref
            print("Null")

    def add_begin(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    def add_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = node

    def add_between(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in Linked List")
        else:
            node = Node(data)
            node.ref = n.ref
            n.ref = node

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_last(15)
LL1.add_between(14,15)
LL1.add_begin(12)
LL1.display()


