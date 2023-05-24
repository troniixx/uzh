#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct TreeNode{
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct list{
    int sum; int len; int data[20];
}list;

void insert(struct TreeNode** root, int val);
struct list* lrlp(struct TreeNode *root);


int main(){

    struct TreeNode* root = NULL;

    insert(&root, 7);
    insert(&root, 5);
    insert(&root, 2);
    insert(&root, 15);
    insert(&root, 21);
    insert(&root, 10);
    insert(&root, 9);
    insert(&root, 13);
    struct list *l = lrlp(root);
    printf("LRLP for the given graph: ");
    for(int i = (l->len)-1; i > 0; i--){ printf("%d--", l->data[i]); }
    printf("%d ", l->data[0]);
    printf("sum: %d", l->sum);

    return 0;
}

int max(int a,int b){
	if(a>b)
		return a;
	else
		return b;		
}

void insert(struct TreeNode** root, int val){
    struct TreeNode* new = NULL;
    struct TreeNode* prev = NULL;
    struct TreeNode* curr = *root;

    new = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    new->val = val;
    new->left = NULL;
    new->right = NULL;

    while(curr != NULL){
        prev = curr;
        if(val < curr->val){
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }

    if(prev == NULL){
        *root = new;
    } else if(val < prev->val){
        prev->left = new;
    } else {
        prev->right = new;
    }
}

struct list* lrlp(struct TreeNode *root) {
		if(root->left && root->right){
            struct list* left_list = lrlp(root->left);
            struct list* right_list = lrlp(root->right);
            if(left_list->sum > right_list->sum){
                left_list->data[left_list->len] = root->val;
                left_list->len++;
                left_list->sum += root->val;
                return left_list;
            } else{
                right_list->data[right_list->len] = root->val;
                right_list->len++;
                right_list->sum += root->val;
                return right_list;
            }
        } else if(root->left){
            struct list* left_list = lrlp(root->left);
            left_list->data[left_list->len] = root->val;
            left_list->len++;
            left_list->sum += root->val;
            return left_list;
        } else if(root->right){
            struct list* right_list = lrlp(root->right);
            right_list->data[right_list->len] = root->val;
            right_list->len++;
            right_list->sum += root->val;
            return right_list;
        } else {
            struct list* l = (struct list*)malloc(sizeof(struct list));
            l->sum = root->val;
            l->len = 1;
            l->data[0] = root->val;
            return l;
        }
	}
