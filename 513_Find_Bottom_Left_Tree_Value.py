# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. BFS. Beats 24%.
    """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        prev_level = []
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            prev_level, level = level, next_level
        return prev_level[0].val
        
class Solution(object):
    """ Wrong. """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        q = [root]
        res = None
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i is 0: res = q[i]
        return res.val
 
class Solution(object):
    """ Tree. BFS. standard using queue. record only first node of each level. """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        q = [root]
        res = None
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i is 0: res = node
        return res.val
        
class Solution(object):
    """ Tree. BFS. use a queue but from right to left. Beats 27%.
    """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        q = [root]
        res = None
        while q:
            res = q.pop(0)
            if res.right: q.append(res.right)
            if res.left: q.append(res.left)
        return res.val
        
class Solution(object):
    """ Tree. BFS. tricks. Beats 69%. """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        for node in q:
            q += filter(None, (node.right, node.left))
        return node.val
