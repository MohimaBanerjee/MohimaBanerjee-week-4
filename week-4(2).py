class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, position):
        if self.head is None or position <= 0:
            return self.head

        current = self.head

        # Deleting the head node
        if position == 1:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return self.head

        # Traverse to the node to be deleted
        for _ in range(position - 1):
            current = current.next
            if current is None:
                return self.head

        # Node to be deleted is current
        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

        current = None
        return self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <--> " if current.next else "")
            current = current.next
        print()


# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(3)
dll.append(4)

print("Original List:")
dll.print_list()

dll.delete_node(3)
print("After deleting node at position 3:")
dll.print_list()

dll2 = DoublyLinkedList()
dll2.append(1)
dll2.append(5)
dll2.append(2)
dll2.append(9)

print("Original List:")
dll2.print_list()

dll2.delete_node(1)
print("After deleting node at position 1:")
dll2.print_list()
