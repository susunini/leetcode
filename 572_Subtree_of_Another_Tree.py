# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong. """
    def dfs(self, root, node, res):
        if not root:
            return
        if root.val == node.val:
            res.append(root)
        self.dfs(root.left, node, res)
        self.dfs(root.right, node, res)
        
    def isSameTree(self, root1, root2):
        if (not root1 or not root2) and (root1 != root2):
            return False
        if root1.val != root2.val:
            return False
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        nodes = []
        self.dfs(s, t, nodes)
        for node in nodes:
            if self.isSameTree(node, t):
                return True
        return False
    
class Solution(object):
    """ Tree. 522ms(26%). """
    def dfs(self, root, node, res):
        if not root:
            return
        if root.val == node.val:
            res.append(root)
        self.dfs(root.left, node, res)
        self.dfs(root.right, node, res)
        
    def isSameTree(self, root1, root2):
        if root1 == root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        nodes = []
        self.dfs(s, t, nodes)
        for node in nodes:
            if self.isSameTree(node, t):
                return True
        return False
    
class Solution(object):
    """ Tree. Recursive. 402ms(60%). """
    def isSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
