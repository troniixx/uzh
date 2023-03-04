#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define N 10000
int top1 = -1;
int top2 = -1;
int top3 = -1;

int stack1[N];
int stack2[N];
int stack3[N];

int hanoi(); int fill(); void push(); int pop(); int peek(); bool isEmpty(); bool isFull();

int main(){
    int disks, moves;
    printf("Enter # of Disks: ");
    scanf("%d", &disks);
    printf("Enter # of Moves: ");
    scanf("%d", &moves);

    hanoi(disks, stack1[], stack2[], stack3[], moves);
    return 0;
}

int hanoi(int disks, int stack1[], int stack2[], int stack3[], int moves){
    
    
}

int fill(int stack[], int disks){
    
}

void push(int stack[], int top){
    if(top == N-1){
        printf("Cant add more elements\n")
    } else {
        int x; 
        printf("Enter element to pe pushed: ")
        scanf("%d",&x);
        top += 1;
        stack[top] = x;
    }
}

int pop(int stack[], int top){
    if(top == -1){
        printf("Stack already empty!\n");
    } else {
        int x = stack[top];
        printf("Popping %d\n", x);
        top -= 1;
        return x;
    }
    return -1;
}

int peek(int stack[], int top){
    int x = stack[top];
    return x;
}

bool isEmpty(int top){
    if(top == -1){
        printf("Stack is empty!");
        return true
    }
    return false;
}

bool isFull(int top){
    if(top == N-1){
        printf("Stack is full!");
        return true;
    } 
    return false;
}

