class Solution(object):
    def isMatch(self, s1, s2, s3, i, j, k, table):
        try:
            return table[(j,k)]
        except:
            pass
        if i == len(s3) and j == len(s1) and k == len(s2):
            return True

        if j < len(s1) and k < len(s2):
            if s3[i] == s1[j] and s3[i] == s2[k]:
                table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j+1, k, table)
                if table[(j,k)] == False: 
                    table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j ,k+1, table)
                
                return table[(j,k)]
            if s3[i] == s1[j]:
                table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j+1, k, table)
                return table[(j,k)]
            if s3[i] == s2[k]:
                table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j, k+1, table)
                return table[(j,k)]
            table[(j,k)] = False
            return False
        if j < len(s1):
            if s3[i] == s1[j]:
                table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j+1, k, table)
                return table[(j,k)]
            table[(j,k)] = False
            return False
        if k < len(s2):
            if s3[i] == s2[k]:
                table[(j,k)] = self.isMatch(s1, s2, s3, i+1, j, k+1, table)
                return table[(j,k)]
            table[(j,k)] = False
            return False
        
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1)+len(s2):
            return False

        i = 0
        j = 0
        k = 0
        table = {}
        return self.isMatch(s1, s2, s3, i, j, k, table)

