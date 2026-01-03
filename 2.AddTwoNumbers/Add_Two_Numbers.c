#include<stdio.h>
#include<stdlib.h>

struct ListNode {
     int val;
     struct ListNode *next;
 };
void Insert();
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *temp1 = l1, *temp2 = l2, *Root = NULL;
    int val1 = 0, val2 = 0, sum = 0, carry = 0;
    do
    {
        if(temp1 != NULL)
        {
            val1 = temp1->val;
            temp1 = temp1->next;
        }
        if(temp2 != NULL)
        {
            val2 = temp2->val;
            temp2 = temp2->next;
        }
        sum = val1 + val2 + carry;
        if(sum >= 10)
        {
            carry = sum / 10;
            sum %= 10;
        }
        else
        {
            carry = 0;
        }
        val1 = 0;
        val2 = 0;
        Insert(&Root, sum);
    }while(temp1 != NULL || temp2 != NULL);
    if(carry)
    {
        Insert(&Root, carry);
    }
    return Root;
}
void Insert(struct ListNode** Root, int data)
{

    struct ListNode* New = (struct ListNode*)malloc(sizeof(struct ListNode));
    New->val = data;
    New->next = NULL;
    if(*Root == NULL)
    {
        *Root = New;
    }
    else
    {
        struct ListNode* temp = *Root;
        while(temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = New;
    }
    
}