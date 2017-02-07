# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers.
    
    Use two pointers, pre for the node before duplicates, cur to find the last one of duplicates. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy; cur = dummy.next
        while pre and cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next != cur:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
        
 class Solution(object):
    """ Trivial improvements. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy; cur = dummy.next
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next != cur:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
        
class Solution(object):
    """ A variation of previous solution. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy; cur = pre.next
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
        
class Solution(object):
    """ Recursive solution. """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        if cur != head:
            return self.deleteDuplicates(cur.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
