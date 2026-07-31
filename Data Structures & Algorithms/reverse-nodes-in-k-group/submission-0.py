# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Calculate the group
        # Record current head 
        curr = head
        group = 0
        while curr and group < k:
            # Update pointer for curr
            curr = curr.next 
            group += 1
        
        # Curr will stop at k+1 node
        # Check if there's k nodes to reverse
        if group == k:
            # Calculate the next one
            curr = self.reverseKGroup(curr, k) # This should be k+1 node if the next recursion is not equal to k
            while group > 0:
                # Store the next node
                temp = head.next
                # Connect the head to the curr
                head.next = curr
                # Swapping 
                curr = head
                head = temp
                group -= 1
            head = curr
        return head

