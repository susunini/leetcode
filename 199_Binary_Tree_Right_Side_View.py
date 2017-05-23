# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. BFS. 
    
    This problem is asking for a list of right most nodes at each level. 
    """
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == n-1: res.append(node.val)
        return res
    
class Solution(object):
    """ DFS also works but not as natural as BFS.
    def dfs(self, root, level, res):
        if not root:
            return
        try:
            res[level] = root.val
        except IndexError:
            res.append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
            
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, 0, res)
        return res
