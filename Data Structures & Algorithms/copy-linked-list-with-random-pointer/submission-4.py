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
        
        hm = {}

        curr = head

        while curr is not None:
            hm[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr is not None:
            copy = hm[curr]

            if curr.next is not None:
                copy.next = hm[curr.next]
            
            if curr.random is not None:
                copy.random = hm[curr.random]

            curr = curr.next

        if head is not None:
            return hm[head]
        else:
            return None



            