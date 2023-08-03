
## Aufgabe 1

##### a)

5/2 + 3

Type: float, Value: 5.5

##### b)
``` python
b1 = "13579"
b2 = "02468"
b1[5:] + b2[-5]
```

Type: 0, Value: str

##### c)
``` python
(lambda x: x%2 == 0) (2)
```
Type: Boolean, Value: True

##### d)
``` python
d = [[[1, 1], [2, 2]], [[3, 3], [4, 4]]]
d[0][2]
```
Type: Error, Value: IndexError

##### e)
``` python
class X: pass
class Y(X): pass
class Z(Y): pass
if isinstance(Z(), X):
    e = 1
else:
    e = 2.3
print(e)
```
Type: int, Value: 1

##### f)
``` python
f = sorted({ ’a’:1, ’b’:2, ’c’:3 }.items())
f[0]
```
Type: Tuples, Value: ("a", 1)

##### g)
``` python
def g(): 
    return False
"x" if not g else {}
```
Type: dict, Value: {}

##### h)
``` python
def addition(arr):
    s = 0
    for el in arr:
        if el % 2 == 0:
            s += el
    return s
addition([1, 2, 3, 4])
```
Type: int, Value: 6

##### i)
``` python
class Animal:
    def talk(self):
        return "Moo!"
class Dog(Animal):
    pass
dog = Dog()
dog.talk()
```
Type: str, Value: "Moo!"

##### j)
``` python
class Employee:
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = Employee.id
        Employee.id += 1
emp = Employee("Marc")
emp.id
```
Type: int, Value: 0