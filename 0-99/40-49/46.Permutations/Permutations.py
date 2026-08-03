
def permuteRec(temp, i, final):

    if i == len(temp):
        return False

    if temp not in final:
        final += [temp[:]]

    for j in range(i, len(temp)):
        temp[i], temp[j] = temp[j], temp[i]
        permuteRec(temp, i+1, final) 
        temp[i], temp[j] = temp[j], temp[i]
    return False

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        final = []
        permuteRec(nums, 0, final)
        return final
                
