# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Complexity O(n^n). 1395 ms. """
    
    def pathSumFromRoot(self, root, sum):
        if not root:
            return 0
        return ((1 if root.val == sum else 0)  # path found ending at root 
                + self.pathSumFromRoot(root.left, sum-root.val) 
                + self.pathSumFromRoot(root.right, sum-root.val))
            
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return (self.pathSumFromRoot(root, sum) # number of paths having sum and starting from root
                + self.pathSum(root.left, sum) # number of paths having sum and not starting from root
                + self.pathSum(root.right, sum))
