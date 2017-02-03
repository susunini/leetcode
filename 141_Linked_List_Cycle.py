# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. 
    
    If there is a cycle, after slow and fast both enters the cycle, the distance
    between them will decrease by 1 at each step. Sooner or later, they will
    meet each other.
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
