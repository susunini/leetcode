class Solution(object):
    """ Tree. Recursive. O(logn*logn)
    
    Number of nodes in a full binary tree = 2^k - 1 = 1 << k - 1 where k is tree height
    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur = root.left
        left_height = 0
        while cur:
            left_height += 1
            cur = cur.left
        cur = root.right
        right_height = 0
        while cur:
            right_height += 1
            cur = cur.left
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
