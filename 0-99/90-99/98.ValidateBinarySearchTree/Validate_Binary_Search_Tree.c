#include<stdio.h>
#include<stdbool.h>
//  * Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void inOrder(struct TreeNode* root, long int* arr, long int* i){
    if(root->left != NULL){
        inOrder(root->left, arr, i);
    }
    *(arr + *i) = root->val;
    *i += 1;
    if(root->right != NULL){
        inOrder(root->right, arr, i);
    }
    
}
bool isValidBST(struct TreeNode* root) {
    long int arr[10000], i = 0;
    inOrder(root, arr, &i);
    for(int j = 0; j < i-1; j++){
        if(arr[j] >= arr[j+1]){
            return false;
        }
    }
    return true;
}