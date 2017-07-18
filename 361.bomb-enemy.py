# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy
#
# Medium (38.81%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '["0E00","E0WE","0E00"]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# ⁠Note that you can only put the bomb at an empty cell.
#
# Example:
#
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
#
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#
class Solution(object):
    """ TLE. """
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        matrix1 = [[0]*n for _ in range(m)]
        matrix2 = [[0]*n for _ in range(m)]
        matrix3 = [[0]*n for _ in range(m)]
        matrix4 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W':
                    matrix1[i][j] = (matrix1[i][j-1] if j > 0 else 0) + int(grid[i][j] == 'E')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 'W':
                    matrix2[i][j] = (matrix2[i][j+1] if j < n-1  else 0) + int(grid[i][j] == 'E')
        for j in range(n):
            for i in range(m):
                if grid[i][j] != 'W':
                    matrix3[i][j] = (matrix3[i-1][j] if i > 0  else 0) + int(grid[i][j] == 'E')
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                if grid[i][j] != 'W':
                    matrix4[i][j] = (matrix4[i+1][j] if i < m-1  else 0) + int(grid[i][j] == 'E')
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, sum([matrix1[i][j], matrix2[i][j], matrix3[i][j], matrix4[i][j]]))
        # print matrix1, matrix2, matrix3, matrix4
        return res
