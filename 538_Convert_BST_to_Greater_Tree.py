class Solution(object):
    """ Tree. In-order Traversal. """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.tree_sum = 0
        
        def traverseInOrder(root):
            if not root: return
            traverseInOrder(root.right)
            tmp = root.val
            root.val += self.tree_sum
            self.tree_sum += tmp
            traverseInOrder(root.left)
            
        traverseInOrder(root)
        return root
