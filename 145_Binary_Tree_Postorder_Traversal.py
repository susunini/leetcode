# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Recursive """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def doTraversal(node):
            if not node: return
            doTraversal(node.left)
            doTraversal(node.right)
            r_vals.append(node.val)
        doTraversal(root)
        return res
        
class Solution(object):
    """ Iterative using count of occurrence """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [(root, 1)]
        while stack:
            node, idx = stack.pop()
            if not node:
                continue
            if idx == 3:
                res.append(node.val)
            else:
                stack.append((node, idx + 1))
                if idx == 1:
                    stack.append((node.left, 1))
                elif idx == 2:
                    stack.append((node.right, 1))
        return res
        
 class Solution(object):
    """ 取巧
    pre-order: root-left-right
    modified pre-order: root-right-left
    post-order: left-right-root (reverse of modified pre-order)
    """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]
        
 class Solution(object):
    """ Small change but more efficient than previous solution """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res.insert(0, node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res
