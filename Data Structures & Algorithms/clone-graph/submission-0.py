"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        q = deque()
        q.append(node)

        hm = {}
        hm[node] = Node(node.val)

        while q:

            n = q.popleft()

            for neighbor in n.neighbors:
                if neighbor not in hm:
                    hm[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                hm[n].neighbors.append(hm[neighbor])
            
        return hm[node]

        
                

