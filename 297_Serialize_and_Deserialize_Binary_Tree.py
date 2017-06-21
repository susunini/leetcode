# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """ Tree. ItePre-order Traversal with 'null'. 356 ms. 
   
    Follow pre-order to serialize and deserialize. 
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(' ')
        def buildTree():
            val = data.pop(0)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = buildTree()
            root.right = buildTree()
            return root
        return buildTree()

class Codec:
    """ 362 ms. """
    def preorder(self, root):
        if not root:
            self.res += '#' if not self.res else ' #'
            return
        self.res += str(root.val) if not self.res else ' ' + str(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ''
        self.preorder(root)
        return self.res
        
    def buildTree(self, data):
        val = data.pop(0)
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self.buildTree(data)
        root.right = self.buildTree(data)
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        return self.buildTree(data)
    
 class Codec:
    """ Iterative preorder DFS. """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        stack = [root]
        while stack:
            node = stack.pop()
            res += ' ' if res else ''
            res += str(node.val) if node else '#'
            if node:
                stack.append(node.right)
                stack.append(node.left)
        return res
        

    def buildNode(self, data):
        if not data:
            return None
        val = data.pop(0)
        return None if val == '#' else TreeNode(int(val))
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        root = self.buildNode(data)
        stack = []; cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                new_node = self.buildNode(data)
                cur.left = new_node
                cur = cur.left
            cur = stack.pop()
            new_node = self.buildNode(data)
            cur.right = new_node
            cur = cur.right
        return root
