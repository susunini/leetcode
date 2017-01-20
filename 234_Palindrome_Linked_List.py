# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Two Pointers; Linked List
    Phase 1: Use two pointers to find the node in the middle (actually, the node before the middle)
    and break the linked list into two halves
    Phase 2: Reverse 1st or 2nd half (we will reverse 1st half while looking for middle)
    Phase 3: Compare 1st with 2nd half
    Optional: Restore the list
    Summary 1: handle linked list with even and odd number of nodes; try some test cases will help
    make things clear 
    Summary 2: use python's way of swapping instead of using several temporary variables.
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow_prev, slow = slow_prev, slow, slow.next
        p1 = slow_prev
        if fast:
            slow = slow.next
        p2 = slow
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next; p2 = p2.next
        return True

class Solution(object):
    """ Optional: restore the list while comparing first half with second. """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow_prev, slow = slow_prev, slow, slow.next
        p1 = slow_prev
        p1_prev = slow
        if fast:
            slow = slow.next
        p2 = slow
        res = True
        while p1 and p2:
            if p1.val != p2.val:
                res = False
            p2 = p2.next
            p1.next, p1_prev, p1 = p1_prev, p1, p1.next
        # debug: verify if the list is correctly restored
        p = head
        while p:
            print p.val
            p = p.next
        return res
        
