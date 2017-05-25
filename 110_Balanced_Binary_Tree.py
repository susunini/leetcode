# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong definition of height balanced tree -> max depth of leaf node - min depth of leaf node <= 1
    For example
    1
      2
         3
    """
    pass

class Solution(object):
    """ Wrong. """
    def getDepth(self, root):
        if not root:
            return 0
        left_dep = self.getDepth(root.left)
        if left_dep == -1:
            return -1
        right_dep = self.getDepth(root.right)
        if right_dep == -1:
            return -1
        return max(left_dep, right_dep) if abs(left_dep - right_dep) <= 1 else -1
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_dep = self.getDepth(root.left)
        right_dep = self.getDepth(root.right)
        return left_dep != -1 and right_dep != -1 and abs(left_dep - right_dep) <= 1
        
class Solution(object):
    """ Tree. Divide and Conquer. 75ms. 
    
    Definition of height balanced tree"""
    def getDepth(self, root):
        if not root:
            return 0
        left_dep = self.getDepth(root.left)
        if left_dep == -1:
            return -1
        right_dep = self.getDepth(root.right)
        if right_dep == -1:
            return -1
        return max(left_dep, right_dep) + 1 if abs(left_dep - right_dep) <= 1 else -1
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_dep = self.getDepth(root.left)
        right_dep = self.getDepth(root.right)
        return left_dep != -1 and right_dep != -1 and abs(left_dep - right_dep) <= 1
        
        
