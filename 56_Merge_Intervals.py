# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
                
        if not intervals: 
            return intervals
        
        intervals.sort(key = lambda x: x.start)
        r_intervals = [intervals[0]]
        for t2 in intervals[1:]:
            t1 = r_intervals[-1]
            if t2.start > t1.end: # disjoint
                r_intervals.append(t2)
            else: # joint 
                r_intervals[-1] = Interval(t1.start, max(t1.end, t2.end))
        return r_intervals
            
            
            
        
        
        
