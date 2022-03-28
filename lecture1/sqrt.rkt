#lang slideshow

(define avg
  (lambda (x y)
    (/ (+ x y) 2)))
(define square
  (lambda (x)
    (* x x)))
(define (abs1 x)
  (cond [(< x 0) (- 0 x)]
        [(= x 0) 0]
        [(> x 0) x]))
(define (abs2 x)
  (if (< x 0)
      (- x)
      x))

(define (sqrt x)
  (define (try guess)
    (if (< (abs2 (- (square guess) x)) 0.001) guess (try (avg guess (/ x guess)))))
  (try 1))