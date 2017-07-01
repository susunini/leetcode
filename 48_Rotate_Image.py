class Solution(object):
    """ Pythonic. 94%. 
    1  2  3  4         13 14 15 16          13 9  5   1
    5  6  7  8    =>   9  10 11 12    =>    2  6  10  14
    9  10 11 12        5  6  7  8           3  7  11  15
    13 14 15 16        1  2  3  4           4  8  12  16
    
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        
class Solution(object):
    """ Similar to solution above but in place. 84%. """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
