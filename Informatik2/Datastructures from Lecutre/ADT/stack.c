#include <stdio.h>

int MAX = 8;
int stack[10];
int top = -1;

int isempty(){ if(top == -1){ return 1; } else { return 0;} }

int isfull(){ if(top == MAX){ return 1; } else { return 0; } }

int peek(){ return stack[top]; }

int push(int data){

    if(!isfull()) {
        top = top+1;
        stack[top] = data;
    } else {printf("Stack is full, could not add the data!\n"); }
}

int pop(){
    int data;

    if(!isempty()){
        data = stack[top];
        top = top-1;
        return data;
    } else { printf("Stack is empty, no data to return!\n"); }
}



