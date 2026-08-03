class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        idx = 0
        for x in nums:
            if x in dict.keys():
                dict[x].append(idx)
            else:
                dict[x] = [nums.index(x)]
            idx += 1
        for x in dict.keys():
            y = target - x
            if y in dict.keys():
                if y != x:
                    return [nums.index(x), nums.index(y)]
                else:
                    try:
                        list = dict[x]
                        if len(list) == 2:
                            return list
                    except:
                        pass