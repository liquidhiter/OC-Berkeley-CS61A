from functools import total_ordering
from operator import add, mul, sub
from tempfile import tempdir
from typing import Container


def square(x): return x * x


def identity(x): return x


def triple(x): return 3 * x


def increment(x): return x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    term -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    total, k = 1, 1
    while k <= n:
        total, k = total * term(k), k + 1
    return total


def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, term(k)), k + 1

    return total


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul, 1, n, term)


def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    # Basic Solution (un-comment the following lines)
    # def repeater(x):
    #     k = 1
    #     while k <= n:
    #         x, k = func(x), k + 1
    #     return x
    # return repeater

    # Extra Challenge
    return accumulate(compose1, lambda x: x, n, lambda y: func)


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    return lambda x: f(x)


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    return lambda x: f(f(x))


three = successor(two)


def f(x):
    """Helper function used to express the logic"""
    return x**2


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    # Basic solution...
    # base = zero
    # convToInt = 0
    # while base(f)(2) != n(f)(2):  # Any number > 1
    #     base = successor(base)
    #     convToInt += 1

    # return convToInt
    
    return n(lambda x: x+1)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    # Express m + n into successor function
    res = zero
    while res(f)(2) != m(f)(2):
        res = successor(res)

    base = zero
    while base(f)(2) != n(f)(2):
        res = successor(res)
        base = successor(base)

    return res

    # The following solution is only used to test...
    # total_conv_to_int = church_to_int(m) + church_to_int(n)
    # res = zero
    # for i in range(0, total_conv_to_int):
    #     res = successor(res)

    # return res


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    # Simulate the multiplication with two loops...
    baseOuter = base = zero
    while baseOuter(f)(2) != m(f)(2):
        baseOuter = successor(baseOuter)
        baseInner = zero
        while baseInner(f)(2) != n(f)(2):
            baseInner = successor(baseInner)
            base = successor(base)

    return base


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    # I have not found a simple solution to simulate the power...
    # In this case, I have to use the church_to_int
    res = one
    n_conv_to_int = church_to_int(n)
    for i in range(n_conv_to_int):
        res = mul_church(res, m)

    return res
