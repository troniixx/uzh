#include <stdio.h>
int main()
{
    int array[5] = {7, 4, 9, 2, 8};
    int loop, largest, second;

    //Compare first two elements of the array and define which one is larger (largest) and smaller (second)
    if (array[0] > array[1]){
        largest = array[0];
        second = array[1];
    }else{
        largest = array[1];
        second = array[0];
    }


    //work thorugh the array starting at the third element and comapre it to the pre defined largest and second and
    //adjust values of largest and second accordingly
    for (loop = 2; loop < 5; loop++){
        if (largest < array[loop]){
            second = largest;
            largest = array[loop];
        }else if (second < array[loop]){
            second = array[loop];
        }
    }

    printf("Largest - %d \nSecond - %d \n", largest, second);

    return 0;
}