# Lecture 2a - Higher-order Procedures

**One of the things you can do in this language that we're showing you is not only do you know something like that, but you give the knowledge of that a name.**

**授人以鱼不如授人以渔.**

## Prologue

```lisp
;; add numbers
(define (sum-int a b)
    (if (> a b)
        0
	(+ a (sum-int (+ a 1) b))))
```

## The Pattern

```lisp

(define (sum TERM A NEXT B)
    (if (> A B)
        0
	(+ (TERM A)
	    (sum TERM (NEXT A) NEXT B))))
```

## Heron Method


```lisp
(define (sqrt x)
    (define tolerance 0.00001)
    (define (good-enuf? y)
        (< (abs (- (* y y) x)) tolerance))
    (define (improve y)
        (average (/ x y) y))
    (define (try y)
        (if (good-enof? y)
	    y
	    (try (improve y))))
    (try 1))
```


Look for a fixed-point of the function

```lisp
(define (fixed-point f start)
    (define tolerance 0.00001)
    (define (close-enuf? u v)
        (< (abs (- v u)) tolerance))
    (define (iter old new)
        (if (close-enuf? old new)
	    new
	    (iter new (f new))))
    (iter start (f start)))
```

## Newton's Method

To find a y such that f(y) = 0

y_{n+1} = y_n - f(y_n)/f'(y_n)

```lisp

(define (sqrt x)
    (newton (lambda (y) (- (square y) x)), 1.0))
(define (newton f guess))
    (define df (Derivative f))
    (fixed-point (lambda (x) (/ (f x) (df x))) guess)
(define Derivative 
    (lambda (f)
        (lambda (x)
	    (/ (- (f (+ x dx))
	          (f x))
	       dx))))
(define dx 0.000001)
```

```






