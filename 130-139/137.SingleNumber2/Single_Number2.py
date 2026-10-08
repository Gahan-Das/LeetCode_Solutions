class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        for key,val in dic.items():
            if val == 1:
                return key
            