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
        queue = []
        count = 1
        countNode = 1
        queue += [root]
        while queue != []:
            temp = queue.pop(0)
            if temp.left != None:
                queue += [temp.left]
            if temp.right != None:
                queue += [temp.right]

            if countNode == count:
                countNode = 1
                count *= 2
            else:
                countNode += 1
                temp.next = queue[0]
        return root