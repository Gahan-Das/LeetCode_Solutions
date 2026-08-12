# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    index = 0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        global index
        index = 0
        val = preorder[index]
        index += 1
        idx = inorder.index(val)
        root = TreeNode(val)
        self.buildTreeRecL(root, inorder[:idx], preorder)
        self.buildTreeRecR(root, inorder[idx:], preorder)
        return root
    def buildTreeRecL(self, root, inorder, preorder):
        global index
        if index >= len(preorder):
            return 
        if preorder[index] in inorder:
            val = preorder[index]
            root.left = TreeNode(val)
            index += 1
            idx = inorder.index(val)
            self.buildTreeRecL(root.left, inorder[:idx], preorder)
            self.buildTreeRecR(root.left, inorder[idx:], preorder)
    def buildTreeRecR(self, root, inorder, preorder):
        global index
        if index >= len(preorder):
            return 
        if preorder[index] in inorder:
            val = preorder[index]
            root.right = TreeNode(val)
            index += 1
            idx = inorder.index(val)
            self.buildTreeRecL(root.right, inorder[:idx], preorder)
            self.buildTreeRecR(root.right, inorder[idx:], preorder)
