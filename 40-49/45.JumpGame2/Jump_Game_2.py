class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        jump = {}
        jump[0] = 0
        for j in range(len(nums)): 
            for i in range(j+1, j+nums[j]+1):
                try:
                    if jump[i] > jump[j]+1:
                        jump[i] = jump[j] + 1
                except:
                    jump[i] = jump[j] + 1

        return jump[len(nums)-1]