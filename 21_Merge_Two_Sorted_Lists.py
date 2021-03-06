# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers. """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p1 = l1; p2 = l2; p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1; p1 = p1.next
            else:
                p.next = p2; p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        res = dummy.next; dummy.next = None
        return res
    
    
class Solution(object):
    """ Same as previous. Use one-line ternary. """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p1 = l1; p2 = l2; p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1; p1 = p1.next
            else:
                p.next = p2; p2 = p2.next
            p = p.next
        p.next = p1 if p1 else p2 # or p.next = p1 or p2
        res = dummy.next; dummy.next = None
        return res

    
class Solution(object):
    """ Recursive solution. """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            return l2
