# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Google. DFS Postorder Traversal. 15%. """
    def __init__(self):
        self.res = 0
        
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = max([1, left+1 if root.left and root.left.val-root.val == 1 else 0,
                   right+1 if root.right and root.right.val-root.val == 1 else 0])
        self.res = max(self.res, res)
        return res
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.res
        
        
