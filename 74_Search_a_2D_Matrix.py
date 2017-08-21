class Solution(object):
    """ Binary Search Once. 38%. """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix); n = len(matrix[0])
        
        start = 0; end = m*n-1
        while start+1 < end:
            mid = start+(end-start)/2
            if matrix[mid/n][mid%n] == target:
                return True
            if matrix[mid/n][mid%n] < target:
                start = mid
            else:
                end = mid
        if matrix[start/n][start%n] == target:
            return True
        if matrix[end/n][end%n] == target:
            return True
        return False
        
 class Solution(object):
    """ Binary Search Twice. 88%. """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix); n = len(matrix[0])
        start = 0; end = m-1
        while start+1 < end:
            mid = start+(end-start)/2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[start][0] <= target <= matrix[start][-1]:
            row = matrix[start]
        elif matrix[end][0] <= target <= matrix[end][-1]:
            row = matrix[end]
        else:
            return False
        
        start = 0; end = n-1
        while start+1 < end:
            mid = start+(end-start)/2
            if row[mid] == target:
                return True
            if row[mid] < target:
                start = mid
            else:
                end = mid
        if row[start] == target:
            return True
        if row[end] == target:
            return True
        return False
                
            
            
            
        
