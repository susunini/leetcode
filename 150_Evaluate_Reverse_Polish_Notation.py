class Solution(object):
    """ Stack. 72secs(68%). 
    
    Assumption: The list of operands and operators will compose a valid expression. """
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {
            '+': lambda x, y: y+x,
            '-': lambda x, y: y-x,
            '*': lambda x, y: y*x,
            '/': lambda x, y: int(operator.truediv(y,x)) # Wrong: '/': lambda x, y: operator.truediv(y,x)
        }
        stack = []
        for tok in tokens:
            try:
                stack.append(int(tok))
            except ValueError:
                stack.append(operators[tok](stack.pop(), stack.pop()))
        return stack.pop()
    
class Solution(object):
    """ 65ms(89%). """
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {
            '+': lambda x, y: y+x,
            '-': lambda x, y: y-x,
            '*': lambda x, y: y*x,
            '/': lambda x, y: int(operator.truediv(y,x)) #
        }
        stack = []
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                stack.append(operators[tok](stack.pop(), stack.pop()))
        return stack.pop()
            
