# Exercise 01

## Task 1: Searching the Corpus of the SAC

### a)

``` bash
ggrep -P -c '^[mM]' SAC-Jahrbuch_193*_mul_columns.txt
```

>Solution: 94005

### b)

``` bash
ggrep -P '.+en\s(VAFIN | VAIMP | VVFIN | VVIMP | VMFIN | VVINF | VAINF | VMINF | VVIZU | VVPP | VMPP | VAPP)' SAC-Jahrbuch_193*_mul_columns.txt | wc -l
```

>Solution: 69338

### c)

``` bash
ggrep -P '(VAFIN|VAIMP|VVFIN|VVIMP|VMFIN|VVINF|VAINF|VMINF|VVIZU|VVPP|VMPP|VAPP)\s(haben|sein)' SAC-Jahrbuch_193*_mul_columns.txt | ggrep -Po '(haben|sein)' | sort | uniq -c
```

>Solution: 10591 haben, 24416 sein

### d)

``` bash
ggrep -Pi '\w*([bcdfghjklmnprstvwxyz])(\w*\1){3,}\w*\s' SAC-Jahrbuch_193*_mul_columns.txt | sort | uniq -c | wc -l
```

>Solution: 2772

### e)

``` bash
ggrep -Pi '\w*([bcdfghjklmnprstvwxyz])(\w*\1){3,}\w*\s' SAC-Jahrbuch_193*_mul_columns.txt | sort | uniq | ggrep -Po '\s[A-Z]*\s' | sort | uniq -c | sort -rn
```

>Solution: 1269 NN (German, noun)

### f)

``` bash
ggrep -Po '\s(KOUI|KOUS|KON|KOKOM)\s.+' SAC-Jahrbuch_193*_mul_columns.txt | ggrep -Po '\s.+' | sort | uniq -c | sort -rn | head -5
```

>Solution:
39435        KON     und
4658         KOUS    dass
2977         KOKOM   als
2519         KON     oder
2228         KON     aber

### g)

m as second character
``` bash
ggrep -P '\s(VAFIN|VAIMP|VVFIN|VVIMP|VMFIN|VVINF|VAINF|VMINF|VVIZU|VVPP|VMPP|VAPP)\s\wm\w+' SAC-Jahrbuch_193*_mul_columns.txt | sort | uniq -c | sort -rn | head -3
```

>Solution: 14 SAC-Jahrbuch_1933_mul_columns.txt:stiegen       VVFIN   empor+steigen
     12 SAC-Jahrbuch_1938_mul_columns.txt:umgangen      VVPP    umgehen
     12 SAC-Jahrbuch_1937_mul_columns.txt:umgangen      VVPP    umgehen

### h)

``` bash
ggrep -P '^\S+-\S+\t' SAC-Jahrbuch_193*_mul_columns.txt | sort | uniq -c | wc -l
```

>Solution: 8428, a lot of French tokens

### i)

``` bash
ggrep -Po '(ab|an|auf|aus)\w+\t(VAFIN|VAIMP|VVFIN|VVIMP|VMFIN|VVINF|VAINF|VMINF|VVIZU|VVPP|VMPP|VAPP)' SAC-Jahrbuch_193*_mul_columns.txt | ggrep -Po '(ab|an|auf|aus)' | sort | uniq -c | sort -rn | head -1
```

>Solution: 9820 an

## Task 2: Searching a book from Project Gutenberg

### a)

``` bash
ggrep -P '?$' GreatGatsby.txt | head -n 5
```

>Solution: her back inside? What would happen now in the dim, incalculable hours?
"Come on!" His temper cracked a little. "What’s the matter, anyhow?
conception of the affair that couldn’t be measured?
"You said a bad driver was only safe until she met another bad driver?
There were no more than 4 matches. Because there is a lot of dialog in the story, we get better results by inserting an optional quotation mark after the question mark: ggrep -P '\?"*' GreatGatsby.txt | head -5
This way, we also get dialog sentences ending with ?, which give us a much better idea of the people and mood of the book (including a well-known line involving 2 main characters as the 4th match):
"She’s asleep. She’s three years old. Haven’t you ever seen her?"
"What you doing, Nick?"
"Who with?"
"Gatsby?" demanded Daisy. "What Gatsby?"
helplessly: "What do people plan?"

### b)

Characters sometimes have dialogues pre- or postfixed with their names, like ’Alice: How are you?’. identify if your book contains such a pattern, and extract the ten most frequently mentioned character names. Which character seems to be the most dominant or involved based on this?
Note: If your book does not contain this pattern, propose another way to identify character names in your book.

``` bash ggrep -P '\w:\s".' GreatGatsby.txt `````` would search for Name: ", but does not return any names.
By using a ggrep to capture capitalized words before or after the quotation marks (most likely names), we get better results: ``` bash ggrep -P '([A-Z]\w+\s*\w*:\s"|"\s[A-Z]\w+)' GreatGatsby.txt ``````
We can then extract the capitalized words only, sort and count them: ```bash ggrep -Po '([A-Z]\w+\s*\w*:\s"|"\s[A-Z]\w+)' GreatGatsby.txt | ggrep -Po '[A-Z]\w+' | sort | uniq -c | sort -rn ```

>Solution: The most frequent names are:
      9 Tom
      7 Gatsby
      5 Daisy
      2 Jordan

### c)

``` bash
ggrep -Pc '^[A-Z].*[A-Z]$' GreatGatsby.txt and ggrep -P '^[A-Z].*[A-Z]$' GreatGatsby.txt | head -3
```

>Solution: START: FULL LICENSE
	THE FULL PROJECT GUTENBERG LICENSE
	PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

### d)

``` bash
ggrep -Pc '(happy|joy|love|excited)' GreatGatsby.txt 
ggrep -Pc '(sad|sorrow|hate|angry)' GreatGatsby.txt 
```

>Solution: 81 // 26

## Reflection

### a)

>Very small mistakes in the RegEx can lead to very different results. It is important to be very precise when writing RegEx and it takes a long time to get used to it.

### b)

> It pretty much took from the day the exercise was released to the day we had to hand it in. It's important to be able to work on the RegEx uninterrupted, since it's quite difficult to take the work up again on a later day.