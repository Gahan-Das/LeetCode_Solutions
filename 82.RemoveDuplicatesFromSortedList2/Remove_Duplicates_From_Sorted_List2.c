#include<stdio.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL){
        return head;
    }
    struct ListNode *prev = NULL, *temp = head, *next = head->next, *last = NULL;
    if(prev == NULL && next == NULL){
        return head;
    }
    head = NULL;
    while(temp != NULL){
        if(prev!=NULL)
            printf("Prev: %d ", prev->val);
        printf("Temp: %d ", temp->val);
        if(next!=NULL)
            printf("Next: %d", next->val);
        printf("\n");
        if(next == NULL){
            if(prev->val != temp->val){
                if(last == NULL){
                    head = temp;
                }
                else{
                    last->next = temp;
                }
                last = temp;
                prev = temp;
                temp = temp->next;
            }
            else{
                prev = temp;
                temp = temp->next;
            }
        }
        else if(temp->val != next->val){
            if(prev == NULL){
                head = temp;
                last = temp;
                prev = temp;
                temp = next;
                next = next->next;
            }
            else if(prev->val != temp->val){
                if(last != NULL){
                    last->next = temp;
                }
                else{
                    head = temp;
                }
                last = temp;
                prev = temp;
                temp = next;
                next = next->next;
            }
            else{
                prev = temp;
                temp = next;
                next = next->next;
            }
        }
        else{
            prev = temp;
            temp = next;
            next = next->next;
        }
    }
    if(last != NULL){
        last->next = NULL;
    }
    return head;
}