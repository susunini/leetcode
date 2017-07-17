class Solution(object):
    """ Google. Stack. 85%. """
    def getLevel(self, token):
        return len(token)-len(token.lstrip('\t'))
        
    def getLen(self, token):
        return len(token.lstrip('\t'))
        
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        tokens = input.split('\n')
        res = 0; cur_len = 0; stack = []
        for tok in tokens:
            level = self.getLevel(tok); length = self.getLen(tok);
            length += 1 if level else 0
            while len(stack) > level:
                cur_len -= stack.pop()
            if '.' in tok:
                res = max(res, cur_len+length)
            else:
                cur_len += length
                stack.append(length)
        return res
                
