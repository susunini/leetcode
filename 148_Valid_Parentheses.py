class Solution(object):
    """ Wrong. """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_to_r = {'(':')', '[':']', '{':'}'}
        stack = []
        for i, ch in enumerate(s):
            if ch in l_to_r:
                stack.append(ch)
            else:
                if l_to_r[stack[-1]] != ch:
                    return False
                stack.pop()
        return True
        
class Solution(object):
    """ Stack. """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_to_r = {'(':')', '[':']', '{':'}'}
        stack = []
        for i, ch in enumerate(s):
            if ch in l_to_r:
                stack.append(ch)
            else:
                if not stack or l_to_r[stack[-1]] != ch:
                    return False
                stack.pop()
        if stack:
            return False
        return True
        
        
