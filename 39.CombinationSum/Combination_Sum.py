curr = []
def isSafe(target, candidate, idx):
    global curr
    if target - sum(curr) - candidate[idx] >= 0:
        return True
    else:
        return False

def CombinationSumRec(candidate, rem, final, idx, target):
    global curr
    if rem == 0 and sum(curr) == target:
        if sorted(curr) not in final:
            final += [curr]
        return False
    
    for i in range(idx, len(candidate)):
        if isSafe(target, candidate, i):
            rem = rem - candidate[i]
            curr += [candidate[i]]

            if CombinationSumRec(candidate, rem, final, idx, target):
                return True
            curr = curr[:-1]

            rem += candidate[i]
    return False


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final = []

        rem = target
        CombinationSumRec(sorted(candidates), rem, final, 0, target)
        return final