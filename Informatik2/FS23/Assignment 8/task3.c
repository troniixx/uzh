#include <stdio.h>

struct TreeNode{
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

void insert(struct TreeNode** root, int val); int lrlp(struct TreeNode* root);

int main(){

    struct TreeNode* root = NULL;

    insert(root, 7);
    insert(root, 5);
    insert(root, 2);
    insert(root, 15);
    insert(root, 21);
    insert(root, 10);
    insert(root, 9);
    insert(root, 13);

    lrlp(root);
}