# Global Variables

This is a project to show that you CAN in fact use a global variable in a function in python.
[here's a tutorial](https://www.w3schools.com/python/python_variables_global.asp) on how. 

Basically:

```
i = 0 # this is your global variable

def function_that_accesses_the_variable():
  global i # you put this line, it tells python that 'i' should be accessed from outside
  i += 1 # do whatever
  # blah blah blah...

```

