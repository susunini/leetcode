# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Two Pointers; Linked List.
    We need to find the node before the node to remove.The distance between that node and tail is n.
    We use two pointers to find it. First we move one pointer n places forward，to maintain distance
    of n between the two pinters. Then we move the two pointers at the same speed until the fast 
    pointer hit tail.
    Since the question gives that n is valid, not too many checks have to be put in place.
    
    Alternative: do not use dummy node
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: 
            return None
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p2 = p2.next
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        tmp = p1.next; p1.next = p1.next.next; tmp.next = None
        res = dummy.next; dummy.next = None
        return res
        
        
        
        
        
            
            
        
