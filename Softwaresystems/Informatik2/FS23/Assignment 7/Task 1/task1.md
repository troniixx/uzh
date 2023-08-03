# Task 1

1. Given an empty stack S, illustrate the result of each operation in the sequence push(4), push(1),
push(3), pop(), push(8), and pop(S).

    > - 4
    > - 1 4
    > - 3 1 4
    > - 1 4
    > - 8 1 4
    > - NULL

2. Given an empty queue Q, illustrate the result of each operation in the sequence enqueue(4),
enqueue(1), enqueue(3), dequeue(), enqueue(8), and dequeue().

    > - 4
    > - 4 1
    > - 4 1 3
    > - 1 3
    > - 1 3 8
    > - 3 8

3. Explain how to implement two stacks in one array A[] in such a way that neither stack overflows
unless the total number of elements in both stacks together is n. The push and pop operations
should run in O(1) time.

    &nbsp;&nbsp;&nbsp;&nbsp;Divide the array into two halves (arr[0] upto arr[n/2] is stack1 and arr[n/2 + 1] to arr[n-1] is stack 2).\
    &nbsp;&nbsp;&nbsp;&nbsp;This requires to have two push functions (push1, push2), two pop functions (pop1, pop2) and two variables (e.g top1 of stack1 and &nbsp;&nbsp;&nbsp;&nbsp;top2 for stack2.)\
    &nbsp;&nbsp;&nbsp;&nbsp;top1 has to be > 0 an top2 < n-1.\
    &nbsp;&nbsp;&nbsp;&nbsp;For more details check out this: [Implement two Stacks in an Array](https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/).

4. Explain how to implement a queue Q′ using two stacks. Analyze the running time of the enqueue
and dequeue operations on Q′.

    &nbsp;&nbsp;&nbsp;&nbsp;We have to stacks: one called Stack1 (this will be our input stack) and stack2 (this will be our output stack).

    &nbsp;&nbsp;&nbsp;&nbsp;**Enqueue operation:**\
    &nbsp;&nbsp;&nbsp;&nbsp;Push every new element into stack1  


    &nbsp;&nbsp;&nbsp;&nbsp;**Dequeue Operation:**\
    &nbsp;&nbsp;&nbsp;&nbsp;If(stack2 is empty) {pop every element in stack1 and push onto stack2 until stack1 is empty}\
    &nbsp;&nbsp;&nbsp;&nbsp;Pop everything from stack2.

5. Explain how to implement a stack S′ using two queues. Analyze the running time of the pop
and push operations on S′.

    &nbsp;&nbsp;&nbsp;&nbsp;We use two queues similar to task 4. One called queue1 and the other called queue2. Our elementto push to stack is "x".

    &nbsp;&nbsp;&nbsp;&nbsp;**Push operation**\
    &nbsp;&nbsp;&nbsp;&nbsp;if q1 is empty, enqueue to q1\
    &nbsp;&nbsp;&nbsp;&nbsp;if q1 is not empty, enqueue all elements from q1 to q2. Then enqueue element x to q1 and enqueue all elements from q2 back to q1.

    &nbsp;&nbsp;&nbsp;&nbsp;**Pop operation**\
    &nbsp;&nbsp;&nbsp;&nbsp;dequeue an element from q1.
