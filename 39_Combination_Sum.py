class Solution(object):
    """ Backtracing(DFS). 
    
    画一下树就清楚了. """
    def helper(self, candidates, target, solution, solutions):
        if target == 0:
            solutions.append(solution)
            return
        if not candidates or candidates[0] > target:
            return
        for i, num in enumerate(candidates):
            self.helper(candidates[i:], target-num, solution+[num], solutions)
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = list()
        candidates.sort()
        self.helper(candidates, target, [], solutions)
        return solutions
