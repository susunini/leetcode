class Solution(object):
    """ Google. DP. 9%. """
    def preprocess(self, sentence, cols):
        n = len(sentence)
        dp = [0]*n
        for i in range(n):
            j = i; len_sum = 0
            while len_sum+len(sentence[j%n]) <= cols:
                len_sum += (len(sentence[j%n])+1)
                j += 1
            dp[i] = j-i
        return dp
    
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        dp = self.preprocess(sentence, cols)
        # print dp
        n = len(sentence); word_cnt = 0; line_start = 0
        for _ in range(rows):
            word_cnt += dp[line_start]
            line_start = (line_start+dp[line_start])%n
        # print word_cnt
        return word_cnt/n
        
        
