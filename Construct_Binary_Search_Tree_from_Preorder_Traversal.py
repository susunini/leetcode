class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = self.right = None
        
class Solution(object):
     """ Tree. O(n^2). """
     def construct_bst(self, li):
         if not li:
             return None
         root = TreeNode(li[0])
         i = 1
         while i < len(li):
             if li[i] > root.val:
                 break
             i += 1
         root.left = self.construct_bst(li[:i])
         root.right = self.construct_bst(li[i:])
         return root
         
class Solution(object):
     """ Tree. O(n). """
     def __init__(self):
         self.idx = 0
         
     def construct_bst(self, li):
         return construct_bst(li, None, None)
         
     def construct_bst(self, li, min_val, max_val):
          if self.idx >= len(li):
               return None
          val = li[self.idx]
          if (min_val is None or val >= min_val) and (max_val is None or val <= max_val):
               root = TreeNode(val)
               self.idx += 1
               root.left = self.construct_bst(li, min_val, min(max_val, val))
               root.right = self.construct_bst(li, max(min_val, val), max_val)
               return root
          else:
               return None
               
               
        
     
         
         
                 
             
