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
        l1_sum, l2_sum = 0, 0
        while l1:
            l1_sum += l1.val * time
            time *= 10
            # Update both linked list
            l1 = l1.next
        print(l1_sum)

        time = 1
        while l2: 
            l2_sum += l2.val * time
            time *= 10
            l2 = l2.next
        print(l2_sum)

        print(l1_sum + l2_sum)

        total = l1_sum + l2_sum
        while total > 0:
            digit = total % 10
            # Create node and add it into the list
            dummy.next = ListNode(digit)
            dummy = dummy.next
            total //= 10

        return new_head.next