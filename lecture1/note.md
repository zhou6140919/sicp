# Lecture 1a

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

```python
# 9227465 2.84971022605896
# 9227465 2.3126602172851562e-05
```

## Difference between Iteration and Recursion

An iteration is a system that has all of its state in explicit variables.


















