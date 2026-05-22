class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 1
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                flag = 0
       
        if flag:
            nums.sort()
        else:
            j = len(nums) - 1
            while nums[j-1] >= nums[j] and j != 1:
                j = j - 1
            next_max = nums[j]
            idx = j
            for i in range(j+1,len(nums)):
                if nums[i] < next_max and nums[i] > nums[j-1]:
                    next_max = nums[i]
                    idx = i
            nums[idx], nums[j-1] = nums[j-1], nums[idx]
            nums[j:] = sorted(nums[j:])
