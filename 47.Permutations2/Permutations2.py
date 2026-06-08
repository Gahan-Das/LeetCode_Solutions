def permuteUniqueRec(nums, i, store):
    if i == len(nums):
        return False

    if nums[:] not in store:
        store += [nums[:]]
    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        permuteUniqueRec(nums, i+1, store)
        nums[i], nums[j] = nums[j], nums[i]
    return False
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        store = []
        permuteUniqueRec(nums, 0, store)
        return store

        