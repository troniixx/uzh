#include <stdio.h>

struct TreeNode{
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode *newTreeNode(int name){
    struct TreeNode *newNode = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    newNode->val = name;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void insert(struct TreeNode** root, int val); void delete(struct TreeNode** root, int val); void traverseTree(struct TreeNode* root); void printTree(struct TreeNode* root);

int main(){
    struct TreeNode* root = NULL;

    insert(root, 4); 
    insert(root, 2); 
    insert(root, 3); 
    insert(root, 8); 
    insert(root, 6); 
    insert(root, 7); 
    insert(root, 9); 
    insert(root, 12); 
    insert(root, 12);

    printf("Before deleting node 4, 12 and 2");
    printTree(root);
    printf("\n");
    traverseTree(root);
    printf("\n");

    delete(root, 4); 
    delete(root, 12); 
    delete(root, 2);

    printf("After deleting node 4, 12 and 2");
    printf("\n");
    printTree(root);
    printf("\n");
    traverseTree(root);
}

void insert(TreeNode **root, int val){
    
    struct TreeNode *newNode = newTreeNode(val);

    if(root == NULL){
        root = newNode;
        return; }

    

}
