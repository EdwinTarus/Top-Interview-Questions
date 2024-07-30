# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        """
        The trick is to make the value of that node to be the value of the next node 
        and the pointer to point to the next next node.
        """
        node.val = node.next.val
        node.next = node.next.next
        
