# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. In-order Traversal. Recursive. 115ms. """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def InOrderTraversal(root):
            if not root:
                return
            InOrderTraversal(root.left)
            res.append(root.val)
            InOrderTraversal(root.right)
        
        InOrderTraversal(root)
        return res[k-1]
    
class Solution(object):
    """ Best: In-order Traversal. Recursive. Pruning. 112ms. """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def InOrderTraversal(root):
            if not root:
                return
            if len(res) == k:
                return
            InOrderTraversal(root.left)
            res.append(root.val)
            InOrderTraversal(root.right)
        
        InOrderTraversal(root)
        return res[-1]
    
class Solution(object):
    """ In-order Traversal. Recursive. Pruning. No extra space except stack. 152ms. """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        k = [k]
        def InOrderTraversal(root):
            if not root:
                return
            res = InOrderTraversal(root.left)
            if k[0] == 0:
                return res
            k[0] -= 1
            if k[0] == 0:
                return root.val
            return InOrderTraversal(root.right)
        
        return InOrderTraversal(root)
    
class Solution(object):
    """ In-ordert Traversal. Iteractive. Pruning. 96ms """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        stack = []
        cur = root
        while 1:
            if len(res) == k:
                break
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res[-1]
    
class Solution(object):
    """ In-ordert Traversal. Iteractive. Pruning. No extra Space except stack. 96ms """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cur = root
        while 1:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            k -= 1
            if k == 0:
                return top.val
            cur = top.right
        return res[-1]
    
class Solution(object):
    """ 79ms. """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: 
            return
        stack = [(root,1)]
        while stack:
            top, i = stack.pop()
            if i == 1:
                stack.append((top, 2))
                if top.left:
                    stack.append((top.left, 1))
            elif i == 2:
                k -= 1
                if k == 0:
                    return top.val
                if top.right:
                    stack.append((top.right, 1))
        

        
