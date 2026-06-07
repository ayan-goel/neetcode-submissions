# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = False
        dummy = ListNode()
        curr = dummy

        while l1 is not None or l2 is not None or carry:
            
            val = 1 if carry else 0
            
            if l1 is not None:
                val += l1.val

            if l2 is not None:
                val += l2.val

            if val < 10:
                carry = False
            else:
                val = val % 10
                carry = True

            curr.next = ListNode(val)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

    
        return dummy.next

                