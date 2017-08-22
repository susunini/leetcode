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
        
class Solution(object):
    """ Union Find. """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not len(board) or not len(board[0]):
            return
        m = len(board); n = len(board[0])
        parents = [i for i in range(m*n+1)]
            
        def getRoot(e):
            while e != parents[e]:
                parents[e] = parents[parents[e]]
                e = parents[e]
            return e
            
        def isConnected(e1, e2):
            return getRoot(e1) == getRoot(e2)
            
        def union(e1, e2):
            r1, r2 = getRoot(e1), getRoot(e2)
            if r1 == r2:
                return
            if r1 == m*n:
                parents[r2] = r1
            else:
                parents[r1] = r2
            
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'O':
                    continue
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    union(i*n+j, m*n)
                if i != 0 and board[i-1][j] == 'O':
                    union(i*n+j, (i-1)*n+j)
                if j != 0 and board[i][j-1] == 'O':
                    union(i*n+j, i*n+(j-1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not isConnected(i*n+j, m*n):
                    board[i][j] = 'X'

class Solution(object):
    """ Union Find. Using ranks. """
    def solve(self, board):
        if not board or not board[0]:
            return
        m = len(board); n = len(board[0])
        dummy = m*n
        parents = [i for i in range(m*n+1)]
        ranks = [0]*(m*n+1)
        ranks[m*n] = m*n
        
        def getRoot(e):
            while e != parents[e]:
                parents[e] = parents[parents[e]]
                e = parents[e]
            return e
        
        def union(e1, e2):
            root1 = getRoot(e1)
            root2 = getRoot(e2)
            if root1 == root2:
                return
            if ranks[root1] < ranks[root2]:
                parents[root1] = root2
            elif ranks[root1] > ranks[root2]:
                parents[root2] = root1
            else:
                ranks[root2] += 1
                parents[root1] = root2
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    union(i*n+j, dummy)
                if i > 0 and board[i-1][j] == 'O':
                    union(i*n+j, (i-1)*n+j)
                if j > 0 and board[i][j-1] == 'O':
                    union(i*n+j, i*n+(j-1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if getRoot(i*n+j) == m*n: # Wrong: if parents[i*n+j] == m*n
                    continue
                board[i][j] = 'X'
