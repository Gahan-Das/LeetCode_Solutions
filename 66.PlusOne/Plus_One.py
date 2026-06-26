class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if i == 0 and digits[i] == 9 and carry == 1:
                digits += [0]
                digits[i] = 1
            else:
                digits[i] = digits[i] + 1
                if digits[i] > 9:
                    digits[i] = 0
                else:
                    carry = 0
            if carry == 0:
                break
        return digits

        