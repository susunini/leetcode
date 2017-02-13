# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Linked List.
    
    Proof:
    We have two pointers, slow move one step at a time and fast moves two steps.
    Sooner or later, slow will meet fast. But where will they meet?
    Assume the length of the non-cycle part is n1. When p1 is at the start of the cycle, it has
    moved n1 steps while fast has moved n1 * 2 steps and n1 steps inside the cycle. 
    We assume that the length of cycle is n2. Now, the distance from p2 to p1 is (n2 - n1). For
    each iteration the distance from p2 to p1 will be shortened by 1. Thus, when they meet, (n2 - n1)
    iterations has passed and p1 will have moved (n2 - n1) steps.
    We record their meeting place, the distance from meeting place to the start of cycle will be
    same as the distance from head to the start of the cycle.
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while 1:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

        
