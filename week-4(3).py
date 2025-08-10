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

    def reverse(self):
        current = self.head
        temp = None

        # Swap next and prev for all nodes
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev  # Move to the next node (which is now previous)

        # Adjust head to the new first node
        if temp:
            self.head = temp.prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <--> " if current.next else "")
            current = current.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(3)
dll.append(4)
dll.append(5)

print("Original List:")
dll.print_list()

dll.reverse()
print("Reversed List:")
dll.print_list()

dll2 = DoublyLinkedList()
dll2.append(75)
dll2.append(122)
dll2.append(59)
dll2.append(196)

print("Original List:")
dll2.print_list()

dll2.reverse()
print("Reversed List:")
dll2.print_list()
 