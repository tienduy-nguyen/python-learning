# Master Python Lambda Functions With These 4 Don’ts

- [Master Python Lambda Functions With These 4 Don’ts](#master-python-lambda-functions-with-these-4-donts)
  - [Don’t Return Any Value](#dont-return-any-value)
  - [Don’t Forget About Better Alternatives](#dont-forget-about-better-alternatives)
  - [Don’t Assign It to a Variable](#dont-assign-it-to-a-variable)
  - [Don’t Forget About List Comprehension](#dont-forget-about-list-comprehension)


Lambda functions are anonymous functions in Python. Using them is a handy technique in a local environment when you need to perform a small job. Some people simply refer to them as lambdas, and they have the following syntax:

```
lambda arguments: expression
```


The creation of a `lambda` function is signaled by the `lambda` keyword, followed by the list of arguments and a single expression separated by a colon. For instance, `lambda x: 2 * x` simply multiplies any input number by two, while `lambda x, y: x+y` simply calculates the sum of two numbers. The syntax is pretty straightforward, right?
With the assumption that you know what a lambda function is, this article is intended to provide some general guidelines on how to use lambda functions properly.


## Don’t Return Any Value

Looking at the syntax, you may notice that we don’t return anything for the lambda function. It’s all because lambda functions can only contain a single expression. However, the use of the return keyword will constitute a statement that is incompatible with the required syntax, as shown below:

```python
>>> integers = [(3, -3), (2, 3), (5, 1), (-4, 4)]
>>> sorted(integers, key=lambda x: x[-1])
[(3, -3), (5, 1), (2, 3), (-4, 4)]
>>> sorted(integers, key=lambda x: return x[-1])
... 
  File "<input>", line 1
    sorted(integers, key=lambda x: return x[-1])
                                   ^
SyntaxError: invalid syntax
```
This mistake probably arises due to the inability to differentiate expressions from statements. Statements like those involving `return`, `try`, `with`, and `if` perform particular actions. However, expressions are those that can be evaluated to a single value, such as a number or other Python objects.

With lambda functions, the single expression will evaluate a single value that is used subsequently, such as being sorted by the `sorted` function.


## Don’t Forget About Better Alternatives

One of the most common use cases is to set a lambda function to the key argument of some built-in utility functions, such as `sorted()` and `max()`, as shown above. Depending on the situation, we can use other alternatives. Consider the following examples:


```python
>>> integers = [-4, 3, 7, -5, -2, 6]
>>> sorted(integers, key=lambda x: abs(x))
[-2, 3, -4, -5, 6, 7]
>>> sorted(integers, key=abs)
[-2, 3, -4, -5, 6, 7]
>>> scores = [(93, 100), (92, 99), (95, 94)]
>>> max(scores, key=lambda x: x[0] + x[1])
(93, 100)
>>> max(scores, key=sum)
(93, 100)
```
In data science, many people use the pandas library to process data. We can use the lambda function to create new data from existing data using the map() function, as shown below. Instead of using a lambda function, we can simply use the arithmetic function directly because it’s supported in pandas:

```python
>>> import pandas as pd
>>> data = pd.Series([1, 2, 3, 4])
>>> data.map(lambda x: x + 5)
0    6
1    7
2    8
3    9
dtype: int64
>>> data + 5
0    6
1    7
2    8
3    9
dtype: int64
```

## Don’t Assign It to a Variable

I’ve seen some people mistakenly think that a lambda function is an alternative way to declare a simple function, and you may have seen people do the following:

```python

>>> doubler = lambda x: 2 * x
>>> doubler(5)
10
>>> doubler(7)
14
>>> type(doubler)
<class 'function'>
```

The only use of naming a lambda function is probably for teaching purposes to show that a lambda function is indeed a function just like other functions — to be called and having a type of function. Other than that, we shouldn’t assign a lambda function to a variable.

The problem with naming a lambda function is that it makes debugging less straightforward. Unlike other functions that are created using the regular def keyword, lambda functions don’t have names, which is why they’re sometimes referred to as anonymous functions. Consider the following trivial example to see this nuance:

```python

>>> inversive0 = lambda x: 1 / x
>>> inversive0(2)
0.5
>>> inversive0(0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 1, in <lambda>
ZeroDivisionError: division by zero
>>> def inversive1(x):
... 	return 1 / x
... 
>>> inversive1(2)
0.5
>>> inversive1(0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 2, in inversive1
ZeroDivisionError: division by zero
```
When your code has problems with a lambda function (i.e. inversive0), the Traceback error information can only tell you that a lambda function has bugs.

By contrast, with a regularly defined function, the Traceback will clearly inform you of the problematic function (i.e. inversive1).

Related to this, if you have the temptation to use a lambda function more than once, the best practice is to use a regular function using the def keyword, which will also allow you to have docstrings.


## Don’t Forget About List Comprehension

Some people like to use lambda functions with higher-order functions, such as `map` or `filter`. Consider the following example for this usage:

```python

>>> # Create a list of numbers
>>> numbers = [2, 1, 3, -3]
>>> # Use the map function with a lambda function
>>> list(map(lambda x: x * x, numbers))
[4, 1, 9, 9]
>>> # Use the filter function with a lambda function
>>> list(filter(lambda x: x % 2, numbers))
[1, 3, -3]
```
Instead of using the lambda function, we can use list comprehension, which has better readability. As shown below, we use list comprehension to create the same list objects. As you can see, the previous usage of `map` and `filter` functions with lambda functions is more cumbersome compared to list comprehension. So you should consider using list comprehension when you’re creating lists involving higher-order functions.

```python
[x*x for x in numbers]
[x for x in numbers if x%2]
```


[Source](https://medium.com/better-programming/master-python-lambda-functions-with-these-4-donts-655b212d36d7)