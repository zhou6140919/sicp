#lang slideshow
;; version 1
(define (fib1 x)
  (if (< x 2)
      x
      (+ (fib1 (- x 1)) (fib1 (- x 2)))))

;; version 2
(define (fib2 n)
  (define calc-fib
    (lambda (n a b)
      (if (= n 0)
          a
          (calc-fib (- n 1) b (+ a b)))))
  (calc-fib n 0 1))
    
    