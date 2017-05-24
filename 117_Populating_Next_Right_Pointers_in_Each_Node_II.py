# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    """ Linked List. Tree.
    
    We keep two pointers, p for parent level and c for child level.
    We can easily find c.next with help of parent level because nodes in parent level is already
    linked.
    We use a dummy node as head of child level to find the head of next parent level easily. 
    """
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        p = root
        dummy = TreeLinkNode(0)
        while p:
            c = dummy
            while p:
                if p.left: c.next = p.left; c = c.next
                if p.right: c.next = p.right; c = c.next
                p = p.next
            p = dummy.next; dummy.next = None
