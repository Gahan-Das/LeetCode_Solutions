# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        queue = [(root,0)]
        dic = {}
        while queue != []:
            root,level = queue.pop(0)
            try:
                dic[level] += [root.val]
            except:
                dic[level] = [root.val]
            if root.left != None:
                queue += [(root.left,level+1)]
            if root.right != None:
                queue += [(root.right,level+1)] 
        ans = []
        for key,value in sorted(dic.items()):
            if key % 2 == 1:
                value.reverse()
                ans += [value]
            else:
                ans += [value]
        return ans
    