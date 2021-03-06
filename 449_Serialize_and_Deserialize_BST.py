# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """ Tree. Pre-order traversal. 156 ms. 
    
    The preorder sequence of a BST: root | left branch (< root) | right branch (> root)
    We can use this rule to deserialize.
    
    We iterate the sequence and use a stack to maintain unfinished nodes on the path from root to previous traversed node.
    If current node is smaller than the top node(previous traversed node) in the stack, it must be the left node of the top node.
    Otherwise, it must be the right node of some node in the stack. We keep poping from the stack until the
    current node is smaller than the top node or stack is empty. The current node is the right node of the last poped node.
    Up until now, We have found left and right nodes for all the poped nodes.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
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
        root = TreeNode(int(data[0]))
        stack = [root]
        for ch in data[1:]:
            new_node = TreeNode(int(ch))
            if new_node.val < stack[-1].val:
                stack[-1].left = new_node
            else:
                while stack and new_node.val > stack[-1].val:
                    node = stack.pop()
                node.right = new_node
            stack.append(new_node)
        return root

class Codec:
   """ 136 ms. """

    def preorder(self, root):
        if not root:
            return
        self.res = ' '.join([self.res, str(root.val)])
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

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split()
        root = TreeNode(int(data[0]))
        stack = [root]
        for ch in data[1:]:
            new_node = TreeNode(int(ch))
            if new_node.val < stack[-1].val:
                stack[-1].left = new_node
            else:
                while stack and new_node.val > stack[-1].val:
                    node = stack.pop()
                node.right = new_node
            stack.append(new_node)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
