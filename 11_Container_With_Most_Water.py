class Solution:
    """Naive: enumerate each pairs of lines O(n^2)."""
    pass
    

""" The gneral idea to find some maxium value is to go through all cases. Generally, to increase efficiency, we need to find a smart
way to cur off the useless cases and meanwhile guarentee that the max value can be reached through the rest of cases.

The widest container (using first and last line)is a good candicate, because of its width. Its water level is the height of the smaller
of two ends. All other containers are less wide and thus would need a higher water level in order to hold more water. Thus, after
evaluating the widest container, skip lines at both ends that don't support a higher height. Then evaluate that new container we arrived
at. Repeat until there are no more possible containers left.

For further clarification
https://discuss.leetcode.com/topic/3462/yet-another-way-to-see-what-happens-in-the-o-n-algorithm
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0; right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, h * w)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1; right -= 1
        return res
  
class Solution(object):
    """ Slightly faster """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0; right = len(height) - 1
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        
 class Solution(object):
    """ Using while to skip more cases; faster """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0; right = len(height) - 1
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
                while left < right and height[left] <= height[left-1]: 
                    left += 1
            else:
                right -= 1
                while left < right and height[right] <= height[right + 1]: 
                    right -= 1
        return res
        
 class Solution(object):
    """ concise and fastest """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0; right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, h * w)
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return res
