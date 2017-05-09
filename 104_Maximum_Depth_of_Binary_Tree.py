class Solution(object):
    """ Wrong. """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, level):
            if not root:
                return
            res = max(res, level)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        res = 0
        dfs(root, 1)
        return res
        
class Solution(object):
    """ Tree. Divide and Conquer. """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(root):
            if not root:
                return 0
            return max(getDepth(root.left), getDepth(root.right)) + 1
        return getDepth(root)
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
