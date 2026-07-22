ans = [[]]
temp = []
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global ans
        global temp
        nums.sort()
        temp = []
        ans = [[]]
        self.backtrack(nums, 0)
        return ans
    def backtrack(self, nums, i):
        global ans
        global temp
        if temp[:] not in ans:
            ans += [temp[:]]     
        for j in range(i,len(nums)):
            temp += [nums[j]]
            self.backtrack(nums, j+1)
            temp = temp[:-1]
        return False