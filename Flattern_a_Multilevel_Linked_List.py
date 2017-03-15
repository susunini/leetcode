class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None
        
class Solution(object):
    """ Google. 
    
    1. queue 2. maintain tail 3. another pointer for child """
    def flattern_list(self, head):
         if not head:
             return head
         queue = [head]
         while queue:
              cur = queue.pop(0)
              while cur:
                   if cur.child:
                       queue.append(cur.child)
                   cur = cur.next
              cur.next = 
