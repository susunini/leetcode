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
