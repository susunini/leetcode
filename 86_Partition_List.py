# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """  Linked List. 
    beats 63% 56ms. """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(0); h2 = ListNode(0)
        c1 = h1; c2 = h2
        c = head
        while c:
            if c.val < x:
                c1.next = c
                c1 = c1.next
            else:
                c2.next = c
                c2 = c2.next
            c.next, c = None, c.next
        c1.next = h2.next
        r_node = h1.next
        h1.next = None; h2.next = None
        return r_node
        
class Solution(object):
    """ Wrong. """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = ListNode(0); d2 = ListNode(0)
        p1 = d1; p2 = d2
        p = head
        while p:
            if p.val < x:
                p1.next, p.next, p, p1 = p, None, p.next, p1.next
            else:
                p2.next, p.next, p, p2 = p, None, p.next, p2.next
        p1.next = d2.next
        return d1.next
        
class Solution(object):
    """ Similar to the first solution. I think that one is better. """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = ListNode(0); d2 = ListNode(0)
        p1 = d1; p2 = d2
        p = head
        while p:
            if p.val < x:
                p1.next, p.next, p, p1 = p, None, p.next, p1.next
            else:
                p2.next, p.next, p, p2 = p, None, p.next, p2.next
        p1.next = d2.next
        return d1.next
                
        
