# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        pathSum = 0
        tempList = []
        ansList = []
        self.hasPathSum(root, targetSum, pathSum, tempList, ansList)
        return ansList
    def hasPathSum(self, root, targetSum, pathSum, tempList, ansList):
        pathSum += root.val
        tempList += [root.val]
        if root.left == None and root.right == None:
            if pathSum == targetSum:
                ansList += [tempList]
        if root.left != None:
            self.hasPathSum(root.left, targetSum, pathSum, tempList[:], ansList)
        if root.right != None:
            self.hasPathSum(root.right, targetSum, pathSum, tempList[:], ansList)
        
