# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [(root, 0)]
        dic = {}
        while queue != []:
            root, level = queue.pop(0)
            try:
                dic[level] += [root.val]
            except:
                dic[level] = [root.val]
            if root.left != None:
                queue += [(root.left, level+1)]
            if root.right != None:
                queue += [(root.right, level+1)]
        ans = []
        for key, val in sorted(dic.items(), reverse=True):
            ans += [val]
        return ans
