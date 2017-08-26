class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:i+1] == w and dp[i-len(w)+1]:
                    dp[i+1] = True
                    break
        return dp[-1]
