;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car(cdr (cdr s)))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
  ((< x 0) -1)
  ((> x 0) 1)
  (else 0)
  )
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
  ((= n 0) 1)
   ((even? n) (square (pow b (/ n 2))))
   ((odd? n) (* b (square (pow b (/ (- n 1) 2)))))

))

(define (unique s)
  'YOUR-CODE-HERE
  (cond
  ((null? s) nil)
  (else (cons (car s) (filter (lambda(x) (not (eq? x (car s)))) (unique (cdr s))))
  ))
  
)