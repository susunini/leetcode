# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Recursive. """
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def do(root):
            if not root: return (0, 0)
            (left_sum, left_tilt) = do(root.left)
            (right_sum, right_tilt) = do(root.right)
            return (left_sum + right_sum + root.val, left_tilt + right_tilt + abs(left_sum - right_sum))
        _, res = do(root)
        return res
