class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        return_str = ""
        if strs == [""]:
            return return_str
        if len(strs) == 1:
            return strs[0]
        for i in range(min(len(strs[0]), len(strs[1]))):
            if strs[0][i] == strs[1][i]:
                return_str += strs[0][i]
            else:
                break
        for i in range(2, len(strs)):
            if strs[i] == "":
                return_str = ""
                break
            for j in range(min(len(return_str), len(strs[i]))):
                if strs[i][j] == return_str[j]:
                    continue
                else:
                    return_str = strs[i][:j]
                    break
            if len(return_str) > len(strs[i]):
                return_str = strs[i]
        return return_str