# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Wrong. """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sum_to_cnt = collections.defaultdict(0)
        def traversePostOrder(root):
            if not root: return
            traversePostOrder(root.left)
            traversePostOrder(root.right)
            if root.left:
                root.val += root.left.val
            if root.right:
                root.val += root.right.val
            self.sum_to_cnt[root.val] += 1
        sorted_x = sorted(self.sum_to_cnt.items(), key=operator.itemgetter(1), reverse=True)
        res = []
        for i, (sum, cnt) in enumerate(sorted_x):
            if i == 0 or cnt == sorted_x[i-1][1]:
                res.append(sum)
            else:
                break
        return res
        
class Solution(object):
    """ Tree. Post-order Traversal. """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sum_to_cnt = collections.defaultdict(int)
        def traversePostOrder(root):
            if not root: return
            traversePostOrder(root.left)
            traversePostOrder(root.right)
            if root.left:
                root.val += root.left.val
            if root.right:
                root.val += root.right.val
            self.sum_to_cnt[root.val] += 1
        traversePostOrder(root)
        sorted_x = sorted(self.sum_to_cnt.items(), key=operator.itemgetter(1), reverse=True)
        res = []
        for i, (sum, cnt) in enumerate(sorted_x):
            if i == 0 or cnt == sorted_x[i-1][1]:
                res.append(sum)
            else:
                break
        return res
        
class Solution(object):
    """ Wrong. """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def getSubTreeSum(node):
            if not node: return 0
            sub_tree_sum = node.val + getSubTreeSum(node.left) + getSubTreeSum(node.right)
            c[sub_tree_sum] += 1
            return sub_tree_sum
        c = collections.Counter()
        getSubTreeSum(root)
        max_val = max(c.values())
        return [key for (key, val) in c.iteritems() if val == max_val] 
        
class Solution(object):
    """ No need to change the tree. """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def getSubTreeSum(node):
            if not node: return 0
            sub_tree_sum = node.val + getSubTreeSum(node.left) + getSubTreeSum(node.right)
            c[sub_tree_sum] += 1
            return sub_tree_sum
        c = collections.Counter()
        getSubTreeSum(root)
        max_val = max(c.values())
        return [key for (key, val) in c.iteritems() if val == max_val]      
            
        
        
