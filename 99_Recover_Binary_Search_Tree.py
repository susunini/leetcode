# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ In-order traversal.
    https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal/2
    Test cases: 1 2 3 5 4; 5 2 3 4 1
    """
    def __init__(self):
        self.first = self.sec = None
        self.prev = None
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.sec.val = self.sec.val, self.first.val
        
    def traverse(self, cur):
        if not cur: return
        self.traverse(cur.left)
        if self.prev and not self.first and self.prev.val > cur.val:
            self.first = self.prev; self.sec = cur
        elif self.prev and self.first and self.prev.val > cur.val: 
            self.sec = cur
            return
        self.prev = cur
        self.traverse(cur.right)
        
