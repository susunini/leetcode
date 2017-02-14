# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    
class Solution(object):
    """ Wrong. 
    Typos. One-line swapping does not always work. """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        heap = [(head.val, head) for head in lists if head]
        heapq.heapify(heap)
        while heap:
            val, node = heapq.heappop(heap)
            if node.next:
               heapq.heappush(heap, (node.next.val, node.next))
            p.next = node; node.next = None; p = p.next
        return dummy.next
        
        
  
