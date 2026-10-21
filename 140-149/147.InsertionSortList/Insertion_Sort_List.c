#include<stdlib.h>
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void sort(struct ListNode** head, struct ListNode* prev, struct ListNode* tmp){
    if(tmp->val < (*head)->val){
        prev->next = tmp->next;
        tmp->next = *head;
        *head = tmp;
        
        return;
    }
    
    struct ListNode *temp = (*head)->next, *prv = *head;
    while(temp != tmp){
        if(prv->val <= tmp->val && tmp->val < temp->val){
            prev->next = tmp->next;
            prv->next = tmp;
            tmp->next = temp;
            return;
        }
        prv = temp;
        temp = temp->next;
    }
}
void special(struct ListNode** head){
    struct ListNode *temp = (*head)->next, *prev = *head;
    while(temp != NULL){
        prev->next = temp->next;
        temp->next = *head;
        *head = temp;
        temp = prev->next;
    }
}
struct ListNode* insertionSortList(struct ListNode* head) {
    struct ListNode *tmp = head, *prev = NULL;
    while(tmp != NULL){
        if(prev != NULL ){   
            if(tmp->val >= prev->val){
                prev = tmp;
                tmp = tmp->next;
                continue;
            }       
            sort(&head, prev, tmp);
        }
        prev = tmp;
        tmp = tmp->next;
    }
    return head;
}