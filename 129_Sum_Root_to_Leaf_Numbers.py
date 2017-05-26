# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong. """
    def dfs(self, root, cur_sum, res):
        if not root:
            return 
        cur_sum += root.val
        if not root.left and not root.right:
            res[0] += cur_sum
            return
        self.dfs(root.left, cur_sum, res)
        self.dfs(root.right, cur_sum, res)
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, 0, res)
        return res[0]
        
class Solution(object):
    """ Tree. DFS. """
    def dfs(self, root, cur_sum, res):
        if not root:
            return 
        cur_sum = cur_sum*10+root.val
        if not root.left and not root.right:
            res[0] += cur_sum
            return
        self.dfs(root.left, cur_sum, res)
        self.dfs(root.right, cur_sum, res)
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, 0, res)
        return res[0]
