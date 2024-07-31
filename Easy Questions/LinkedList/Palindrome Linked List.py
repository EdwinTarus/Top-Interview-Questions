# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Convert the linked list into an array.
        listA = ""
        while head:
            listA += str(head.val)
            head = head.next
            
        # Check whether the string is a palindrome
        l,r = 0, len(listA)-1
        while l < r:
            if listA[l] != listA[r]:
                return False
            l +=1
            r-=1
        return True
