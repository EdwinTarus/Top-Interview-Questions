# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [l1,2,r3,4,5,null] 
        # n = 2
        # [0,1,null]
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        r = dummy
        
        # move the right pointer by n
        while (n+1) != 0:
            r = r.next
            n -=1
            
        # move the left and right pointers 
        while r:
            r = r.next
            l = l.next
            
        # remove the nth node
        l.next = l.next.next
        
        return dummy.next
       
            
            
        
        
