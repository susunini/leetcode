# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Merge Sort. Top-Down. """
    
    def mergeList(self, h1, h2):
        dummy = ListNode(0)
        p1 = h1; p2 = h2; p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next, p1.next, p1 = p1, None, p1.next
            else:
                p.next, p2.next, p2 = p2, None, p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next
            
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow = head; fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        return self.mergeList(left, right)
        
