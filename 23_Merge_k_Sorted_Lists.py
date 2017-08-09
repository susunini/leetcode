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
    """ Divide and Conquer. """
    
    def mergeTwoLists(self, h1, h2):
        dummy = ListNode(None)
        p1 = h1; p2 = h2
        p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1; p1 = p1.next
            else:
                p.next = p2; p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next
                
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) is 0:
            return None
        if len(lists) is 1:
            return lists[0]
        n = len(lists)
        h1 = self.mergeKLists(lists[:n/2])
        h2 = self.mergeKLists(lists[n/2:])
        return self.mergeTwoLists(h1, h2)
    
import heapq

class Solution(object):
    """ Linked List. Heaqp. 
    
    We can also divide and conquer to use merge two lists at a time. 
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        h = [(head.val, head) for head in lists if head]
        heapq.heapify(h)
        while h:
            _, node = heapq.heappop(h)
            cur.next = node; cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))
            
        return dummy.next

        
        
  
