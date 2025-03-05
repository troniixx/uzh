- What special values can you get when working with float?
  - float('inf')
  - float('-inf')
  - float('nan')  

- What options do you have to include a number in a string?
  - Use str(number) and concatenate
  - Use f-strings
  - Use format
  - Use the older % formatting

- What are the advantages of using functions?
  - Reusability: avoid repeating the same logic  
  - Better organization and readability  
  - Easier testing and debugging  
  - Modular design  

- What is the structure of a function in Python?
  - Definition starts with def function_name(parameters):
  - Docstring describing the function  
  - Code
  - return (optional)  

- What is the difference between print(res) and return res? When do you use which?
  - print(res) displays the result to the console
  - return res sends the result back to the caller

- What is the difference between foo(1) and foo[1]?
  - foo(1) calls the function foo with an argument 1  
  - foo[1] accesses the element at index 1 of the object foo

- What does if __name__ == "__main__": do?
  - Checks if the module is being run directly  
  - Code inside this if block only runs when the file is executed as a script and not when it’s imported as a module

- How do you make your documentation available for the help(...) function?
  - Write a docstring at the start of a module, class, or function
  - Then help(my_func) will display that docstring

- What is the difference between default arguments, positional arguments and keyword arguments? How do you use them?
  - Positional arguments: matched by their position in the function call
  - Keyword arguments: matched by name in the function call order doesn’t matter
  - Default arguments: provide a default value so if you don’t pass a value, it uses the default

- How do you use the data type Fraction?  
  - Automatically reduces fractions and allows exact rational arithmetic
