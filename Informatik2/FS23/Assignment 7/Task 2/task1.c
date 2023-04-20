#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 1000

int top = -1;
int stack[N];

void push(int data); int pop(); void printStack();


int main(){
    push(5);
    push(10);
    push(12);
    push(6);
    push(1);
    printf("Before Pop: ");
    printStack();
    printf("\n");
    printf("After Pop: ");
    pop();
    pop();
    printStack();
}

void push(int data){

    if(top == N-1){
        printf("Stack is full\n");
    } else{
        top += 1;
        stack[top] = data;
    }
}

int pop(){

    if(top == -1){
        printf("Stack is empty\n");
    } else{
        int data = stack[top];
        top -= 1;
        return data;
    }
    return -1;
}

void printStack(){
    if(top >= 0){
        for(int i = top; i >= 0; i--){
            printf("%d ", stack[i]);
        }
    } else {
        printf("The stack is empty!\n");
    }
}
