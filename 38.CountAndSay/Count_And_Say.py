class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        val = "1"
        for i in range(n-1):
            temp = ""
            count = 1
            j = 0
            for j in range(1, len(val)):
                if val[j-1] == val[j]:
                    count += 1
                else:
                    temp += str(count) + str(val[j-1])
                    count = 1

            temp += str(count) + str(val[j])
            val = temp
        return val
        