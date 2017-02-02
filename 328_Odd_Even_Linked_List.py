# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 
    
    Two dummy nodes, two pointers. 
    """
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0); dummy2 = ListNode(0)
        p1 = dummy1; p2 = dummy2
        p = head
        cnt = 0
        while p:
            cnt += 1
            if cnt % 2:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p.next, p = None, p.next
        p1.next = dummy2.next
        res = dummy1.next
        dummy1.next = dummy2.next = None
        return res

class Solution(object):
    """ Faster beats 88%. """
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: 
            return None
        h1 = head; h2 = head.next
        p1 = h1; p2 = h2
        while p2 and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = h2
        return h1
        
        
