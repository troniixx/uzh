#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
  int val;
  struct TreeNode* left;
  struct TreeNode* right;
  struct TreeNode* parent;
};

struct TreeNode* insert(struct TreeNode *root, struct TreeNode *parent, int val) {
  struct TreeNode* newTreeNode = NULL;
  if (root == NULL) {
    newTreeNode = malloc(sizeof(struct TreeNode));
    newTreeNode->val = val;
    newTreeNode->left = NULL;
    newTreeNode->right = NULL;
    newTreeNode->parent = parent;
    return newTreeNode;
  }
  if (val > root->val) {
    root->right = insert(root->right, root, val);
  } else {
    root->left = insert(root->left, root, val);
  }
  return root;
}

struct TreeNode* search(struct TreeNode* root, int val) {
  struct TreeNode* current = root;
  while (current != NULL && current->val != val) {
    if (val < current->val) {
      current = current->left;
    } else {
      current = current->right;
    }
  }
  return current;
}


struct TreeNode* leftRotate(struct TreeNode* root, int key) {
  
}

struct TreeNode* rightRotate(struct TreeNode* root, int key) {
    //Write code here
}

void printTreeRecursive(struct TreeNode *root) {
  if (root == NULL)
    return;
  if (root->left != NULL) {
    printf("  %d -- %d\n", root->val, root->left->val);
    printTreeRecursive(root->left);
  }
  if (root->right != NULL) {
    printf("  %d -- %d\n", root->val, root->right->val);
    printTreeRecursive(root->right);
  }
}

void printTree(struct TreeNode* root) {
  printf("graph g {\n");
  printTreeRecursive(root);
  printf("}\n");
}

int main() {
  struct TreeNode* root = NULL;
  printf("Inserting: 4, 2, 3, 8, 6, 7, 9, 12, 1\n");
  root = insert(root, root,  4);
  root = insert(root, root, 2);
  root = insert(root, root, 3);
  root = insert(root, root, 8);
  root = insert(root, root, 6);
  root = insert(root, root, 7);
  root = insert(root, root, 9);
  root = insert(root, root, 12);
  root = insert(root, root, 1);
  printTree(root);
  root = leftRotate(root,8);
  printTree(root);
  root = rightRotate(root,4);
  printTree(root);
  return 0;
}