class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        output = []
        final_output = []
        for i in range(len(digits)):
            if i == 0:
                final_output += dict[digits[i]]
            else:
                
                output = final_output
                final_output = []
                for j in range(len(output)):
                    for k in range(len(dict[digits[i]])):
                        final_output += [output[j] + dict[digits[i]][k]]
        return final_output
        