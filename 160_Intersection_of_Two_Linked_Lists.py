# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List. Two Pointers. 
    
    Without calculating length."""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA; p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        p1_prime = headA
        while p1:
            p1 = p1.next
            p1_prime = p1_prime.next
        p2_prime = headB
        while p2:
            p2 = p2.next
            p2_prime = p2_prime.next
        while p1_prime and p2_prime:
            if p1_prime == p2_prime:
                return p1_prime
            p1_prime = p1_prime.next
            p2_prime = p2_prime.next
        return None
        
class Solution(object):
    """ Improvement of previous solution. 
    
    p1_prime and p2_prime will be same sooner or later. If there is intersaction,
    they will meet at the intersaction node. Otherwise, they will point to None
    at same time. """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA; p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        p1_prime = headA
        while p1:
            p1 = p1.next
            p1_prime = p1_prime.next
        p2_prime = headB
        while p2:
            p2 = p2.next
            p2_prime = p2_prime.next
        while p1_prime != p2_prime:
            p1_prime = p1_prime.next
            p2_prime = p2_prime.next
        return p1_prime
 
class Solution(object):
    """ Further improvement. 
    
    Maintain two pointers p1 and p2 initialized at the head of A and B, respectively. 
    Then let them both traverse through the lists, one node at a time.
    When p1 reaches the end of a list, then redirect it to the head of B (yes, B, 
    that's right.); similarly when pB reaches the end of a list, redirect it the head 
    of A.
    If at any point p1 meets p2, then p1/p2 is the intersection node.To see why the 
    above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and 
    B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), 
    p2 would reach the end of the merged list first, because p2 traverses exactly 2 nodes 
    less than pA does. By redirecting pB to head A, and pA to head B, we now ask pB to travel 
    exactly 2 more nodes than pA would. So in the second iteration, they are guaranteed to 
    reach the intersection node at the same time.
    """ 
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA; p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
        
