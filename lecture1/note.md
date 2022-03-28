# Lecture 1a

Recommend book: [Purely Functional Data Structures](https://doc.lagout.org/programmation/Functional%20Programming/Chris_Okasaki-Purely_Functional_Data_Structures-Cambridge_University_Press%281998%29.pdf)

## Lisp Abstract

```lisp
# How to define a function
(define (square x)
	(* x x))
# This is same as the above
(define square
	(lambda (x)
		(* x x)))
# IF statement
(define (iszero x)
	(if (= x 0)
            1
	    0))
```
**Homework**
1. Write a function that returns the square root of a number.
2. Write a number that returns the n^th fibonacci number.

# Lecture 1b

## Calculation Process

```lisp
(define (+ x y)
	(if (= x 0)
	    y
            (+ (-1+ x) (1+ y))))
# (+ 3 4)
# (+ 2 5)
# (+ 1 6)
# (+ 0 7)
# 7
```
$$ time = O(n) $$
$$ space = O(1) $$

We call this **Iteration**.

```lisp
(define (+ x y)
	(if (= x 0)
	    y
	    (1+ (+ (-1+ x) y))))
# (+ 3 4)
# (1+ (+ 2 4))
# (1+ (1+ (+ 1 4)))
# (1+ (1+ (1+ (+ 0 4))))
# (1+ (1+ (1+ 4)))
# (1+ (1+ 5))
# (1+ 6)
# 7
# cannot do them immediately
```
$$ time = O(n) $$
$$ space = O(x) $$

We call this **Recursion**.

In python I tried to produce fibonacci 35th number.
By the first process, it took about 3 seconds. But it took about 2.3*10^-5 seconds by the second process.
The python script is in the same folder. Try it yourself, but I don't recommend you to produce more than 35th number.

```python
# 9227465 2.84971022605896
# 9227465 2.3126602172851562e-05
```

## Difference between Iteration and Recursion

An iteration is a system that has all of its state in explicit variables.

An recursion cannot continue if it has lost part of its state.

## Fibonacci

```bash
fib(4)
├── fib(3)
│   ├── fib(1)
│   └── fib(2)
│	├── fib(1)
│	│   └── 1
│	└── fib(0)
│	    └── 0
└── fib(2)
    ├── fib(1)
    │   └── 1
    └── fib(2)
        └── 0
```
Need to add an existing result which has to be compute again to produce the answer.

$$ time = O(fib(n)) $$
$$ space = O(n) $$

## Tower of Hanoi

```lisp

```















