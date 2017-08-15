class Solution(object):
    """ Largest Rectangle in Histogram. 单调栈. """
    def helper(self, heights):
        stack = []
        result = 0
        for i, height in enumerate(heights):
            if not stack or height >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and height < heights[stack[-1]]:
                    cur_index = stack.pop()
                    cur_height = heights[cur_index]
                    left_border = stack[-1]+1 if stack else 0
                    right_border = i-1
                    result = max(result, cur_height*(right_border-left_border+1))
                stack.append(i)
        while stack:
            cur_index = stack.pop()
            cur_height = heights[cur_index]
            left_border = stack[-1]+1 if stack else 0
            right_border = len(heights)-1
            result = max(result, cur_height*(right_border-left_border+1))
        return result
            
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix); n = len(matrix[0])
        heights = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                heights[i][j] = (heights[i-1][j] if i > 0 else 0) + 1
        result = 0
        for i in range(m):
            result = max(result, self.helper(heights[i]))
        return result
        
