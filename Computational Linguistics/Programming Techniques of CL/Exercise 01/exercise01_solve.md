# Exercise 01

## Task 1: Searching the Corpus of the SAC

### a)

``` bash
ggrep -P -c '^[mM]' SAC-Jahrbuch_193*_mul_columns.txt
```

>Solution:
SAC-Jahrbuch_1930_mul_columns.txt:9259
SAC-Jahrbuch_1931_mul_columns.txt:8648
SAC-Jahrbuch_1932_mul_columns.txt:9537
SAC-Jahrbuch_1933_mul_columns.txt:9198
SAC-Jahrbuch_1934_mul_columns.txt:8772
SAC-Jahrbuch_1935_mul_columns.txt:10167
SAC-Jahrbuch_1936_mul_columns.txt:9203
SAC-Jahrbuch_1937_mul_columns.txt:9039
SAC-Jahrbuch_1938_mul_columns.txt:10681
SAC-Jahrbuch_1939_mul_columns.txt:9501

### b)

``` bash
ggrep -P '(VAFIN | VAIMP | VVFIN | VVIMP | VMFIN | VVINF | VAINF | VMINF | VVIZU | VVPP | VMPP | VAPP)' SAC-Jahrbuch_193*_mul_columns.txt | ggrep -P '\w+en\t' SAC-Jahrbuch_193*_mul_columns.txt
```

>Solution:

### c)

``` bash
ggrep -Pow '\b(haben|sein)\b' SAC-Jahrbuch_193*_mul_columns.txt | sort | uniq -c
```

>Solution:
946 SAC-Jahrbuch_1930_mul_columns.txt:haben
2826 SAC-Jahrbuch_1930_mul_columns.txt:sein
 968 SAC-Jahrbuch_1931_mul_columns.txt:haben
2757 SAC-Jahrbuch_1931_mul_columns.txt:sein
 985 SAC-Jahrbuch_1932_mul_columns.txt:haben
3060 SAC-Jahrbuch_1932_mul_columns.txt:sein
1220 SAC-Jahrbuch_1933_mul_columns.txt:haben
3366 SAC-Jahrbuch_1933_mul_columns.txt:sein
 910 SAC-Jahrbuch_1934_mul_columns.txt:haben
2715 SAC-Jahrbuch_1934_mul_columns.txt:sein
 937 SAC-Jahrbuch_1935_mul_columns.txt:haben
2838 SAC-Jahrbuch_1935_mul_columns.txt:sein
1108 SAC-Jahrbuch_1936_mul_columns.txt:haben
2972 SAC-Jahrbuch_1936_mul_columns.txt:sein
1073 SAC-Jahrbuch_1937_mul_columns.txt:haben
3225 SAC-Jahrbuch_1937_mul_columns.txt:sein
1186 SAC-Jahrbuch_1938_mul_columns.txt:haben
3315 SAC-Jahrbuch_1938_mul_columns.txt:sein
1259 SAC-Jahrbuch_1939_mul_columns.txt:haben
3169 SAC-Jahrbuch_1939_mul_columns.txt:sein

sein: 29933
haben: 10582 

### d)

``` bash

```

>Solution:

### e)

``` bash

```

>Solution:

### f)

``` bash

```

>Solution:

### g)

m as second character
``` bash
ggrep -P '\b\wm\w+\b$' SAC-Jahrbuch_1930_mul_columns.txt
```

>Solution:

### h)

``` bash
ggrep -P '[a-zA-Z0-9]+-[a-zA-z0-9]+\t' SAC-Jahrbuch_193*_mul_columns.txt | wc
```

>Solution: 9612   28836  569251

### i)

``` bash

```

## Task 2: Searching a book from Project Gutenberg

### a)

``` bash

```

>Solution:

## Reflection

### a)

>

### b)

>