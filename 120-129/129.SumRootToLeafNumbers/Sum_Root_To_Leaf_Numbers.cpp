#include<iostream>
//Definition for a binary tree node.
struct TreeNode {
   int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int totalValue = 0;
    void sumTree(TreeNode* root, int value){
        if(root == NULL){
            return;
        }
        value = value*10 + root->val;
        sumTree(root->left, value);
        if(root->left == NULL && root->right == NULL){
            totalValue += value;
        }
        sumTree(root->right, value);
    }
    int sumNumbers(TreeNode* root) {
        totalValue = 0;
        sumTree(root, 0);
        return totalValue;
    }
};