#include<stdio.h>

//   Definition for singly-linked list.
struct ListNode {
     int val;
     struct ListNode *next;
};

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode *prev = NULL, *curr = head, *next = head->next;
    int count = 1;
    while(count != left){
        prev = curr;
        curr = next;
        next = next->next;
        count += 1;
    }
    struct ListNode *hold = prev, *temp = curr;
    while(count != right){
        curr->next = prev;
        prev = curr;
        curr = next;
        next = next->next;
        count += 1;
    }
    if(left != right){
        curr->next = prev;
    }
    
    if(left == 1){
        head = curr;
    }
    if(hold != NULL)
    {
        hold->next = curr;
    }
    temp->next = next;
    return head;

}