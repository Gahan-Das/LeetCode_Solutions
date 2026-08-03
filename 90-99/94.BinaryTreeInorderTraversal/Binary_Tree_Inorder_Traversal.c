#include<stdio.h>
#include<stdlib.h>

//  Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void inOrder(int* arr, struct TreeNode* root, int* returnSize){
    if(root->left != NULL){
        inOrder(arr, root->left, returnSize);
    }
    arr[*returnSize] = root->val;
    *returnSize += 1;
    if(root->right != NULL){
        inOrder(arr, root->right, returnSize);
    }
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    if(root == NULL){
        int* arr = (int*)malloc(sizeof(int));
        *returnSize = 0;
        return arr;
    }
    else if(root->left == NULL && root->right == NULL){
        int* arr = (int*)malloc(sizeof(int));
        *arr = root->val;
        *returnSize = 1;
        return arr;
    }
    *returnSize = 0;
    int* list = (int*)malloc(100*sizeof(int));
    inOrder(list, root, returnSize);

    return list;
}