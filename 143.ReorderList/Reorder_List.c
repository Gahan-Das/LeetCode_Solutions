#include<stdlib.h>
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void reorder(struct ListNode* head){
    if(head == NULL || head->next == NULL){
        return;
    }
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    while(curr->next != NULL){
        prev = curr;
        curr = curr->next;
    }
    if(head->next == curr){
        curr->next = NULL;
    }
    else{
        curr->next = head->next;
    }
    
    head->next = curr;
    if(prev != NULL && head != prev){
        prev->next = NULL;
    }
    
    reorder(curr->next);
}
void reorderList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    reorder(head);
}