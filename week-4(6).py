class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        
        # Case 1: List is empty
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Point to itself
            return
        
        # Case 2: Inserting at the beginning or in between
        current = self.head
        while True:
            # Case 2a: Insert before the head
            if current.data <= data <= current.next.data:
                new_node.next = current.next
                current.next = new_node
                break
            
            # Case 2b: We are at the last node
            if current.next == self.head:
                current.next = new_node
                new_node.next = self.head
                break
            
            current = current.next

    def print_list(self):
        if not self.head:
            return "List is empty"
        
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return "->".join(map(str, result))

# Example usage:
cll = CircularLinkedList()
cll.insert_sorted(1)
cll.insert_sorted(2)
cll.insert_sorted(4)
print(cll.print_list())  # Output: 1->2->4

cll.insert_sorted(2)
print(cll.print_list())  # Output: 1->2->2->4

cll = CircularLinkedList()
cll.insert_sorted(1)
cll.insert_sorted(4)
cll.insert_sorted(7)
cll.insert_sorted(9)
print(cll.print_list())  # Output: 1->4->7->9

cll.insert_sorted(5)
print(cll.print_list())  # Output: 1->4->5->7->9
