# Calculator Package Task

## setup.py code
```python
from setuptools import setup

# add some information about package
setup(name="app") # this is required, lines below are optional
version = "1.0"
description = "Python calculator app"
author = "Tom at Sparta Global"
author_email = "twilliams@spartaglobal.com"
url = "http://spartaglobal.com"
```
## calculator.py code
```python
class CalcFunctions:
    def add(self):
        self.x = int(input("What is the first number you would like to add in digits?  "))
        self.y = int(input("What is the second number you would like to add in digits?  "))
        return self.x + self.y

    def subtract(self):
        self.x = int(input("What number would you like to subtract from what in digits? Press enter after each number  "))
        self.y = int(input())
        return self.x - self.y

    def multiply(self):
        self.x = int(input("What is the first number you would like to multiply in digits?  "))
        self.y = int(input("What is the second number you would like to multiply in digits?  "))
        return self.x * self.y

    def divide(self):
        self.x = int(input("What number would you like to divide by what in digits? Press enter after each number  "))
        self.y = int(input())
        return self.x / self.y
```
## program.py code
```python
from app.calculator import CalcFunctions

calc_functions = CalcFunctions()

while True:
    func = str(input("What function would you like? Add, Subtract, Multiply or Divide?\n Type "
                     "'Exit' to finish.\n")).capitalize()
    if func == "Add":
        print(calc_functions.add())
    elif func == "Subtract":
        print(calc_functions.subtract())
    elif func == "Multiply":
        print(calc_functions.multiply())
    elif func == "Divide":
        print(calc_functions.divide())
    elif func == "Exit":
        break
    else:
        print("Unrecognised input, please try again")
```
