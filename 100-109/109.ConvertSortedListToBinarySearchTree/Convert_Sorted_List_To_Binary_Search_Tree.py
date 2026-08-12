# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if head == None:
            return None
        length = 0
        temp = head
        while(temp != None):
            length += 1
            temp = temp.next
        l = 0
        m = (l + length-1) // 2
        count = 0
        temp = head
        while(count < m):
            count += 1
            temp = temp.next
        root = TreeNode(temp.val)
        self.buildTreeL(root, l, count-1, head)
        self.buildTreeR(root, count+1-count, length-count-1, temp)
        return root
    def buildTreeL(self, root, l, r, head):
        if l <= r and l >= 0:
            m = (l + r) // 2
            count = 0
            temp = head
            while(count < m):
                count += 1
                temp = temp.next
            new = TreeNode(temp.val)
            root.left = new
            self.buildTreeL(new, l, count-1, head)
            self.buildTreeR(new, count+1-count, r-count, temp)
    def buildTreeR(self, root, l, r, head):
        if l <= r and l >= 0:
            m = (l + r) // 2
            count = 0
            temp = head
            while(count < m):
                count += 1
                temp = temp.next
            new = TreeNode(temp.val)
            root.right = new
            self.buildTreeL(new, l, count-1, head)
            self.buildTreeR(new, count+1-count, r-count, temp)
