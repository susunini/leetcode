# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. beats 98% """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None: 
            return None
            
        cur_root = root
        while 1:
            if p.val < cur_root.val and q.val < cur_root.val:
                cur_root = cur_root.left
            elif p.val > cur_root.val and q.val > cur_root.val:
                cur_root = cur_root.right
            else:
                return cur_root
            
class Solution(object):            
    def lowestCommonAncestor(self, root, p, q):
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = (root.left, root.right)[a > root.val]
        return root
            
