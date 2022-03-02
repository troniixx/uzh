#include <string.h>
#include <stdio.h>

void selection_sort(int a[], int n) {
    int i, j, position, swap;

    for(i = 0; i < n - 1; ++i){
        position=i;
        for(j = i + 1; j < n; ++j){
            if(a[position] > a[j])
                position=j;
            }
            if(position != i){
                swap=a[i];
                a[i]=a[position];
                a[position]=swap;
                }
    }
}

void even_odd_selection(int a[], int n) {

    int even[n];
    int odd[n];
    int odd_count = 0, even_count = 0;
    selection_sort(a, n);

    for(int i = 0; i < n; ++i) {
        if(a[i]%2 == 0) {
            even[even_count] = a[i];
            even_count++;
        } else {
            odd[odd_count] = a[i];
            odd_count++;
        }
    }

    printf("Even array sorted: ");
    for(int i = 0; i < even_count; ++i){
        printf("%d ",even[i]);
    }

    printf("Odd array sorted: ");
    for(int i = 0; i < odd_count; ++i){
        printf("%d ",odd[i]);
    }
    return;
}


int main() {
    int a[8] = {2, 3, 4, 5, 6, 7, 8, 9};
    int n = 8;
    even_odd_selection(a, n);
}