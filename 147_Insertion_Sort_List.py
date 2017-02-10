# Note:
# Solution 1:
# Locate prev which is the place to insert
# Remember to reposition prev; but only in certain cases to avoid LTE

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 98%.
    
    Locate prev which is the place to insert. 
    Remember to reposition prev; but only in certain cases to avoid LTE. """
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        
        prev = dummy_node
        cur = head
        
        while cur:
            nex = cur.next # save next node because cur will be repositioned
            # find the place to insert cur
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            # insert cur
            prev.next, cur.next = cur, prev.next
            # move cur to nex
            cur = nex
            # reposition prev
            if cur and prev.val > cur.val:
                prev = dummy_node
        
        r_node = dummy_node.next
        dummy_node.next = None
        return r_node

class Solution(object):
    """ Linked List. 73%. """
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = head
        while p:
            p2 = dummy
            while p2.next and p2.next.val < p.val:
                p2 = p2.next
            p2.next, p.next, p = p, p2.next, p.next
        return dummy.next
        
            
                
            
        
