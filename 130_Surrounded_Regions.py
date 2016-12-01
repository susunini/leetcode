class Solution(object):
    """
    https://discuss.leetcode.com/topic/18706/9-lines-python-148-ms/17
    DFS with python tricks
    Line 14 initialize stack: for k in range(max(m, n)) for four corners
    last line: e = X if e == 'C' otherwise e = 'O'
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not(any(board)): return
    
        m = len(board); n = len(board[0])
        stack = [ij for k in range(max(m,n)) for ij in (0, k), (m-1, k), (k, 0), (k, n-1)]
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'C'
                stack += (i-1, j), (i+1, j), (i, j-1), (i,j+1)
        board[:] = [['XO'[e == 'C'] for e in row] for row in board]
