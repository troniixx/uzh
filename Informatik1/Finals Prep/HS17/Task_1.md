
## Aufgabe 1

##### a)

```python
1.2+3
```
Type: float, Value: 4.2

##### b)

```python
b1 = "13579"
b2 = "02468"
print(b1[1:3] + b2[-3:-1])
```
Type: str, Value: 3546

##### c)

```python
def c(value):
    return value
c(False)
```

Type: bool, Value: False

##### d)

```python
d = [1, 2.3, (True, None, "bar")]
print(d[3][3][3])
```
Type: Error, Value: Index out of Range

##### e)

```python
def e():
    for i in { ’a’:1, ’b’:2, ’c’:3 }:
        return i
print(e())
```
Type: str, Value: "a"

##### f)

```python
f = ((1), (2,3))
f[0]
```

Type: int, Value: 1

##### g)

```python
class g(object):
    x = 1.2
    def __init__(self):
        self.x = 3
g.x
```

Type: float, Value: 1.2
