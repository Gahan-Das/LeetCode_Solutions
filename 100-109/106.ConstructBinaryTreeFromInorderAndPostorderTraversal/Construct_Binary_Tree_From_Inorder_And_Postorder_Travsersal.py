# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    index = 0
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(postorder) == 0:
            return None
        global index
        index = len(postorder)-1
        val = postorder[index]
        index -= 1
        idx = inorder.index(val)
        root = TreeNode(val)
        self.buildTreeRecR(root, inorder[idx:], postorder)
        self.buildTreeRecL(root, inorder[:idx], postorder)
        return root
    def buildTreeRecL(self, root, inorder, postorder):
        global index
        if index < 0:
            return
        if postorder[index] in inorder:
            val = postorder[index]
            index -= 1
            root.left = TreeNode(val)
            idx = inorder.index(val)
            self.buildTreeRecR(root.left, inorder[idx:], postorder)
            self.buildTreeRecL(root.left, inorder[:idx], postorder)
            
    def buildTreeRecR(self, root, inorder, postorder):
        global index
        if index < 0:
            return
        if postorder[index] in inorder:
            val = postorder[index]
            index -= 1
            root.right = TreeNode(val)
            idx = inorder.index(val)
            self.buildTreeRecR(root.right, inorder[idx:], postorder)
            self.buildTreeRecL(root.right, inorder[:idx], postorder)
            
        