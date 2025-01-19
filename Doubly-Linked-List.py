class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev_node is not None:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node

                if current.next_node is not None:
                    current.next_node.prev_node = current.prev_node
                else:
                    self.tail = current.prev_node

                return
            current = current.next_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next_node
        print("None")


if __name__ == "__main__":
    Doubly_LL = DoublyLinkedList()

    print("Is the doubly linked list empty?", Doubly_LL.is_empty())

    Doubly_LL.append(1)
    Doubly_LL.append(2)
    Doubly_LL.append(3)

    print("Doubly Linked List:")
    Doubly_LL.display()

    Doubly_LL.prepend(0)
    print("Doubly Linked List after prepending 0:")
    Doubly_LL.display()

    Doubly_LL.delete(2)
    print("Doubly Linked List after deleting 2:")
    Doubly_LL.display()
