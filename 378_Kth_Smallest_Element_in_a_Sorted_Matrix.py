from heapq import heappush, heappop

class Solution(object):
    """ Heap. """
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        m = len(matrix); n = len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        heap = [(matrix[0][0], 0, 0)]
        while 1:
            val, i, j = heappop(heap)
            k -= 1
            if k == 0:
                return val
            if 0 <= (i+1) < m and not visited[i+1][j]:
                heappush(heap, (matrix[i+1][j], i+1, j))
                visited[i+1][j] = True
            if 0 <= (j+1) < n and not visited[i][j+1]:
                heappush(heap, (matrix[i][j+1], i, j+1))
                visited[i][j+1] = True
