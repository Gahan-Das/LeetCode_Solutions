# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderRec(self, root):
        dic = {}
        queue = [(root,0)]
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
        answer = []
        for j,i in sorted(dic.items()):
            answer += [i]
        return answer
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return self.levelOrderRec(root)
