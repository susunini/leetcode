# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Divide and Conquer. """
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def doDBT(root):
            """ return a list of two elements: 
                first element - num of nodes of longest path ending at root; 
                second element - num of nodes of longest path not ending at root (passing or not passing)
            """
            if not root:
                return [0,0]
            left = doDBT(root.left)
            right = doDBT(root.right)
            return [max(left[0], right[0])+1, max(left[1], right[1], left[0]+right[0]+1)]
        
        res = doDBT(root)
        return max(res)-1
        
 class Solution(object):
    """ Tree. DFS. Traversal each node and get depth of that node. 
    Length of longest path passing a node = depth of its left node + depth of its right node
    """
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        
        def depth(root):
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            res[0] = max(res[0], left_depth+right_depth)
            return max(left_depth, right_depth)+1
            
        depth(root)
        return res[0]
