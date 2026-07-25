# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new head for new linked list
        new_head = ListNode()
        dummy = new_head

        # Find the sum of the from two numbers
        time = 1
        sums = 0
        while l1 and l2:
            sums += (l1.val + l2.val) * time
            time *= 10
            # Update both linked list
            l1 = l1.next
            l2 = l2.next
        
        while sums > 0:
            digit = sums % 10
            dummy.next = ListNode(digit)
            dummy = dummy.next
            sums = sums // 10


        return new_head.next