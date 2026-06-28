class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start = 0
        width = 0
        temp = ""
        ans = []
        for i in range(len(words)):
            
            if width == 0:
                width = len(words[i])
            else:
                width += len(words[i])+1
            # print("start:",start,"i:",i,"temp:",temp,"width:",width,"ans:",ans)
            if width < maxWidth:
                continue
            elif width == maxWidth:
                for j in range(start, i):
                    temp += words[j] + ' '
                temp += words[i]
                ans += [temp]
                start = i + 1
                width = 0
            else:
                width -= len(words[i])+1
                print(maxWidth, width, i, start)
                print(ans)
                if i == start+1:
                    space = 0
                else:
                    space = (maxWidth - width + i - start) // (i - start - 1) 
                    # print("space:", space)
                for j in range(start, i-1):
                    temp += words[j] + space*' '
                temp += words[i-1]
                k = len(temp)
                while k < maxWidth:
                    temp += ' '
                    k = k + 1

                
                while temp[len(temp)-1] == ' ' and space != 0:
                    temp = temp[:-1]
                while len(temp) > maxWidth:
                    for k in range(maxWidth-1, -1, -1):
                        if temp[k] == ' ' and temp[k-1] == ' ':
                            temp = temp[:k] + temp[k+1:]
                            break
                print(temp)
                k = 0
                while len(temp) < maxWidth:
                    while k < maxWidth:
                        if temp[k] == ' ':
                            temp = temp[:k] + ' ' + temp[k:]
                            k = k + 2
                            break
                        k = k + 1
                    
                    
                ans += [temp]
                start = i
                try:
                    width = len(words[i])
                except:
                    pass
            temp = ""


 
        for j in range(start, i+1):
            temp += words[j] + ' '
        k = len(temp)
        while k < maxWidth:
            temp += ' '
            k = k + 1
        ans += [temp]

        last = ans[-1]
        last = last.split()
        temp = ""
        for k in range(len(last)-1):
            temp += last[k] + ' '
        try:
            temp += last[len(last)-1]
        except:
            pass
        temp = temp + (maxWidth - len(temp))*' '
        ans[-1] = temp

        if ans[-1] == maxWidth*' ':
            ans = ans[:-1]

        return ans