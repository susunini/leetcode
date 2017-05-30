# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong. """
    def getMinMax(self, root):
        if not root:
            return (True, None, None)
        left_valid, left_min, left_max = self.getMinMax(root.left)
        if not left_valid:
            return False
        right_valid, right_min, right_max = self.getMinMax(root.right)
        if not right_valid:
            return False
        return (
            (left_max is None or left_max < root.val) and (right_min is None or right_min > root.val), 
            left_min,
            right_max
        )
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _, _ = self.getMinMax(root)
        return res
        
class Solution(object):
    """ Tree. Recursive. 82ms. """
    def getMinMax(self, root):
        if not root:
            return (True, None, None)
        left_valid, left_min, left_max = self.getMinMax(root.left)
        if not left_valid:
            return (False, None, None)
        right_valid, right_min, right_max = self.getMinMax(root.right)
        if not right_valid:
            return (False, None, None)
        return (
            (left_max is None or left_max < root.val) and (right_min is None or right_min > root.val), 
            left_min if left_min else root.val, 
            right_max if right_max else root.val
        )
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _, _ = self.getMinMax(root)
        return res
       
import sys
class Solution:
    """ Tree. Inorder Traversal. Recursive. 88ms. 
    
    lower and upper float('inf') """
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        return self.inorder(root, -float('inf'), float('inf'))
        
    def inorder(self, root, lower, upper):
        if not root:
            return True
            
        if root.val <= lower or root.val >= upper:
            return False
            
        return self.inorder(root.left, lower, min(root.val, upper)) and self.inorder(root.right, max(root.val, lower), upper)
        
 class Solution:
     """ Tree. Inorder Travseral. Recursive.
     
     Instead of maintaining buggy lower and upper, maintain prev. """
     pass
     
class Solution(object):
    """ Tree. Inorder Traversal. Iteractive. Stack. 69ms. 
    
    *Best solution. """
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = None; cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev and cur.val <= prev.val: 
                return False
            prev = cur
            cur = cur.right
        return True
     
  
