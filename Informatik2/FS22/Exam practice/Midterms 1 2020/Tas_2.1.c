#include <stdio.h>

int search(int arr[], int n)
{

    int l = 0;
    int r = n -1;

    while( l < r){
        int m = (l+r)/2;
        if(l == m && arr[m] < arr[m+1]){
            l = r;
        }
        else if(l == m) {
            r = l;
        } else if (arr[m-1] > arr[m]){
            r = m;
        } else {
            l = m;
        }
    }

    return arr[l];
    }

/* Driver program to check above functions */
int main()
{
int arr[] = {1,2,4,5,7,9,6,3};
int n = sizeof(arr)/sizeof(arr[0]);
printf("The maximum element is %d", search(arr, n));
return 0;
}
