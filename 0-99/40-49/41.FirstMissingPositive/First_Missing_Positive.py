class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) >= 10**4:
            store = {}
            for i in nums:
                store[i] = 1
            for i in range(1, 10**5 + 2):
                try:
                    m = store[i]
                except:
                    return i
        for i in range(1, 10**5 + 2):
            if i not in nums:
                return i
        