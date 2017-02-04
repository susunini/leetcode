# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers (prev and cur). """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        self.next = head
        prev, cur = self, head
        while cur:
            if cur.val == val:
                prev.next, cur.next, cur = cur.next, None, cur.next
            else:
                prev = cur
                cur = cur.next
        return self.next
        
  class Solution(object):
    """ Use one pointer instead of two. """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        self.next = head
        cur = self
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.next
        
        
