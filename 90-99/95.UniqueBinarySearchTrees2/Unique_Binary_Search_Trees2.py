# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
values = []
class Solution(object):
    def permutation(self, n, count, ans):
        global values
        if count == n:
            ans += [values]
        for i in range(1,n+1):
            if i not in values:
                values += [i]
                count += 1
                self.permutation(n, count, ans)
                values = values[:-1]
                count -= 1
        return False

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """ 
        global values
        values = []
        ans = []
        answer = []
        final_answer = []
        count = 0
        self.permutation(n, count, ans)
        for i in ans:
            temp = TreeNode()
            self.insert(i, temp)
            self.design(temp, n, final_answer, answer)
        return final_answer

    def insert(self, arr, temp):
        for i in arr:
            root = temp
            if root.val == 0:
                root.val = i
            else:
                while(1):
                    if i < root.val:
                        if root.left != None:
                            root = root.left
                        else:
                            root.left = TreeNode(i)
                            break
                    else:
                        if root.right != None:
                            root = root.right
                        else:
                            root.right = TreeNode(i)
                            break

    def design(self, temp, n, answer, ans):
        queue = []
        root = temp
        queue += [temp]
        count = [root.val]
        counter = 1
        while queue != []:
            root = queue[0]
            queue.pop(0)

            if self.isLeaf(root):
                continue
            if root.left == None:
                count += [None]
            else:
                queue += [root.left]
                count += [root.left.val]
                counter += 1
            if counter == n:
                break
            if root.right == None:
                count += [None]
            else:
                queue += [root.right]
                count += [root.right.val]
                counter += 1
            if counter == n:
                break
            
        
        if count not in ans:
            ans += [count]
            answer += [temp] 
    def isLeaf(self, root):
        if root.left == None and root.right == None:
            return True
        return False