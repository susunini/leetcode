# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Linked List. 
    
    Recursive solution. Find middle node. 4%. """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        prev_slow = None
        slow = head
        fast = head.next
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if prev_slow:
            prev_slow.next = None
            left = self.sortedListToBST(head)
        else:
            left = None
        right = self.sortedListToBST(slow.next)
        tree_node = TreeNode(slow.val)
        tree_node.left = left; tree_node.right = right
        return tree_node
        
class Solution(object):  
    """ Wrong. """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def do(head, tail):
            if not head:
                return None
            slow = head
            fast = head.next
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            tree_node = TreeNode(slow.val)
            tree_node.left = do(head, slow)
            tree_node.right = do(slow.next, tail)
            return tree_node
            
        do(head, None)

class Solution(object):
    """ Similar to previous solution but do not alter the list. 66%. """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def do(head, tail):
            if head == tail:
                return None
            slow = head
            fast = head.next
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            tree_node = TreeNode(slow.val)
            tree_node.left = do(head, slow)
            tree_node.right = do(slow.next, tail)
            return tree_node
            
        return do(head, None)

class Solution: 
    """ In-order Traversal. 
    
    Do you really understand this solution? """
    pass
        
        
            
        
