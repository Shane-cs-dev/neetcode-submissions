import copy
from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hash map that map original node to new node
        oldToCopy = collections.defaultdict(lambda: Node(0))

        # Add None to the hash map
        oldToCopy[None] = None

        # Loop through the linked list
        curr = head
        while curr:
            # Create node for curr and its next, random
            oldToCopy[curr].val = curr.val
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]

            # Move the node to the next one
            curr = curr.next
        
        return oldToCopy[head]