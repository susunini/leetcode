# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Inorder Traversal. Recursive. """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def doTraversal(node):
            if not node:
                return
            doTraversal(node.left)
            res.append(node.val)
            doTraversal(node.right)
        return res
    
class Solution(object):
    """ Tree. Inorder Traversal. Iteractive. """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root; stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res
    
# TODO: Morri's Traversal
            
            
        
