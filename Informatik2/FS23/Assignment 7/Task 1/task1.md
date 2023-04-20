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

    Divide the array into two halves (arr[0] upto arr[n/2] is stack1 **and** arr[n/2 + 1] to arr[n-1] is stack 2).
    This requires to have two push functions (push1, push2), two pop functions (pop1, pop2) and two variables --> top1 of stack1 and top2 for stack2
    top1 has to be > 0 an top2 < n-1
    For more details check out this: [Implement two Stacks in an Array](https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/)

4. Explain how to implement a queue Q′ using two stacks. Analyze the running time of the enqueue
and dequeue operations on Q′.

5. Explain how to implement a stack S′ using two queues. Analyze the running time of the pop
and push operations on S′.
