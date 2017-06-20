# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. beats 41%.
    
    For any node, its right node will be its left node if its left node is not none and its right node's parent node will
    be the right most node in its left branch if its left node is not none.
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                tmp = cur.right
                left_most_right = cur.left
                while left_most_right.right: left_most_right = left_most_right.right
                left_most_right.right = tmp
                cur.right = cur.left; cur.left = None
            cur = cur.right
            
 class Solution(object):
    """ Tree. 49ms(74%). 20170620. """
    def dfs(self, root):
        """ return the right most node after flattening. """
        if not root:
            return None
        if not root.left and not root.right: #
            return root
        rt_rt_most= self.dfs(root.right)
        lft_rt_most = self.dfs(root.left)
        if lft_rt_most: 
            lft_rt_most.right = root.right
            root.right = root.left
            root.left = None #
        return rt_rt_most if rt_rt_most else lft_rt_most #
        
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
            
            
        
