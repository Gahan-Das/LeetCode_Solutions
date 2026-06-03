class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        ans = {}
        greater = len(num2) if len(num2) > len(num1) else len(num1)
        for i in range(2*greater):
            ans[i] = 0
        Size1 = len(num1)-1
        Size2 = len(num2)-1
        Tsize = Size1+Size2
        for i in range(len(num2)-1, -1, -1):
            for j in range(len(num1)-1, -1, -1):
                mul = int(num2[i])*int(num1[j])
                ans[Tsize-i-j] += mul%10
                ans[Tsize-i-j+1] += mul//10
                if ans[Tsize-i-j] >= 10:
                    ans[Tsize-i-j+1] += 1
                    ans[Tsize-i-j] -= 10
                if ans[Tsize-i-j+1] >= 10:
                    ans[Tsize-i-j+2] += 1
                    ans[Tsize-i-j+1] -= 10
                k = Tsize-i-j+2
        answer = ""
        print(k)
        for i in range(k+1):
            try:
                answer = str(ans[i]) + answer 
            except Exception as e:
                print(e)
                pass
        i = 0
        while answer[i] == '0':
            answer = answer[1:]
        return answer

                

        