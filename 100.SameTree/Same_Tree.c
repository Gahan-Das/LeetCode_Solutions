#include<stdio.h>
#include<stdbool.h>

//   Definition for a binary tree node.
struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
};

bool isSameTreeRec(struct TreeNode* p, struct TreeNode* q){
    //printf("\n%d %d",p->val, q->val);
    if(p == NULL && q == NULL){
        return true;
    }
    else if(p == NULL || q == NULL){
        return false;
    }
    else{
        if(p->val != q->val){
            return false;
        }
        if(!isSameTreeRec(p->left, q->left)){
            return false;
        }
        if(!isSameTreeRec(p->right, q->right)){
            return false;
        }
        return true;
    }
}
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    return isSameTreeRec(p,q);
}