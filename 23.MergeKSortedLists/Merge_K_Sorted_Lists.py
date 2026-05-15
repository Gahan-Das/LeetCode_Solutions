# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        output = []
        if len(lists) == 0:
            return None
        else:
            flag = 1
            for i in range(len(lists)):
                temp = lists[i]
                if temp != None:
                    flag = 0
                    break
                    
        if flag:
            return None
        else:
            ptr = []
            for i in range(len(lists)):
                temp = lists[i]
                ptr += [temp]

            while flag != 1:
                flag = 1
                min_val = 10**5
                for i in range(len(lists)):
                    
                    if ptr[i] == None:
                        continue
                    else:
                        flag = 0
                        if min_val > ptr[i].val:
                            temp = i
                            min_val = ptr[i].val
                if len(output) == 0:
                    head = ptr[temp]
                    output = [ptr[temp]]
                    ptr[temp] = ptr[temp].next
                    
                else:
                    output[-1].next = ptr[temp]
                    output += [ptr[temp]]
                    if ptr[temp] != None:
                        ptr[temp] = ptr[temp].next
   

            return head
