from operator import itemgetter
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        intervals += [newInterval]
        intervals.sort(key = itemgetter(0))
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans += [intervals[i]]
        return ans