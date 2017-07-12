LESS_THEN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

class Solution(object):
    """ 55%. """
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        return self.helper(num)
    
    def helper(self, num):
        if num < 20:
            return LESS_THEN_20[num]
        if num < 100:
            return ' '.join([TENS[num/10], self.helper(num%10)]).strip()
        if num < 1000:
            return ' '.join([self.helper(num/100), 'Hundred', self.helper(num%100)]).strip()
        if num < 1000000:
            return ' '.join([self.helper(num/1000), 'Thousand', self.helper(num%1000)]).strip()
        if num < 1000000000:
            return ' '.join([self.helper(num/1000000), 'Million', self.helper(num%1000000)]).strip()
        else:
            return ' '.join([self.helper(num/1000000000), 'Billion', self.helper(num%1000000000)]).strip()
        
        
LESS_THEN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ['', 'Thousand', 'Million', 'Billion']

class Solution(object):
    """ 96%. """
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        return self.helper(num)
    
    def helper(self, num):
        if num < 20:
            return LESS_THEN_20[num]
        if num < 100:
            return ' '.join([TENS[num/10], self.helper(num%10)]).strip()
        if num < 1000:
            return ' '.join([self.helper(num/100), 'Hundred', self.helper(num%100)]).strip()
        i = 1
        while num >= pow(1000, i+1):
            i += 1
        print i
        return ' '.join([self.helper(num/pow(1000, i)), 
                         THOUSANDS[i], 
                         self.helper(num%pow(1000, i))]).strip()
