# Handle and Raise Exceptions in Python

- [Handle and Raise Exceptions in Python](#handle-and-raise-exceptions-in-python)
  - [Exception Handling](#exception-handling)
    - [Basic form of handling exceptions](#basic-form-of-handling-exceptions)
    - [Why handle excemtions?](#why-handle-excemtions)
    - [Variable assignment](#variable-assignment)
    - [Multiple exceptions](#multiple-exceptions)
    - [Multiple except clauses](#multiple-except-clauses)
    - [The else clause](#the-else-clause)
    - [The finally clause](#the-finally-clause)
  - [Raise Exceptions](#raise-exceptions)
    - [Basic form of raising exceptions](#basic-form-of-raising-exceptions)
    - [Exception with a custom message](#exception-with-a-custom-message)
  - [Re-raise and bubble up](#re-raise-and-bubble-up)
    - [User-defined exception](#user-defined-exception)
    - [When to raise](#when-to-raise)

## Exception Handling

### Basic form of handling exceptions

The standard way to handle exceptions is to use the `try…except` block. It’s pretty much like ``try…catch` block in many other programming languages, if you have such a background.
The `try` clause includes the code that potentially raises an exception. If everything works well in the `try` clause, no code in the except clause will be executed. The `try…except` block is completed and the program will proceed.

However, if an exception is raised in the `try` clause, Python will stop executing any more code in that clause, and pass the exception to the except clause to see if this particular error is handled there.

Let’s take a look at a trivial example of the most basic form of exception handling:

```python
def devide_tweleve(number):
  try:
    print(f'Result: {12/number}')
  except ZeroDivisionError:
    print('You can't divide 12 by zero')

```

```bash
>>> # Use the function
>>> divide_twelve(6)
Result: 2.0
>>> divide_twelve(0)
You can't divide 12 by zero.
```

As you can see, when the division works as expected, the result of this division (i.e., 2.0) is printed. However, when we try to divide the number by zero, Python raises the ZeroDivisionError. Fortunately, our function was written to handle this error, and the message “You can’t divide 12 by zero.” is printed to inform the user of this error.

### Why handle excemtions?

We now understand how to handle exceptions using the `try…except` block. But why do we bother to handle exceptions? The most essential benefit is to inform the user of the error, while still allowing the program to proceed. Let’s see some similar functions, with and without handling exceptions:

```python

>>> # Define a function without handling
>>> def division_no_handle(x):
...     print(f"Result: {20/x}")
...     print("division_no_handle completes running")
... 
>>> # Define a function with handling
>>> def division_handle(x):
...     try:
...         print(f"Result: {20/x}")
...     except ZeroDivisionError:
...         print("You can't divide a number with zero.")
...     print("division_handle completes running")
...
>>> # Call the functions
>>> division_handle(0)
You can't divide a number with zero.
division_handle completes running
>>> division_no_handle(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in division_no_handle
ZeroDivisionError: division by zero
```
As shown above, when we call the function that handles the exception, we see that the program executes until the end of the function (Lines 15–17). By contrast, when we call the function that doesn’t handle the exception, we see that the program can’t complete to the end of the function (Lines 18–22).

### Variable assignment

We can assign the exception to a variable such that we can retrieve more information about the exception. In the code below, we can assign the handled exception `TypeError` to the variable `e`, so we can ask Python to print the error message for us. As shown in Line 10, the error message is printed telling us that we can’t concatenate strings with integers:

```python
def concat_messages(x, y):
  try:
    print(f'{x + y}')
  except TypeError as e:
    print(f'Argument error: {e}')
```

```bash
>>> # Call the function
>>> concat_messages("Hello, ", 2020)
Argument Error: can only concatenate str (not "int") to str
```

### Multiple exceptions

We can handle multiple exceptions in the except clause. We’ll simply wrap possible exceptions in a tuple, as shown in Line 6 in the following code snippet. When we call the function, we intentionally make two distinct errors by raising the ValueError and ZeroDivisionError, respectively. The messages clearly tell us what exceptions are handled.

```python
def divide_six(number):
  try:
    formatted_number = int(number)
    result = 6/formatted_number
  except(ValueError, ZeroDivisionError) as e:
    print(f'Error {type(e)}: {e}')  
```

```bash
>>> # Use the function
>>> divide_six("six")
Error <class 'ValueError'>: invalid literal for int() with base 10: 'six'
>>> divide_six(0)
Error <class 'ZeroDivisionError'>: division by zero
```

### Multiple except clauses

Related to the previous section, when we expect different exceptions, we can actually have multiple `except` clauses with each handling some specific exceptions. Let’s modify the above function (i.e., `divide_six`) to create multiple `except` clauses, as shown below.

```python
def divide_six(number):
  try:
    formatted_number = int(number)
    result = 6/formatted_number
  except ValueError:
    print(f'This is a ValueError')
  except ZeroDivisionError:
    print(f'This is a ZeroDivisionError')

```

```bash
>>> # Use the function
>>> divide_six("six")
This is a ValueError
>>> divide_six(0)
This is a ZeroDivisionError
```
After the modification, when we call the function twice with the intention of raising two distinct exceptions each, the expected messages are printed for each except clause.

### The else clause

We can use an `else` clause in the try…except block. It should be noted that the `else` clause needs to appear after the except clause. The code in the `else` clause runs when the try clause completes without any exceptions raised. Let’s see it in use:

```python
def divide_eight(number):
  try:
    result  = 8/number
  except:
    print('Divide_eight has an error')
  else:
    print(f'Result: {result}')

```
```bash
>>> # Use the function
>>> divide_eight(0)
divide_eight has an error
>>> divide_eight(4)
Result: 2.0
```

The code has a function that uses an `else` clause in the try…except block. As you can see, the code in the `else` clause only runs when the try clause completes and no exceptions are raised. On the other hand, the code does not run when an exception is raised and handled.

### The finally clause

Besides the use of the `else` clause, we can also use a `finally` clause in the try…except block. Please note that the `finally` clause needs to be placed at the end of the block, below the `except` clause or `else` clause (if set). The code in the `finally` clause will run right before the entire `try…except` block completes (after executing code in the try or `except` clause). Importantly, the code in the `finally` clause will run regardless of the exception raising and handling status. Let’s see how it works:


```python
def divide_six(number):
  try:
    print(f'Result: {6/number}')
  except:
    print(f'Error encoutered')
  finally: 
    print('The function devide_six is completed')

```

```bash
>>> # Use the function
>>> divide_six(2)
Result: 3.0
The function divide_six is completed.
>>> divide_six(0)
Error Encountered
The function divide_six is completed.
```

As shown in the code snippet above, we have a function that has a `finally` clause. We call the function twice with the second call raising an exception. In both cases, the code in the `finally` clause runs successfully.


Another important thing to note with the use of the `finally` clause is that if the try clause includes a break, continue, and return statement, the `finally` clause will run first before executing the break, continue, or return statement. Many people can make mistakes here. Let’s take a look at a trivial example below:

```python

>>> # Check the order of running
>>> def get_integer(number):
...     try:
...         return int(number)
...     except:
...         print("Error Encountered")
...     finally:
...         return "No Numbers!"
... 
>>> # Use the function
>>> get_integer(5)
'No Numbers!'
>>> get_integer("hello")
Error Encountered
'No Numbers!'
```

## Raise Exceptions

### Basic form of raising exceptions

In the last section, we learned various features of using the `try…except` block to handle exceptions in Python, which are certainly necessary for more robust code. However, your code can be further strengthened if you know how to raise exceptions properly. Let’s first see a basic form:

```python
>>> # Raise exceptions
>>> raise Exception
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception
>>> raise NameError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError
>>> raise ValueError()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

As shown above, we use the `raise` keyword (in other programming languages, it’s called `throw`), followed by the exception class (e.g., Exception, NameError). We can also use the exception class constructor to create an instance, like ValueError(). These two usages have no differences, and the former is just a syntax sugar for the latter using the constructor.

### Exception with a custom message

We can also provide additional information about the exception that we’re raising. The easiest way to do it is simply to use the exception class constructor and include the applicable error message to create the instance. This is pretty straightforward:

```py
>>> raise ValueError("You can't divide something with zero.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: You can't divide something with zero.
>>> raise NameError("It's silly to make this mistake.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: It's silly to make this mistake.
```

## Re-raise and bubble up


As shown, all the exceptions are handled whenever they’re caught. However, it’s possible that we can re-raise the exception and pass the exception to the outside scope to see if it can be handled. Such passing of the exception to the outside is also known as bubbling up or propagation.

This feature is more useful when we write complicated code that involves nested structures (e.g., a function calling another function, which may call another function). With the exception re-raising, we can decide where to handle particular exceptions. Certainly, the exact location of handling a specific exception is determined on a case-by-case basis. Here, I can show you how we can re-raise an exception. Let’s see some code first:

```python

>>> # Define two functions with one calling the other
>>> def cast_number(number_text, to_raise):
...     try:
...         int(number_text)
...     except:
...         print("Failed to cast")
...         if to_raise:
...             print("Re-raise the exception")
...             raise
... 
>>> def run_cast_number(number_text, to_raise):
...     try:
...         cast_number(number_text, to_raise)
...     except:
...         print("Handled in run_cast_number")
... 
>>> # Use the functions 
>>> run_cast_number("six", False)
Failed to cast
>>> run_cast_number("six", True)
Failed to cast
Re-raise the exception
Handled in run_cast_number
```

In the above code, we have two functions, with run_cast_number calling the other function cast_number. We call the function with a string twice, both of which result in an exception, such that the message “Failed to cast” is printed because the exception is handled in the cast_number function. However, for the second time, we call the function, we ask the cast_number function to re-raise the exception (Lines 8–9) such that the except clause runs in the run_cast_number function (Lines 15 & 22–23).

### User-defined exception

In many cases, we can use the built-in exceptions to help us raise and handle exceptions in our project. However, Python gives us the flexibility of creating our own custom exception class. If you don’t know how to create a Python custom class, refer to my previous article on this:

Specifically, we need to declare a class as a subclass of the built-in Exception class. Conventionally, you should name your class as something ending with Error (e.g., MediumDataError).

```python
class FileExtensionError(Exception):
  def __init(self, filename, desired_ext):
    self.filename = filename
    self.desired_ext = desired_ext
  def __str__(self):
    return f'File {self.name} should have the extension: {self.desired_ext}'
```

```bash
>>> # Raise custom exceptions
>>> raise FileExtensionError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'filename' and 'desired_ext'
>>> raise FileExtensionError("test.xls", "csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.FileExtensionError: File test.xls should have the extension: csv.
```

As shown above, we create a custom exception class called `FileExtensionError`. When we raise such an exception, using the class name alone won’t work, as shown in Lines 10–13. Instead, we should instantiate this exception by setting the two positional arguments for the constructor method. As shown in Line 17, we can see the custom exception message, by implementing the __str__ method. In other words, the exception message is generated by calling the str() function.

### When to raise

We’ve learned how to raise built-in and custom exceptions. When we learn Python, most of the time, we only need to know how to handle exceptions. However, with the advancement of your Python skills, you may be wondering when you should raise an exception.

The rule of thumb is **you should raise an exception when your code will possibly run into some scenarios when execution can’t proceed**. By raising a proper exception, it will allow other parts of your code to handle the exception properly, such that the execution can proceed.

```python
def read_data(filename):
  file_parts = filename.split('.')
  if file_parts[-1] != 'csv':
    print('Wrong data type')
    raise Exception("Can't read non-csv data.")
  else:
    print('CSV data is read.')

def process_data(filename):
  try:
    read_data(filename)
  except Exception as e:
    print(f'Error {e}')
  else:
    print('Further process the data.')
```

```bash
>>> process_data("test.docx")
Wrong data type.
Error: Can't read non-csv data.
>>> process_data("test.csv")
CSV data is read.
Further process the data.
```

In the above code, we first define a function, read_data, that can read a file. Suppose that the other function process_data is a public API and we don’t have good control over what file type the user is going to pass. Therefore, when we read the data using the read_data function, we want to raise an exception, because our program can’t proceed without the correct data.

We call the public API process_data function twice, with one using the wrong data type and the other using the correct data type. For the former condition, the exception is properly raised and handled such that our program doesn’t crash and the user is also informed of the mistake about the API use.

[Source](https://medium.com/better-programming/how-to-handle-and-raise-exceptions-in-python-12-things-to-know-4dfef7f02e4)