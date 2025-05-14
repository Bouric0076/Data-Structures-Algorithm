class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    has_cycle = False

    # First, detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None  # No cycle

    # Move one pointer to the head, keep the other at meeting point.
    # They will meet at the start of the cycle.
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Start of the cycle

# Example usage:
# Creating a linked list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creating a cycle
print(detectCycle(node1).val)  # Output: 3 (start of the cycle)


