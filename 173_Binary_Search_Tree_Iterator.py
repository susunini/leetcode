# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    """ Tree. Binary Search Tree. Stack. 132 ms. """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)
        

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        res = top.val
        cur = top.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res

class BSTIterator(object):
    """ 100 ms. """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushAll(root)
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        if top.right is not None:
            self.pushAll(top.right)
        return top.val
        
    def pushAll(self, root):
        cur = root
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
