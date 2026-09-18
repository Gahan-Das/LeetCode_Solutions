#include<iostream>
#include<limits.h>
using namespace std;
// Definition for a binary tree node.
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
    int calcMax(TreeNode* root, int& maxi){
        if (root == NULL){
            return 0;
        }
        int maxi1 = INT_MIN;
        int maxi2 = INT_MIN;
        int lV = calcMax(root->left, maxi1);
        int rV = calcMax(root->right, maxi2);
        maxi = root->val + max(max(maxi1, 0) , max(maxi2, 0));
        return max(max(maxi, max(maxi1, 0)+root->val+max(maxi2, 0)) , max(lV,rV));
    }
    int maxPathSum(TreeNode* root) {
        int value = negTracker(root);
        cout << value;
        if(value < 0){
            return value;
        }
        int maxi = INT_MIN;
        int val = calcMax(root, maxi);
        return max(val, maxi);
    }
    int negTracker(struct TreeNode* root){
        if(root->val < 0){
            int val1 = -1000;
            int val2 = -1000;
            if(root->left != NULL){
                val1 = negTracker(root->left);
            }
            if(root->right != NULL){
                val2 = negTracker(root->right);
            }
            return max(max(val1,val2),root->val);
        }
        return 1;
    }
};