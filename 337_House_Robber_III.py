# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Recursive. """
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def doRob(root):
            """ return a list of two elements: first elem - max value if rob root; second elem -max value if not rob root. """
            if not root:
                return [0,0]
            left = doRob(root.left)
            right = doRob(root.right)
            return [root.val + left[1] + right[1], max(left) + max(right)]
        
        return maxRob(do(root))
