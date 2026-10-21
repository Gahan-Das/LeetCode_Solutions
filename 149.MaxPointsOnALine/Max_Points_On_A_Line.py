class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        store = {}
        maxVal = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j :
                    continue
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                if dx == 0:
                    dy = 1
                    dx = 0
                elif dy == 0:
                    dy = 0
                    dx = 1
                if dx < 0:
                    dy, dx = -dy,-dx
                a = dy if dy > 0 else -dy
                b = dx if dx > 0 else -dx
                while b != 0:
                    a,b = b,a%b   
                dy = dy / a
                dx = dx / a
                try:
                    store[(dy,dx)] += [i]
                except:
                    store[(dy,dx)] = [i]
        
            for key in store.keys():
                if len(store[key]) > maxVal:
                    maxVal = len(store[key])
            store = {}
        return maxVal+1