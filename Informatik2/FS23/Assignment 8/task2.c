#include <stdio.h>
#include <stdlib.h>

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
void preOrder(struct TreeNode *root); void inOrder(struct TreeNode *root); void postOrder(struct TreeNode *root);

int main(){
    struct TreeNode* root = NULL;

    insert(&root, 4); 
    insert(&root, 2); 
    insert(&root, 3);
    insert(&root, 8); 
    insert(&root, 6); 
    insert(&root, 7); 
    insert(&root, 9); 
    insert(&root, 12); 
    insert(&root, 12);

    printf("Before deleting node 4, 12 and 2\n");
    printTree(root);
    printf("\n");
    printf("\n");
    traverseTree(root);
    printf("\n");

    //delete(&root, 4); 
    //delete(&root, 12); 
    //delete(&root, 2);
    //printf("After deleting node 4, 12 and 2");
    //printf("\n");
    //printTree(root);
    //printf("\n");
    //traverseTree(root);

    return 0;
}

void insert(struct TreeNode **root, int val){
    
    struct TreeNode *current = *root;
    struct TreeNode *newNode = NULL;
    struct TreeNode *prev = NULL;

    newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = val;
    newNode->left = NULL;
    newNode->right = NULL;

    while(current != NULL){
        prev = current;
        if(val < current->val){
            current = current->left;
    } else {
        current = current->right;
    }
    }
    if(prev == NULL){
        *root = newNode;
    } else if(val < prev->val){
        prev->left = newNode;
    } else {
        prev->right = newNode;
            }
    }

//void delete(struct TreeNode** root, int val){
//    return;
//}

void traverseTree(struct TreeNode *root){
    printf("preOrder: ");
    preOrder(root);
    printf("\n");

    printf("inOrder: ");
    inOrder(root);
    printf("\n");

    printf("postOrder: ");
    postOrder(root);
    printf("\n");

    
}

void preOrder(struct TreeNode *root){
    printf("%d ", root->val);
    if(root->left){ preOrder(root->left); }
    if(root->right){ preOrder(root->right); }
}

void inOrder(struct TreeNode *root){
    if(root->left){ inOrder(root->left); }
    printf("%d ", root->val);
    if(root->right){ inOrder(root->right); }
}

void postOrder(struct TreeNode *root){
    if(root->left){ postOrder(root->left); }
    if(root->right){ postOrder(root->right); }
    printf("%d ", root->val);
}

void printHelper(struct TreeNode *root, int lvl){
    if(root == NULL){
        return; }

    if(root->left != NULL){
        printf("  %d -- %d : %d\n", root->val, root->left->val, lvl);
        printHelper(root->left, lvl+1);
    }
    if(root->right != NULL){
        printf("  %d -- %d : %d\n", root->val, root->right->val, lvl);
        printHelper(root->right, lvl+1);
    }
}

void printTree(struct TreeNode *root){
    printf("graph g {\n");
    printHelper(root, 1);
    printf("}\n");
}


