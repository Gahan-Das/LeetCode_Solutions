#include<stdlib.h>


struct ListNode {
   int val;
   struct ListNode *next;
};

struct ListNode* rotateRight(struct ListNode* head, int k) {
    int count = 0;
    struct ListNode *temp = head, *prev = NULL;

    while(temp != NULL){
        count++;
        temp = temp->next;
    }
    if(count == 0){
        return NULL;
    }
    int run = k % count;
    if(run == 0){
        return head;
    }
    int i = 0;
    temp = head;
    while(i != count-run){
        prev = temp;
        temp = temp->next;
        i++;
    }
    struct ListNode *tmp = temp;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = head;
    prev->next = NULL;
    head = tmp;
    return head;
}