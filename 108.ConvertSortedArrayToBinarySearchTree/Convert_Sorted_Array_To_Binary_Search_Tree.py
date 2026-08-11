# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        self.buildTreeL(root, left, mid-1, nums)
        self.buildTreeR(root, mid+1, right, nums)
        return root
    def buildTreeL(self, root, left, right, nums):
        if(left <= right):
            mid = (left + right) // 2
            new = TreeNode(nums[mid])
            root.left = new
            self.buildTreeL(new, left, mid-1, nums)
            self.buildTreeR(new, mid+1, right, nums)
    def buildTreeR(self, root, left, right, nums):
        if(left <= right):
            mid = (left + right) // 2
            new = TreeNode(nums[mid])
            root.right = new
            self.buildTreeL(new, left, mid-1, nums)
            self.buildTreeR(new, mid+1, right, nums)
