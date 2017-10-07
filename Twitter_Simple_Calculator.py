import operator


class Solution(object):
    """ Assumptions: +, -, *, /, only positive integer, no parentheses. """

    def calculate(self, s):
        if not s or not s.strip():
            return 0
        stack = list()
        sign = '+'
        num = 0
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            if ch in ['+', '-', '*', '/'] or i == len(s)-1:
                if i == len(s)-1:
                    num = num*10+int(ch)
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(operator.truediv(stack.pop(), num))
                num = 0
                sign = ch
                continue
            num = num*10+int(ch)
        return sum(stack)

assert(Solution().calculate(' ') == 0)
assert(Solution().calculate('123 + 454 *7 - 4') == 3297)
assert(Solution().calculate('123 + 456 *7/4') == 921)

