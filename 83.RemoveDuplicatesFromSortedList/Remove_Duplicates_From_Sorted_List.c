#include<stdio.h>
//  Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL){
        return head;
    }
    struct ListNode *next = head->next, *curr = head, *prev = NULL;
    if(prev == NULL && next == NULL){
        return head;
    }
    while(curr != NULL){
        if(next == NULL){
            if(prev == NULL){
                head = curr;
            }
            else{
                prev->next = curr;
            }
            prev = curr;
            curr = curr->next;
        }
        else if(curr->val != next->val){
            if(prev == NULL){
                head = curr;
            }
            else{
                prev->next = curr;
            }
            prev = curr;
            curr = next;
            next = next->next;
        }
        else{
            curr = next;
            next = next->next;
        }
    }
    return head;
}