https://leetcode.com/problems/binary-tree-inorder-traversal/
http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html

# Note:
# Solution 1: Use recursion or iteration with a stack Time O(n) Space O(lgn)
# Solution 2: Use Morris Traversal Time O(n) ? Space O(1)

# Morris Traversal
# Use leaves' right node to store links to their inorder successors. Although the tree is modified through the traversal, it is reverted back to its original shape after the completion. 
# For each node, if its left node is None, print it and move its right node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        r_ints = []
        cur = root
        while cur:
            # 1) if cur.left is None, append it and move cur to its right node
            if cur.left is None:
                r_ints.append(cur.val)
                cur = cur.right
            # 2) if cur.left is not None
            else:
                # 2) then find cur's inorder predecessor
                pred = cur.left
                while pred.right and pred.right != cur: # pred.right != cur -> a node might be visited twice; the first time we create the link and the sec time we revert link
                    pred = pred.right
                if pred.right is None: # link has not been not created yet
                    pred.right = cur
                    cur = cur.left
                else: # link has been created; revert it
                    pred.right = None
                    r_ints.append(cur.val)
                    cur = cur.right # When we see the link, we know that the left subtree of cur has been traversed
        return r_ints
            
        
