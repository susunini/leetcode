# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. 155ms(78%). """
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        self.res = root.val
        
        def dfs(root):
            """ return max path ends at root """
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max([self.res, max(left, 0)+max(right, 0)+root.val])
            return max([left, right, 0])+root.val
            
        dfs(root)
        return self.res
            
