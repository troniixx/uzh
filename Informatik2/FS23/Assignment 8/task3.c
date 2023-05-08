#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct TreeNode{
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

void insert(struct TreeNode** root, int val); void lrlp(struct TreeNode* root); int max(int a,int b);
#define N 8
int values[9]; int idx;

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

    lrlp(root);
    
    // this should return something in the style of [7, 15, 10, 13]
    for(int i = 0; i < N; i++) {
        printf(" %d\n", values[i]);
    }
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

int maxPathSum(struct TreeNode *root){
    int sum; int left_sum; int right_sum;

    if(!root){return 0;}
    
    left_sum = max(0, maxPathSum(root->left));
    right_sum = max(0, maxPathSum(root->right));

    
    idx = idx + 1;

    return root->val+max(lsum,rsum);

}

void lrlp(struct TreeNode *root) {
		int summy = maxPathSum(root);
		printf("The largest root-leaf path of the given tree equals to: %d\n", summy);
        return;
	}
