class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.val = 0 # sum of nums[start:end+1]
        self.start, self.end = start, end
        self.left = self.right = None
        
class NumArray(object):
    """ Segment Tree. 45%. 
    
    Segment tree methods and complexity
    buildTree: O(nlogn)
    updateTree: O(logn)
    sumRange: O(logn) - at each level visit at most 4 nodes 
    
    Corner cases: nums=[]
    """
    def buildTree(self, nums, start, end):
        """ Build segment tree like post-order traversal.
        Update val of current node after finishing left and right tree. 
        Stop condition: 1. start > end 2. leaf node - update val of leaf node.
        
        :param nums: list of nums
        :param start: start index
        :param end: end index
        :return root node of tree
        """
        if start > end: # Wrong: did not have this stop condition error with corner case: nums=[]
            return None
        node = SegmentTreeNode(start, end)
        if start == end:
            node.val = nums[start]
        else:
            mid = start+(end-start)/2
            left = self.buildTree(nums, start, mid)
            right = self.buildTree(nums, mid+1, end)
            node.left, node.right = left, right
            node.val = left.val + right.val 
            # node.val = (left.val if left else 0) + (right.val if right else 0) : not necessary because non-leaf node always have two children
        return node
    
    def updateTree(self, i, val, cur):
        """ Update segment tree. 
        Don't forget to update cur.val when finishing update left or right branch.
        Stop condition: when start == end == i 
        :param i: index (update nums[i])
        :param val: update nums[i] to val
        :param cur: current node
        """
        start, end = cur.start, cur.end
        if start == end == i:
            cur.val = val
            return
        mid = start+(end-start)/2
        if i <= mid:
            cur.val -= cur.left.val
            self.updateTree(i, val, cur.left)
            cur.val += cur.left.val
        else:
            cur.val -= cur.right.val
            self.updateTree(i, val, cur.right)
            cur.val += cur.right.val
    
    def sumRangeTree(self, i, j, cur):
        """ Get sum of nums[i:j+1] using segment tree. 
        Stop condition: i == cur.start and j == cur.end (if stop when cur.start = cur.end = i then complexity increases to O(nlogn)) 
        """
        start, end = cur.start, cur.end
        if i == start and j == end:
            return cur.val
        mid = start+(end-start)/2
        if j <= mid:
            return self.sumRangeTree(i, j, cur.left)
        elif i > mid:
            return self.sumRangeTree(i, j, cur.right)
        else:
            return self.sumRangeTree(i, mid, cur.left) + self.sumRangeTree(mid+1, j, cur.right)
            
    def sumRangeTree2(self, i, j, cur):
        """ Another way of writing sumRangeTree(). """
        if i > j:
            return 0
        start, end = cur.start, cur.end
        if i == start and j == end:
            return cur.val
        mid = start+(end-start)/2
        return self.sumRangeTree(i, min(j, mid), cur.left) + self.sumRangeTree(max(mid+1, i), j, cur.right)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums)-1)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateTree(i, val, self.root)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeTree(i, j, self.root)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
