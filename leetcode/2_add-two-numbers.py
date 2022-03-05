# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        root = ListNode(0)
        current = root
        while l1 or l2 or carry:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            
            carry = num // 10
            num = num % 10
            
            node = ListNode(num)
            current.next = node
            current = node            
            
            
        return root.next
                
            

