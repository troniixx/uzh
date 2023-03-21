#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int l, m, r, i, j;
int leftToRightSum(int arr[], int l, int r); int midpointSum(int arr[], int l, int m, int r); int maximum(int a, int b, int c);



int main(){
    int arr[] = {2, 4, -6, -2, 3, 8};
    int n = 6;
    int maxSum = leftToRightSum(arr, 0, n-1);
    printf("The maximum subarray sum is: %d\n", maxSum);
    return 0;
}

int leftToRightSum(int arr[], int l, int r){
    
    if(l == r){
        return arr[l];
    }
    int mid = (l + r) / 2;
    int left = leftToRightSum(arr, l, mid);
    int right = leftToRightSum(arr, mid+1, r);
    int across = midpointSum(arr, left, mid, right);

    return maximum(left, right, across);
}

int midpointSum(int arr[], int l, int m, int r){
    
    int sum = 0;
    int left = INT_MIN;
    for(int i = m; i >= l; i--){
        sum = sum + arr[i];
        if(sum > left){
            left = sum;
        }
    }

    sum = 0;
    int right = INT_MIN;
    for(int i = m+1; i <= r; i++){
        sum = sum + arr[i];
        if(sum > right){
            right = sum;
        }
    }
    return left+right;
}

int maximum(int a, int b, int c){

    int maxi;

    if(a > b){
        maxi = a;
    } else {maxi = b;}

    if(c > maxi){
        maxi = c;}
    return maxi;
}
