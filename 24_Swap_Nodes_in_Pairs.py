# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Wrong. """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while 1:
            p4 = p1
            for _ in range(3):
                if not p4:
                    return dummy.next
                p4 = p4.next
            p2 = p1.next; p3 = p2.next
            p1.next = p3; p3.next = p2; p2.next = p4
            p1 = p3
        return dummy.next
        
class Solution(object):
    """ Linked List. Four pointers. """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while 1:
            p4 = p1
            for _ in range(3):
                if not p4:
                    return dummy.next
                p4 = p4.next
            p2 = p1.next; p3 = p2.next
            p1.next = p3; p3.next = p2; p2.next = p4
            p1 = p2
        return dummy.next
        
class Solution(object):
    """ Simpler without using dummy or four pointers. """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next; b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

class Solution(object):
    """ Recursive solution. """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head_next = head.next
        head.next = self.swapPairs(head.next.next)
        head_next.next = head 
        return head_next
