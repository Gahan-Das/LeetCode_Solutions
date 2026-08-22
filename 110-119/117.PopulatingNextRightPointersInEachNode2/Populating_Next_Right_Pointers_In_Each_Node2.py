"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        level = 0
        queue = [(root, level)]

        while queue != []:
            temp, level = queue.pop(0)
            try:
                if queue[0][1] == level:
                    temp.next = queue[0][0]
            except:
                pass
            if temp.left != None:
                queue += [(temp.left, level+1)]
            if temp.right != None:
                queue += [(temp.right, level+1)]
        return root
        