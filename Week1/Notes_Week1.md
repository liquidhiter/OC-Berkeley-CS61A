# Notes for CS61A Week1

## Take away from slides

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
