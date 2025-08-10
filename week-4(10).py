import heapq

class Node:
    def __init__(self, data=0, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom

def flatten_linked_list(head):
    if not head:
        return None

    # Min-heap to store the nodes
    min_heap = []
    
    # Initialize the heap with the head nodes
    current = head
    while current:
        heapq.heappush(min_heap, current)
        current = current.next

    # Dummy node to help with the result list
    dummy = Node(0)
    current = dummy

    # Flatten the list
    while min_heap:
        # Get the smallest node
        smallest_node = heapq.heappop(min_heap)
        current.bottom = smallest_node  # Link the bottom pointer
        current = current.bottom  # Move to the next node

        # If there is a bottom list, add it to the heap
        if smallest_node.bottom:
            heapq.heappush(min_heap, smallest_node.bottom)

    # Return the flattened list starting from the first node
    return dummy.bottom

def print_flattened_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.bottom
    print("None")

# Example usage:
# Creating the linked list:
# 5 -> 7 -> 8 -> 30
# |    |    |    
# 10   20   35
# |          |
# 19         40
# |          |
# 22         45
# |          |
# 28         50

head = Node(5)
head.next = Node(7)
head.next.next = Node(8)
head.next.next.next = Node(30)

head.bottom = Node(10)
head.bottom.bottom = Node(19)
head.bottom.bottom.bottom = Node(22)
head.bottom.bottom.bottom.bottom = Node(28)

head.next.bottom = Node(20)

head.next.next.bottom = Node(35)
head.next.next.bottom.bottom = Node(40)
head.next.next.bottom.bottom.bottom = Node(45)
head.next.next.bottom.bottom.bottom.bottom = Node(50)

# Flattening the linked list
flattened_head = flatten_linked_list(head)

# Printing the flattened list
print_flattened_list(flattened_head)  # Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50 -> None
