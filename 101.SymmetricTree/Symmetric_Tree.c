#include<stdio.h>
#include<stdbool.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isSymmetricRec(struct TreeNode* left, struct TreeNode* right){
    if(left == NULL || right == NULL){
        return true;
    }
    if(left->val != right->val){
        return false;
    }
    if(left->left == NULL && right->right == NULL && left->right == NULL && right->left == NULL){
        return true;
    }
    else if((left->left == NULL && right->left == NULL)||(left->right == NULL && right->right == NULL)||(left->left == NULL && right->right != NULL)||(left->left != NULL && right->right == NULL)||(left->right == NULL && right->left != NULL)||(left->right != NULL && right->left == NULL)){
        return false;
    }
    else{  
        if(!isSymmetricRec(left->left, right->right)){
            return false;
        }
        if(!isSymmetricRec(left->right, right->left)){
            return false;
        }
    }
    return true;
}
bool isSymmetric(struct TreeNode* root) {
    if(root->left == NULL && root->right == NULL){
        return true;
    }
    else if(root->left == NULL || root->right == NULL){
        return false;
    }
    return isSymmetricRec(root->left, root->right);
}