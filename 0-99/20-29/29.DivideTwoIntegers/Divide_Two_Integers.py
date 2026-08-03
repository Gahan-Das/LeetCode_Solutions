class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0) ^ (divisor < 0):
            answer = (-1*dividend) // divisor
            answer *= -1
        else:
            answer = dividend // divisor
        
        if answer < -2**31:
            return -2**31
        elif answer > 2**31-1:
            return 2**31-1
        else:
            return answer
            

        