#include<stdio.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* predecessor(struct TreeNode* temp){
    while(temp->right != NULL){
        temp = temp->right;
    }
    return temp;
}


void flatten(struct TreeNode* root) {
    if(root != NULL){
        if(root->left != NULL){
            struct TreeNode* pred = predecessor(root->left);
            pred->right = root->right;
            root->right = root->left;
            root->left = NULL;
        }
        flatten(root->right);
    }
}