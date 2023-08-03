#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 1000

int top = -1;
int stack[N];

void push(int data); int pop(); void peek(); bool isEmpty(); bool isFull();


int main(){
    
}

void push(int data){

    if(top == N-1){
        printf("Stack is full\n");
    } else{
        top += 1;
        stack[top] = data;
    }
}

void pop(){

    if(top == -1){
        printf("Stack is empty\n");
    } else{
        int data = stack[top];
        top -= 1;
        return data;
    }
    return -1;
}

void peek(){
    printf("The Element on the top of the stack is: %d", stack[top]);
}

bool isEmpty(){
    if(top == -1){
        return true;
    }
    return false;
}

bool isFull(){
    if(top == N-1){
        return true;
    }
    return false;
}