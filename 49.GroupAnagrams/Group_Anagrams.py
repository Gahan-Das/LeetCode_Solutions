class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cpy = {}
        for i in range(len(strs)):
            try:
                tmp = sorted(strs[i])
                tmp = ''.join(tmp)
                cpy[tmp] += [strs[i]]
            except:
                tmp = sorted(strs[i])
                tmp = ''.join(tmp)
                cpy[tmp] = [strs[i]]
        ans = []
        for val in cpy.values():
            ans += [val]
        return ans
        