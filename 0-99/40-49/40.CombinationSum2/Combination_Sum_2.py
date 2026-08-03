curr = []
index = []
def isSafe(target, candidate, i):
    global curr
    global index
    if target - sum(curr) - candidate[i] >= 0:
        if i not in index:
            return True
    return False
def combinationSum2Rec(candidate, target, idx, final):
    global curr
    global index
    if sum(curr) == target:
        if sorted(curr) not in final:
            final += [curr]
        return False
        
    i = idx
    while i != len(candidate):
        if isSafe(target, candidate, i):
            curr += [candidate[i]]
            index += [i]
            if combinationSum2Rec(sorted(candidate), target, idx+1, final):
                return True
            curr = curr[:-1]
            index = index[:-1]
            try:
                while candidate[i] == candidate[i+1]:
                    i = i + 1
            except:
                pass
        i = i + 1
    return False


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final = []
        combinationSum2Rec(sorted(candidates), target, 0, final)
        return final