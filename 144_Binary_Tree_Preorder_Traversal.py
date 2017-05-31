# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Recursive. 49ms. """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def do(root):
            if not root:
                return
            res.append(root.val)
            do(root.left)
            do(root.right)
        do(root)
        return res
    
class Solution(object):
    """ Tree. Iteractive. Stack. 52ms. 
    
    Stack both right and left child. """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root; stack = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right
        return res
    
class Solution(object):
    """ Tree. Iteractive. Stack. 49ms. 
    
    Stack both right and left child but right child first. """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return res
    
class Solution(object):
    """ Tree. Iteractive. Stack. 42ms. 
    
    Stack only right child. """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            while cur: 
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
        return res
            
        
