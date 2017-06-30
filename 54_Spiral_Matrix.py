class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix); n = len(matrix[0])
        top = 0; bot = m-1; lft = 0; rt = n-1
        direction = 1
        res = []
        while top <= bot and lft <= rt:
            if direction % 4 == 1:
                res += matrix[top][lft:rt+1]
                top += 1
            elif direction % 4 == 2:
                res += [matrix[i][rt] for i in range(top, bot+1)]
                rt -= 1
            elif direction % 4 == 3:
                res += [matrix[bot][j] for j in range(rt, lft-1, -1)] #matrix[bot][rt:lft-1:-1]
                bot -= 1
            else:
                res += [matrix[i][lft] for i in range(bot, top-1, -1)]
                lft += 1
            direction += 1
        return res
