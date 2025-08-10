class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def get_intersection_node(head1, head2):
    if not head1 or not head2:
        return None

    # Initialize two pointers for both lists
    pointer1 = head1
    pointer2 = head2

    # Traverse both lists
    while pointer1 != pointer2:
        # Move to the next node or switch to the other list
        pointer1 = pointer1.next if pointer1 else head2
        pointer2 = pointer2.next if pointer2 else head1

    # Either both pointers are at the intersection node or both are None
    return pointer1

# Example usage:
# Creating the first linked list: 4 -> 1 -> 8 -> 4 -> 5
head1 = ListNode(4)
head1.next = ListNode(1)
intersection = ListNode(8)
head1.next.next = intersection
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Creating the second linked list: 5 -> 6 -> 1 -> 8 -> 4 -> 5
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = intersection  # Intersecting at node with value 8

# Finding the intersection
intersecting_node = get_intersection_node(head1, head2)
if intersecting_node:
    print(intersecting_node.data)  # Output: 8
else:
    print("No intersection")
