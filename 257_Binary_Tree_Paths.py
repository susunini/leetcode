# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong. """
    def dfs(self, root, path, res):
        if not root:
            return
        path.append(root)
        if not root.left and not root.right:
            res.append('->'.join(path))
        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)
        path.pop()
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        return res
        
class Solution(object):
    """ Tree. DFS. Recursive. 52ms. """
    def dfs(self, root, path, res):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path))
        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)
        path.pop()
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        return res
