class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sort = sorted(nums)
        diff = 10**5
  
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while( i < j and j < k ):
                add = sort[i] + sort[j] + sort[k]
                if abs(target - add) < diff:
                    output = add
                    diff = abs(target - add)
                if add < target:
                    j = j + 1
                else:
                    k = k - 1
        return output

        