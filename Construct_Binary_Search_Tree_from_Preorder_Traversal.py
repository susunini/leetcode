class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = self.right = None
        
class Solution2(object):
    """ Tree. Divide and Conquer. O(n^2). """
    def construct_bst(self, li):
        print(li)
        if not li:
            return None
        root = TreeNode(li[0])
        i = 1
        while i < len(li):
            if li[i] > root.value:
                break
            i += 1
        root.left = self.construct_bst(li[1:i])
        root.right = self.construct_bst(li[i:])
        return root
         
class Solution(object):
    """ Tree. Recursion. O(n). """
    def __init__(self):
        self.idx = 0
         
    def construct_bst(self, li):
        min_val = min(li); max_val = max(li)
        return self.construct_node(li, min_val, max_val)
        
    def construct_node(self, li, min_val, max_val):
        if self.idx >= len(li):
            return None
        val = li[self.idx]
        if (min_val is None or val >= min_val) and (max_val is None or val <= max_val):
            root = TreeNode(val)
            self.idx += 1
            root.left = self.construct_node(li, min_val, min(max_val, val))
            root.right = self.construct_node(li, max(min_val, val), max_val)
            return root
        return None
               
    def print_in_order(self, root):
        if root is None:
            return
        self.print_in_order(root.left)
        print(root.value)
        self.print_in_order(root.right)
    
pre = [10, 5, 1, 7, 40, 50]
root = Solution().construct_bst(pre)
Solution().print_in_order(root)

         
                 
             
