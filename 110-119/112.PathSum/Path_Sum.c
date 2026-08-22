#include<stdio.h>
#include<stdbool.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool hasPathSumRec(struct TreeNode* root, int targetSum, int pathSum){
    pathSum += root->val;
    if(root->left == NULL && root->right == NULL){
        if(pathSum == targetSum){
            return true;
        }
        return false;
    }
    if(root->left != NULL){
        if(hasPathSumRec(root->left, targetSum, pathSum)){
            return true;
        }
    }
    if(root->right != NULL){
        if(hasPathSumRec(root->right, targetSum, pathSum)){
            return true;
        }
    }
    return false;
}
bool hasPathSum(struct TreeNode* root, int targetSum) {
    if(root == NULL){
        return false;
    }
    if(hasPathSumRec(root, targetSum, 0)){
        return true;
    }
    else{
        return false;
    }
}