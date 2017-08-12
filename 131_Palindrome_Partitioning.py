class Solution(object):
    """ Backtracing(DFS). Time Complexity O(n^3)?. 
    TODO: DP+BFS O(n^2). """
    def isPalindrome(self, s):
        p1 = 0; p2 = len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1; p2 -= 1
        return True
    
    def helper(self, s, solution, solutions):
        if not s:
            solutions.append(solution)
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.helper(s[i+1:], solution+[s[:i+1]], solutions)
                
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        solutions = list()
        self.helper(s, [], solutions)
        return solutions
