#include<stdio.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void minDepthRec(struct TreeNode* root, int level, int* minLevel){
    if(root->left == NULL && root->right == NULL){
        if(*minLevel > level){
            *minLevel = level;
        }
    }
    if(root->left != NULL){
        minDepthRec(root->left, level+1, minLevel);
    }
    if(root->right != NULL){
        minDepthRec(root->right, level+1, minLevel);
    }
}
int minDepth(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int minLevel = 10000;
    minDepthRec(root, 1, &minLevel);
    return minLevel;
}