# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 == None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        else:
            temp1 = list1
            temp2 = list2
            if(list1.val < list2.val):
                head = list1
                temp = list1
                temp1 = temp1.next
            else:
                head = list2
                temp = list2
                temp2 = temp2.next
            
            while(temp1 != None and temp2 != None):

                if(temp1.val < temp2.val):
                   
                    temp.next = temp1
                    temp1 = temp1.next
                    temp = temp.next
                else:
                    
                    temp.next = temp2
                    temp2 = temp2.next
                    temp = temp.next
            while(temp1 != None):
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next
            while(temp2 != None):
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
            return head
