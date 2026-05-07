class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sort = sorted(nums)
        output = []
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                flag = 1
        if flag == 0:
            return [[0, 0, 0]]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while(i < j and j < k):
                item = []
                if sort[i] + sort[j] + sort[k] == 0:
                    
                    min_val = min(sort[i], sort[j], sort[k])
                    max_val = max(sort[i], sort[j], sort[k])
                    middle_val = 0 - min_val - max_val
                    item = [min_val, middle_val, max_val]
                    if item not in output:
                        output += [item]
                    j = j + 1
                    k = k - 1
                elif sort[i] + sort[j] + sort[k] < 0:
                    j = j + 1
                else:
                    k = k - 1

        return output