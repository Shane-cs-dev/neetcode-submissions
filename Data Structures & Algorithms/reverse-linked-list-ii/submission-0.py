# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node
        dummy = ListNode()
        curr = dummy
        curr.next = head

        # Create a number to track where the pointer is pointing at
        prev_node = None
        num = 0
        while curr:
            if num == left - 1:
                prev_node = curr
                break
            curr = curr.next
            num += 1
         
        # Record the previous one before left
        curr = prev_node.next

        # Start reversing the node from left_p
        prev = None
        num = left
        while curr and num <= right:
            # Store the next node into temp
            temp = curr.next
            
            # Update next pointer for current node
            curr.next = prev

            # Udpate pointers 
            prev = curr
            curr = temp

            # Udpate num
            num += 1
        
        # Update next pointer for the edge, curr is the node right after right
        prev_node.next.next = curr
        prev_node.next = prev
        

        return dummy.next
