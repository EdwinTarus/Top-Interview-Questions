# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = None
        #[1,2,3,4,5]
        while head: 
            cur = head
            head = head.next
            cur.next = prev 
            prev = cur
        return cur 
