class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        i = 0; result = 0; sign = 1
        while i < len(s):
            if s[i].isdigit():
                cur_num = 0
                while i < len(s) and s[i].isdigit():
                    cur_num = cur_num*10+int(s[i])
                    i += 1
                result += cur_num*sign
                continue
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0; sign = 1
            elif s[i] == ')':
                result = result*stack.pop()+stack.pop()
            i += 1
        return result
