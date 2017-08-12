class Solution(object):
    """
    Backtracing: backtrace both solution and xy_sums and xy_diffs. 
    
    a solution <=> a valid list of column indexes to position queens
    (x1, y1) and (x2, y2) are in the same diagonal line <=> abs(x1 - x2) == abs(y1 - y2) OR
    [(x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2)]
    """
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(row, cols, xy_sums, xy_diffs):
            if len(cols) == n:
                sols.append(cols)
                return
            for col in range(n):
                if col not in cols and (row + col) not in xy_sums and (row - col) not in xy_diffs:
                    dfs(row+1, cols+[col], xy_sums+[row+col], xy_diffs+[row-col])
            
        sols = []
        dfs(0, [], [], [])
        return [['.'*col + 'Q' + '.'*(n-col-1) for col in sol] for sol in sols]
