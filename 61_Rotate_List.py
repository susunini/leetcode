# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers.
    
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = 0
        tail = head
        while tail:
            n += 1
            tail = tail.next
        k = k % n
        if k == 0:
            return head
        p1 = p2 = head
        for i in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        new_head = p1.next
        p1.next = None
        p2.next = head
        return new_head

class Solution(object):
    """ One Pointer by circling the list. 
    
    57% 
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        tail.next = head
        k = n - k % n
        for _ in range(k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
