from typing import List

def mergeInterval(interval1, interval2, i, intervals):
    if not interval1 or not interval2: 
        return
    if interval1[1] < interval2[0]:
        return
    elif interval1[1] <= interval2[1]:
        interval1[:] = [interval1[0], interval2[1]] if not [interval1[0], interval2[1]] in intervals[:i] else []
        interval2[:] = []        
    else:
        interval1[:] = [interval1[0], interval1[1]] if not [interval1[0], interval1[1]] in intervals[:i] else []
        interval2[:] = []

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        else:
            intervals = sorted(intervals, key=lambda x: x[0])
            for i in range(0, len(intervals) - 1):
                if len(intervals) < i:
                    break
                for j in range(i+1, len(intervals)):
                    mergeInterval(intervals[i], intervals[j], i, intervals)
                intervals = list(filter(lambda x: x, intervals))
            return intervals
                