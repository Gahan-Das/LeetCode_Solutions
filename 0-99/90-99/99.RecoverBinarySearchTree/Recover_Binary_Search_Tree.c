#include<stdio.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


void inOrd(struct TreeNode* root, int* arr, struct TreeNode** adr, int* k){
    if(root->left != NULL){
        inOrd(root->left, arr, adr, k);
    }
    *(arr + *k) = root->val;
    *(adr + *k) = root;
    *k += 1;
    if(root->right != NULL){
        inOrd(root->right, arr, adr, k);
    }
}
void recoverTree(struct TreeNode* root) {
    int arr[10000],k=0;
    struct TreeNode *adr[10000];
    inOrd(root,arr,adr,&k);
    int val1 =-1, val2 =-1;
    for(int i = 0; i < k-1; i++){
        if(arr[i] > arr[i+1]){
            if(val1 != -1){
                val1 = i+1;
            }
            if(val1 == -1){
                val2 = i;
                val1 = i+1;
            }
        }
    }
    int temp = (*(adr + val1))->val;
    (*(adr + val1))->val = (*(adr + val2))->val;
    (*(adr + val2))->val = temp;
}