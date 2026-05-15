# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        flag = 1
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            temp = head.next
            prev = None
            curr = head
            next = head.next
            while curr != None and curr.next != None:
                curr.next = next.next
                next.next = curr
                if prev != None:
                    prev.next = next
                prev = curr
                curr = curr.next
                if curr != None:
                    next = curr.next
            head = temp
            return head