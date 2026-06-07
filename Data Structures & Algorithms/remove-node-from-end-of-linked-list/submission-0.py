# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i = 0
        curr = head
        prev = ListNode()

        length = 0

        while curr != None:
            length += 1
            curr = curr.next

        if length - n == 0:
            return head.next

        curr = head

        while curr != None:

            if i == length - n:
                prev.next = curr.next
                return head
            
            prev = curr
            curr = curr.next
            i += 1
        
        return head
            
            