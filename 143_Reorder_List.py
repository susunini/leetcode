# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 
    
    Classic problem. It is composed of three steps which are commonly 
    used for different linked list problems. 
    step 1: find middle node and split into two halves
    step 2: reverse the second half
    step 3: merge two lists
    """
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
            
        slow = head; fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h1 = head; h2 = slow.next
        slow.next = None
        
        prev = None; cur = h2
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        h2 = prev
        
        p1 = h1
        p2 = h2
        while p2:
            p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next
