class Solution(object):
    """ 20171007. """
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid); n = len(grid[0])
        x_list = list(); y_list = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    x_list.append(i)
                    y_list.append(j)
        x_list.sort(); y_list.sort() 
        meet_x, meet_y = x_list[len(x_list)/2], y_list[len(y_list)/2]
        return sum([abs(x-meet_x) for x in x_list]) + sum([abs(y-meet_y) for y in y_list])
