class Solution(object):
    """ Test cases: '0', '1', '5   '"""
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        signs = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-u,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(operator.truediv(x, y))
        }
        stack = []
        sign='+'
        operand = 0
        for i, ch in enumerate(s):
            if ch not in signs and ch != ' ':
                operand = operand*10+int(ch)
            if ch in signs or i == len(s)-1: #
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                else:
                    stack.append(signs[sign](stack.pop(), operand))
                operand = 0
                sign = ch
             
        return sum(stack) # Wrong: return stack.pop()
