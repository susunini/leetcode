class Solution(object):
    """ Two Way BFS
    At each level, 
    1. find all words in bank which are one mutation away from any word in start
    2. swap start and end if start is larger than end
    3. remove start from bank
    return distance if start & end
    """
        
    def getHammDistance(self, word1, word2):
        result = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                result += 1
        return result
        
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int

        bank = set(bank)
        bank.discard(start)
        start = set([start]); end = set([end])
        level = 0
        while start:
            if start & end:
                return level
            start = set([next_word for cur_word in start for next_word in bank if self.getHammDistance(cur_word, next_word) == 1])
            if len(start) > len(end):
                start, end = end, start
            bank -= start
            level += 1
        if start & end:
            return level
        return -1
            
        
        
