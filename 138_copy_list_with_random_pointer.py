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
        oldToCopy = {None: None}

        # iterate the linked list and create each node copy
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        # link each Node in the copy
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next] # find the copy of next Node
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]

        # time - O(n) iterate n node
        # space - O(n) store n node