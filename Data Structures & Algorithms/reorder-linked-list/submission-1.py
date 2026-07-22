# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: 
        # Corner case
        if not head or not head.next:
            return

        # Create slow and fast pointer to find the middle point and endpoint of the linked list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Spliting the linked list
        head2 = slow.next
        slow.next = None

        # Reversing second linked list head2
        prev, curr = None, head2
        while curr:
            # Storing the next location
            temp = curr.next

            # Reversing
            curr.next = prev
            prev = curr
            curr = temp
            
        
        head2 = prev # Assigning the new head to head2

        # ReorderList
        l1, l2 = head, head2
        while l1 and l2:
            # Storing next location to temp1 and 2
            temp1, temp2 = l1.next, l2.next

            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
        if l2:
            l1.next = l2
        




