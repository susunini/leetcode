# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 
    
    Iterative solution.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = head
        while p:
            dummy.next, p.next, p = p, dummy.next, p.next
        res = dummy.next
        dummy.next = None
        return res
        
class Solution(object):
    """ Recursive solution. """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        
        def doReverseList(head):
            if head.next is None: return head, head
            new_head, new_tail = doReverseList(head.next)
            new_tail.next = head
            head.next = None
            return new_head, head
        
        new_head, _ = doReverseList(head)
        return new_head
