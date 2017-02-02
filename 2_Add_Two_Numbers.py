# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 
    All the integers are single digit. Thus we calculate the carry in the second iteration.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p1 = l1; p2 = l2
        p = dummy
        while p1 and p2:
            p.next = ListNode(p1.val + p2.val)
            p = p.next; p1 = p1.next; p2 = p2.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        p = dummy.next
        while p:
            div, mod = divmod(p.val, 10)
            p.val = mod
            if p.next:
                p.next.val += div
            elif div:
                p.next = ListNode(div)
            p = p.next
        res = dummy.next
        dummy.next = None
        return res


class Solution(object):
    """ Slightly slow. 
    
    One iteration.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p1 = l1; p2 = l2; p = dummy
        carry = 0
        while p1 or p2 or carry:
            val1 = 0; val2 = 0
            if p1: val1 = p1.val; p1 = p1.next
            if p2: val2 = p2.val; p2 = p2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            p.next = ListNode(val)
            p = p.next
        res = dummy.next
        dummy.next = None
        return res
