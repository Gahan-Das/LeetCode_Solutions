class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < min(nums):
            return 0
        if target > max(nums):
            return len(nums)
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        left = 0
        right = len(nums) - 1
        mid = -1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if target > nums[left]:
            return left+1
        if target > nums[mid]:
            return mid+1
        if target > nums[right]:
            return right+1
        return mid - 1
