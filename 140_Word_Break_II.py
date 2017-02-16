class Solution(object):
    """ Dynamic Programming.
    
    TLE for large data. """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = collections.defaultdict(list)
        dp[-1] = [[]]
        for i in range(len(s)):
            for w in wordDict:
                if (i-len(w)+1) >= 0 and s[i-len(w)+1:i+1] == w:
                    for word_li in dp[i-len(w)]:
                        dp[i].append(word_li + [w])
        res = [' '.join(word_li) for word_li in dp[len(s)-1]]
        return res
        
 class Solution(object):
    """ Dynamic Programming.
    
    Add a checker to avoid TLE for large data. """
    def isBreakable(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                if (i-len(w)+1) >= 0 and s[i-len(w)+1:i+1] == w:
                    if dp[i-len(w)+1] is True:
                        dp[i+1] = True
                        break
        return dp[-1]
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not self.isBreakable(s, wordDict):
            return []
        dp = collections.defaultdict(list)
        dp[-1] = [[]]
        for i in range(len(s)):
            for w in wordDict:
                if (i-len(w)+1) >= 0 and s[i-len(w)+1:i+1] == w:
                    for word_li in dp[i-len(w)]:
                        dp[i].append(word_li + [w])
        res = [' '.join(word_li) for word_li in dp[len(s)-1]]
        return res
