# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp = head
        sz = 0
        while temp != None:
            sz = sz + 1
            temp = temp.next
        temp = head
        prev = None
        count = 0
        while count < sz - n:
            count = count + 1
            prev = temp
            temp = temp.next
        if prev == None and sz == 1:
            head = None
            return head
        elif prev == None:
            head = temp.next
            return head
        prev.next = temp.next
        return head
        