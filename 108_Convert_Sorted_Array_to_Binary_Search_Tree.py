# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Tree. Recursive Solution. 
    
    Nested function is slow. """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def do(nums, s, e):
            if s > e:
                return None
            m = (s + e) / 2
            left = do(nums, s, m - 1)
            right = do(nums, m + 1, e)
            new_node = TreeNode(nums[m])
            new_node.left = left; new_node.right = right
            return new_node
        return do(nums, 0, len(nums) - 1)
        
