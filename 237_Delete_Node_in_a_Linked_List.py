# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        p = node
        while p and p.next:
            p.val = p.next.val
            if p.next.next is None:
                p.next = None
                break
            p = p.next

class Solution(object):
    """ Faster and smarter. """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next
            
                
        
            
        
