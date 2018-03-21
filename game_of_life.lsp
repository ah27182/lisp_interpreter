( batch 
(
    define x '((0 0 0 0) (0 0 0 0) (0 0 0 0) (0 0 0 0))
)

(
    define length 3
)

(
    define num_live_neighbors (
        lambda (x i j) (
            cond
            (
                (eq? i j 0)
                (
                    + 
                    (index (index x 1) 0)
                    (index (index x 0) 1) 
                    (index (index x 1) 1)
                )
            )

            (
                (and (eq? i length) (eq? j 0))
                (
                    + 
                    (index (index x (- length 1)) 0) 
                    (index (index x (- length 1) ) 1)
                    (index (index x length) 1)
                )
            )

            (
                (and (eq? i 0) (eq? j length))
                (
                    + 
                    (index (index x 0 ) (- length 1)) 
                    (index (index x 1) (- length 1)) 
                    (index (index x 1) length)
                )
            )

            (
                (and (eq? i length) (eq? j length))
                (
                    + 
                    (index (index x length) (- length 1)) 
                    (index (index x (- length 1)) (- length 1)) 
                    (index (index x (- length 1)) length)
                )
            )

            (
                (eq? i 0)
                (
                    +
                    (index (index x i) (- j 1))
                    (index (index x (+ i 1)) (- j 1))
                    (index (index x (+ i 1)) j)
                    (index (index x (+ i 1)) (+ j 1))
                    (index (index x i) (+ j 1))
                )
            )

            (
                (eq? j 0)
                (
                    +
                    (index (index x (- i 1)) j)
                    (index (index x (- i 1)) (+ j 1))
                    (index (index x i) (+ j 1))
                    (index (index x (+ i 1)) (+ j 1))
                    (index (index x (+ i 1)) j)
                )
            )

            (
                (eq? i length)
                (
                    +
                    (index (index x i) (- j 1))
                    (index (index x (- i 1)) (- j 1))
                    (index (index x (- i 1)) j)
                    (index (index x (- i 1)) (+ j 1))
                    (index (index x i) (+ j 1))
                )
            )

            (
                (eq? j length)
                (
                    +
                    (index (index x (- i 1)) j)
                    (index (index x (- i 1)) (- j 1))
                    (index (index x i) (- j 1))
                    (index (index x (+ i 1)) (- j 1))
                    (index (index x (+ i 1)) j)
                )
            )

            (
                else 
                (
                    + 
                    (index (index x (- i 1)) (- j 1))
                    (index (index x (- i 1)) j)
                    (index (index x (- i 1)) (+ j 1))
                    (index (index x i) (- j 1))
                    (index (index x i) (+ j 1))
                    (index (index x (+ i 1)) (- j 1))
                    (index (index x (+ i 1)) j)
                    (index (index x (+ i 1)) (+ j 1))
                )
            )
        )
    )
)

(
    define rules_on_cell (
        lambda (x i j n) (
            cond 
            (
                (or (< n 2) (> n 3))
                
                (
                    set x i (set (index x i) j 0)
                    )
            )

            (
                else
                (set x i (set (index x i) j 1))
            )
        )
    )
)

(
    define game_of_life (
        lambda (x k) (
            cond
            (
                (> k (- (* (+ length 1) (+ length 1) ) 1)) 
                x
            )

            (
                else
                
                (game_of_life (
                    rules_on_cell 
                    x 
                    (floordiv k (+ length 1) ) 
                    (mod k (+ length 1) ) 
                    (num_live_neighbors 
                        x 
                        (floordiv k (+ 1 length)) 
                        (mod k (+ 1 length))
                    )
                ) 
                    (+ k 1)
                )
            )
        )
    )
)

)


