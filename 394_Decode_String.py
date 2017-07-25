class Solution(object):
    """ Google. Stack. """
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []; num = 0; substr = ''
        
        def insert_substr(substr):
            if not stack or not isinstance(stack[-1], int):
                stack.append(1)
            stack.append(substr)
            
        def helper():
            res = ''
            while stack:
                top = stack.pop()
                if top == '[':
                    break
                if isinstance(top, int):
                    res = substr*top+res
                else:
                    substr = top
            return res
        
        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(num); num = 0
                stack.append('[')
            elif ch == ']':
                insert_substr(substr); substr = ''
                stack.append(helper())
            elif ch.isdigit():
                if substr: insert_substr(substr); substr = ''
                num = num*10+int(ch)
            else:
                if num: stack.append(num); num = 0
                substr += ch
        if substr: insert_substr(substr)
        return helper()
                
        
