# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create slow and fast pointer
        slow, fast = head, head

        # Loop through the linked list
        while fast and fast.next:
            # Update the pointer
            slow = slow.next
            fast = fast.next.next

            # Check if there's an overlap
            if slow == fast:
                return True
        
        return False

