# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. DBS. Iteractive. 52ms. """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left == right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True

class Solution(object):
    """ Tree. DFS. Recursive (Divide and Conquer). 42ms. """ 
    def isMirror(self, root1, root2):
        if root1 == root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
