# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = head; cur = head.next
        while cur:
            if prev.val == cur.val:
                prev.next, cur.next, cur = cur.next, None, cur.next
            else:
                prev = prev.next
                cur = cur.next
        return head

class Solution(object):
    """ No need for two pointers. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
        
