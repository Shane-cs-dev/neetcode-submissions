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
    """
    This is DFS method
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create an empty hash map as cache
        cache = {}

        # Define recursive function
        def clone(node) -> 'Node':
            # Corner case
            if not node:
                return
            if node in cache:
                return cache[node]
            
            # if there's no node, then create a new node for this one
            cache[node] = Node(node.val, None, None)
            cache[node].next, cache[node].random = clone(node.next), clone(node.random)

            return cache[node]
        
        # Calling function
        return clone(head)