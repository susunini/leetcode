class Solution(object):
    """ Union Find. 
    
    BTW how about using rank?
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not len(board) or not len(board[0]):
            return
        m = len(board); n = len(board[0])
        parents = [None]*(m*n+1)
        for i in range(len(parents)):
            parents[i] = i
            
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
        
