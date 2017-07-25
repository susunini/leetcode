class Solution(object):
    """ Google. Hard. Graph BFS. 82%. """
    test cases 1. [[1]] 2. [[1,1], [1,0]]
    caution: cannot be passed through 1
    """
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid); n = len(grid[0])
        dist_sum = [[0]*n for _ in range(m)]
        hit = [[0]*n for _ in range(m)] # Wrong: do not use hit
        build_num = sum([1 for i in range(m) for j in range(n) if grid[i][j] == 1])
        def bfs(start_row, start_col):
            m = len(grid); n = len(grid[0])
            visited = [[False]*n for _ in range(m)]
            visited[start_row][start_col] = True
            queue = [(start_row, start_col)]
            dis = 1; build_reached = 1
            while queue:
                size = len(queue)
                for _ in range(size):
                    row, col = queue.pop(0) # Wrong: queue.pop()
                    for adj_row, adj_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                        if (0 <= adj_row < m and 0 <= adj_col < n) and (not visited[adj_row][adj_col]):
                            visited[adj_row][adj_col] = True
                            if grid[adj_row][adj_col] == 0:
                                queue.append((adj_row, adj_col))
                                dist_sum[adj_row][adj_col] += dis
                                hit[adj_row][adj_col] += 1
                            elif grid[adj_row][adj_col] == 1:
                                build_reached += 1        
                dis += 1
            # print 'Start for building{}{}, visited: {}, dist_sum: {}'.format(start_row, start_col,    visited, dist_sum)
            return build_reached
    
        # print 'build_num: {}'.format(build_num)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    build_reached = bfs(i, j)
                    if build_reached != build_num:
                        return -1
        # print 'dist_sum: {} hit: {}'.format(dist_sum, hit)
        return min([dist_sum[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0 and hit[i][j] == build_num] or [-1]) # Wrong do not have: or [-1]

        
        
