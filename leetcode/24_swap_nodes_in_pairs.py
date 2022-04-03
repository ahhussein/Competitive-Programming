# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)
    
    
    def swap(self, head: ListNode):
        if not head:
            return None
        
        if not head.next:
            return head
        
        # Swap nodes
        temp = head
        head = head.next
        temp.next = head.next
        head.next = temp
        
        # Swap further LL
        head.next.next = self.swap(head.next.next)
        
        return head
        
