class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        val = 0
        max_val = 0
        stack = []
        index = []
        for i in range(len(heights)):
            index += [[]]
            while stack != [] and heights[i] <= heights[stack[-1]]:
                index[stack[-1]] += [i]
                stack = stack[:-1]
            if stack != []:
                index[i] += [stack[-1]]
                stack.append(i)
            else:
                stack.append(i)
                index[i] += [-1]
        while stack != []:
            index[stack[-1]] += [len(heights)]
            stack = stack[:-1]
        for i in range(len(heights)):
            val = heights[i] * (index[i][1] - index[i][0] - 1)
            if max_val < val:
                max_val = val
        return max_val