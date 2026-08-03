/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode* temp = head;
    int length = 0;
    while(temp != NULL){
        length = length + 1;
        temp = temp->next;
    }
    if(k > length)
        return head;
    int count = 1;
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = head->next;
    temp = head;
    int chk = 1;
    struct ListNode* tmp = NULL;
    while(temp != NULL){
        int flag = 1;
        if(count % k != 0){
            temp = temp->next;
            count = count + 1;
        }
        else{
            if(chk){
                chk = 0;
                head = temp;
            }
            while(curr != temp){
                if(flag){
                    flag = 0;
                    curr->next = temp->next;
                    if(tmp != NULL)
                        tmp->next = temp;
                    tmp = curr;
                }
                else{
                    curr->next = prev;
                }
                prev = curr;
                curr = next;
                next = next->next;
                curr->next = prev;
            }
            count = count + 1;
            temp = next;
            prev = curr;
            curr = next;
            if (next != NULL)
                next = next->next;
        }
    }     
    return head;    
}