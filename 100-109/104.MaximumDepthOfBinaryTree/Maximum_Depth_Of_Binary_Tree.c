#include<stdio.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int maxValue = 0;
void maxDepthRec(struct TreeNode* root, int level){
    if(level > maxValue){
        maxValue = level;
    }
    if(root->left != NULL){
        maxDepthRec(root->left, level+1);
    }
    if(root->right != NULL){
        maxDepthRec(root->right, level+1);
    }
}
int maxDepth(struct TreeNode* root) {
    maxValue = 0;
    if(root == NULL){
        return maxValue;
    }
    maxDepthRec(root, 1);
    return maxValue;
}