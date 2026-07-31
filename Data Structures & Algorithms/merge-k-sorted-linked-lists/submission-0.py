# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # Define the size of the list
        n = len(lists)

        # Create a dummy node
        dummy = ListNode()
        # Initialization
        dummy.next = lists[0]

        i = 1
        while i < n:
            # Create a pointer for sweep line
            # Create a pointer for current node
            curr = dummy.next

            # Create another pointer for the next list
            new_curr = lists[i]

            self.mergeTwoListNode(curr, new_curr)
            i += 1
        
        return dummy.next
                
    def mergeTwoListNode(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        # Create a dummy node
        dummy = ListNode()
        curr = dummy

        # Merging two linked lists
        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                curr.next = list1
                list1 = temp
            else:
                temp = list2.next
                curr.next = list2
                list2 = temp
            
            # Update curr pointer
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        

