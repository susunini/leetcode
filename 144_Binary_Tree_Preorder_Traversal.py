# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Recursive. """
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
    """ Tree. Iteractive.
    
    Append both right and left child but right child first. """
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
            
        
