global temp
def subsetRec(nums, length, ans, st):
    global temp
    if temp not in ans:
        ans += [temp[:]]
    for i in range(st, length):
        temp += [nums[i]]
        subsetRec(nums, length, ans, i+1)
        temp = temp[:-1]
    return False
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global temp
        length = len(nums)
        temp = []
        ans = []
        subsetRec(nums, length,  ans, 0)
        return ans