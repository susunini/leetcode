# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. BFS. """
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        q = [root]
        while q:
            size = len(q)
            level_max = None
            for i in range(size):
                node = q.pop(0)
                level_max = max(level_max, node.val) if level_max is not None else node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_max)
        return res
        
class Solution(object):
    """ Tree. DFS + level. """
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root, level):
            if not root: return
            try:
                res[level] = max(res[level], root.val)
            except IndexError:
                res.append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
        dfs(root, 0)
        return res
                
            
