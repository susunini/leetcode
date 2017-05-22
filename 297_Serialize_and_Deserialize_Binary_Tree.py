# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
   """ Tree. Pre-order Traversal with 'null'. 356 ms. """

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
