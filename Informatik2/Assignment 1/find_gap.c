#include <stdio.h>

const int MAX_LENGTH = 1000;

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

int main() {
    printf("Values of A separated by spaces (non-number to stop): ");
    int timestamps[MAX_LENGTH];
    int pos = 0;
    while (scanf("%d", &timestamps[pos]) == 1) {
        pos++;
    }

    selection_sort(timestamps, pos);
    int longest = 0;

    for (int i = 1; i < pos; i++) {
    int gap = timestamps[i] - timestamps[i - 1];
    if (gap > 1 && gap > longest) {
    longest = gap;
        }
    }


    printf("Longest gap: %d\n", longest);
    printf("Oldest timestamp: %d\n", timestamps[0]);
    printf("Most recent timestamp: %d\n", timestamps[pos - 1]);
    return 0;
}