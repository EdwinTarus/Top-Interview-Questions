# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Assign left and right pointer to the head of the linked list
        l = head
        r = head
        
        # The left pointer will be moving one step ahead while the right pointer will be moving two steps
        while r and r.next:
          """
          if the linked list is a cycle it will reach a time when both pointers 
          will be at the same node since the right pointer is moving faster in 
          the same cyle compared to the left pointer. (It's almost like the hour and the minute hands of a clock).
          """
            l = l.next
            r = r.next.next
            if r == l:
                return True
          
        return False
        
