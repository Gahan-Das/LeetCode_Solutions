#include<stdio.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* partition(struct ListNode* head, int x) {
    if(head == NULL || head->next == NULL){
        return head;
    }
    struct ListNode *curr = head, *temp = NULL, *prev = NULL, *hold = NULL;
    while(curr != NULL){
        if(curr->val < x){
            if(prev == NULL){
                head = curr;
                prev = curr;
            }
            else{
                prev->next = curr;
                prev = curr;
            }
            if(temp != NULL){
                temp->next = curr->next;
            }
            curr = curr->next;
        }
        else{
            if(hold == NULL){
                hold = curr;
            }
            temp = curr;
            curr = curr->next;
        }
    }
    if(prev != NULL){
        prev->next = hold;
    }
    return head;
}