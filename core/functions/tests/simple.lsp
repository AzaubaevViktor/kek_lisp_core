(defn my_func (a b c)
    (= x (+ a b))
    (= y (+ x c))
    y
)

(assert (== (my_func 1 2 3) 6))
