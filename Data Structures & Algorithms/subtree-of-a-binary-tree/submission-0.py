# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(p, q):

            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            if p.val != q.val:
                return False
            
            return compare(p.left, q.left) and compare(p.right, q.right)

        q = deque()
        q.append(root)
        
        while q:

            node = q.popleft()
            
            if compare(node, subRoot):
                return True
            
            if node.left is not None:
                q.append(node.left)
            
            if node.right is not None:
                q.append(node.right)
        
        return False



            