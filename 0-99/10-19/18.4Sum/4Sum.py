class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        sort = sorted(nums)
        if len(nums) <= 3:
            return []
  
        for i in range(len(nums) - 3):
            for j in range(i, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while(k < l):
                    if sort[i] + sort[j] + sort[k] + sort[l] == target and i != j != k != l :
                        if [sort[i], sort[j], sort[k], sort[l]] not in output:
                            output += [[sort[i], sort[j], sort[k], sort[l]]]
                        k = k + 1
                    elif sort[i] + sort[j] + sort[k] + sort[l] < target:
                        k = k + 1
                    else:
                        l = l - 1

        return output
