# Homework 1
## Mert Erol, 20-915-245

### Exercise 1
#### a)

``` python
a = 1
b = 1.0
c = 2*a
d = 2+b
e = a-b
f = c/a
g = (-b)**(0.5)


print(f"a = {type(a)}\nb = {type(b)}\nc = {type(c)}\nd = {type(d)}\ne = {type(e)}\nf = {type(f)}\ng = {type(g)}\n ")
```
> Output:
> a = <class 'int'>
b = <class 'float'>
c = <class 'int'>
d = <class 'float'>
e = <class 'float'>
f = <class 'float'>
g = <class 'complex'>


#### b)

##### i)

> % is the modulo operator. It returns the remainder of the division of the first operand by the second.

##### ii)

> // is used for integer division. It returns the quotient of the division of the first operand by the second, rounded down to the nearest integer.

##### iii)

> When both operands are ints, the reuslt is an int. When one of the operands is a float, the result is a float.
> But if one is a int and the other is a float, the result is a float.

### Exercise 2

``` python
a = True
b = False
c = a and b
d = a or b
e = a*b
f = e or a
g = a and False or b

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}, g = {g}")
```

>Output:
a = True, b = False, c = False, d = True, e = 0, f = True, g = False

### Exercise 3

``` python
sentence = "You are using Python right now." #subtask a
print(type(sentence)) #subtask b
print(sentence[0]) #subtask c
print(sentence[-7:]) #subtask d
print(sentence[0:3]) #subtask e
print(len(sentence)) #subtask f
```

>Output:
<class 'str'>
Y
ht now.
You
31

### Exercise 4

``` python
array = [2, "xzy", 5, [2.71]] #subtask a
print(f"Subtask b: {type(array)}")
print(f"Subtask c: {array[-1]}")
names = ["Mert", "Erol"] #subtask d
concatenated = array + names #subtask e
print(f"Subtask f: {len(concatenated)}")
```

>Output:
Subtask b: <class 'list'>
Subtask c: [2.71]
Subtask f: 6