class Solution(object):
    """ Tree. Stack. 49ms. 
    
    Traverse the serialized string from right to left. """
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        li = preorder.split(',')
        for i in range(len(li)):
            if li[i] == '#':
                stack.append(li[i])
            else:
                if len(stack) < 2:
                    return False
                if stack[-1] == '#' and stack[-2] == '#':
                    stack.pop(); stack.pop()
                else:
                    stack.append(li[i])
        return stack == ['#']
        
class Solution(object):
    """ Tree. Stack. 49ms. """
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        li = preorder.split(',')
        for i in range(len(li)-1, -1, -1):
            if li[i] == '#':
                stack.append(li[i])
            else:
                if len(stack) < 2:
                    return False
                if stack[-1] == '#' and stack[-2] == '#':
                    stack.pop()
                else:
                    stack.append(li[i])
        return stack == ['#']
        
