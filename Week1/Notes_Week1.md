# Notes for CS61A Week1

## Lecture 1

### Take away from slides

Operators and operands are also expressions. Based on the defintion given in the lecture, ``expressions in programs evaluate to values``. In any programming language, is ``anything can be evaluated to values`` an expression?


The evaluation of an expression can be summarized into the following steps:
* evaluate the operator
* evalute the operand(s)
* apply operand(s) to operator


NOTE: The detailed parsing process of expressions or the operators and operands is more related to compiler or interpretor (for scripting language like Python)

Nested call expressions ``add(add(6, mul(4, 6)), mul(3, 5))``. What is the order for Python to evaluate this expression? Actually, there is nothing special. Based on the above steps, recursively applying the rule can lead to the final result.
* operator add, operand 1 add(6, mul(4, 6)), operand 2 mul(3, 5)
* (order of evaluating two operands?) operator add, operand 1 6, operand 2 mul(4, 6)
* ...


## Take away from codes
Nothing special...




## Lecture 2
### Take away from slides

Dicussion Question 1:
```python
f = min
f = max
g, h = min, max
max = g
max(f(2, g(h(1, 5), 3)), 4)
```

Solution:
* Most popular implementation of Python language specifications is CPython
* ``f = min``, ``min`` is a function. ``f`` should be understood as a **Name**, which is bound to the function.
* Answer should be ``3``: ``f`` is the bound name to the ``max`` function, ``g`` is the name bound to the ``min`` function, ``h`` is the name bound to the ``max`` function, ``max`` is the name bound to the ``min`` function. ``f = max`` is not affected, as ``f`` is bound to the function of ``max`` but not of the name ``max``. 
* Anything appearing on the left side of ``=`` is a **Name**, which is bound to the right operand.


  <img src="solution_q1.png" alt="drawing" width="500"/>

Further reading:  [Understanding the concept of variables in Python](https://realpython.com/python-variables/)

<!-- Of course you can also understand it as a reference or pointer associated with the right operand, but I personally prefer to understand it as the Name -->



Calling User-defined Functions

* function name is globally visible
* Add a local frame, forming a new environment
* Bind the function's formal parameters to its arguments in that frame
* Execute the body of the function in that new environment
* Return an expression



Looking Up Names in Environments

* Every expression is evaluated in the context of an environment
* An environment is a sequence of frames
* A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.


## Take away from Codes
* ``Operator`` library: https://docs.python.org/3/library/operator.html
