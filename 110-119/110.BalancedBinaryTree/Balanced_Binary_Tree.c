#include<stdio.h>
#include<stdbool.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


int check(struct TreeNode* root, int level){
    if(root == NULL){
        return level;
    }
    int left = check(root->left, level+1);
    int right = check(root->right, level+1);
    printf("%d %d %d\n",root->val, left, right);
    if(abs(left - right) > 1){
        return 5000;
    }
    if(left > right){
        return left;
    } else {
        return right;
    }
}
bool isBalanced(struct TreeNode* root) {
    if(root == NULL){
        return true;
    }
    else if(root->left == NULL && root->right == NULL){
        return true;
    }
    int left = check(root->left, 0);
    if(left == 5000){
        return false;
    }
    int right = check(root->right, 0);
    if(right == 5000){
        return false;
    }
    if(abs(left - right) > 1){
        return false;
    } else {
        return true;
    }
}