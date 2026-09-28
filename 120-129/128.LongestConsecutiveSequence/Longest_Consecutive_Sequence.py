class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        process = set()
        maps = {}
        val = {}
        maxCount = 0
        for i in nums:
            if i-1 in process and i+1 in process:
                process.add(i)
                lis = [maps[i-1][0]] +[ maps[i+1][-1]]
                value = val[i-1] + 1 + val[i+1]
                if maxCount < value:
                    maxCount = value
                maps[maps[i-1][0]] = lis
                maps[maps[i+1][-1]] = lis
                val[maps[i-1][0]] = value
                val[maps[i+1][-1]] = value
            elif i-1 in process:
                process.add(i)
                lis = [maps[i-1][0]] + [i]
                value = val[i-1] + 1
                if maxCount < value:
                    maxCount = value
                maps[maps[i-1][0]] = lis
                maps[i] = lis
                val[maps[i-1][0]] = value
                val[i] = value
            elif i+1 in process:
                process.add(i)
                lis = [i] + [maps[i+1][-1]]
                value = 1 + val[i+1]
                if maxCount < value:
                    maxCount = value
                maps[i] = lis
                maps[maps[i+1][-1]] = lis
                val[i] = value
                val[maps[i+1][-1]] = value
            else:
                process.add(i)
                value = 1
                maps[i] = [i]
                val[i] = value
                if maxCount < value:
                    maxCount = value
        return maxCount
        

