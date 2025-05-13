class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # temporarily store the next node
        curr.next = prev        # reverse the current node's pointer
        prev = curr             # move pointers one step forward
        curr = next_node
    return prev  # New head of the reversed list

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# Reversing the linked list
reversed_head = reverseList(node1)
# Printing the reversed linked list
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None