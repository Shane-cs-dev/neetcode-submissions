# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create an dummy node as a starting point
        new_head = ListNode()
        new_head.next = head
        dummy = new_head

        # Create a pointer next to track n steps of the linked list
        next_n = dummy
        for _ in range(n):
            next_n = next_n.next

        # Traverse the linked list until the next_n pointer becomes None
        prev, curr = None, dummy
        while next_n:
            next_n = next_n.next
            # Update prev and curr
            prev = curr
            curr = curr.next
        
        # Remove curr and connect prev to curr.next
        prev.next = curr.next
        curr.next = None

        return new_head.next
