# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    """ Linked List. Hash. 
    
    Use a dictionary to map each node to a newly created node."""
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = dict()
        p1 = head
        dummy = RandomListNode(0)
        p2 = dummy
        while p1:
            p2.next = RandomListNode(p1.label)
            d[p1] = p2.next
            p1 = p1.next; p2 = p2.next
            
        p1 = head
        while p1:
            if p1.random:
                d[p1].random = d[p1.random]
            p1 = p1.next
        return dummy.next

class Solution(object):
    """ No extra space needed using a trick. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        p = head
        while p:
            new_node = RandomListNode(p.label)
            p.next, new_node.next, p = new_node, p.next, p.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        res = head.next
        p1 = head; p2 = head.next
        while p2:
            p1.next = p1.next.next
            if p2.next:
                p2.next = p2.next.next
            p1 = p1.next; p2 = p2.next
        return res

class Solution(object):
    """ Wrong. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            p.next = RandomListNode(p.label)
            p = p.next.next
        p = head
        while p:
            p.next.random = p.random.next
            p = p.next.next
        dummy = RandomListNode(0)
        p2 = dummy
        p = head
        while p:
            p.next, p2.next = p.next.next, p.next
            p = p.next; p2 = p2.next
        return dummy.next
    
class Solution(object):
    """ Wrong. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            new_node = RandomListNode(p.label)
            p.next, new_node.next = new_node, p.next
            p = p.next.next
        p = head
        while p:
            p.next.random = p.random.next
            p = p.next.next
        dummy = RandomListNode(0)
        p2 = dummy
        p = head
        while p:
            p.next, p2.next = p.next.next, p.next
            p = p.next; p2 = p2.next
        return dummy.next
    
class Solution(object):
    """ Previous solution with a dummy node. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            new_node = RandomListNode(p.label)
            p.next, new_node.next = new_node, p.next
            p = p.next.next
        p = head
        while p:
            if p.random: 
                p.next.random = p.random.next
            p = p.next.next
        dummy = RandomListNode(0)
        p2 = dummy
        p = head
        while p:
            p.next, p2.next = p.next.next, p.next
            p = p.next; p2 = p2.next
        return dummy.next

class Solution(object):
    """ Wrong. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        d = collections.defaultdict(lambda: RandomListNode(0))
        p = head
        while p:
            d[p].val = p.label
            d[p].next = d[p.next]
            d[p].random = d[p.random]
            p = p.next
        return d[head]
        
class Solution(object):
    """ Wrong. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        d = collections.defaultdict(lambda: RandomListNode(0))
        d[None] = None
        p = head
        while p:
            d[p].val = p.label
            d[p].next = d[p.next]
            d[p].random = d[p.random]
            p = p.next
        return d[head]
        
 class Solution(object):
    """ Still use dictionary but one loop. """
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        d = collections.defaultdict(lambda: RandomListNode(0))
        d[None] = None
        p = head
        while p:
            d[p].label = p.label
            d[p].next = d[p.next]
            d[p].random = d[p.random]
            p = p.next
        return d[head]
