from operator import itemgetter
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort( key = itemgetter(0) )
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1] = [ans[-1][0],max(intervals[i][1],ans[-1][1])]
            else:
                ans += [intervals[i]]
        return ans
