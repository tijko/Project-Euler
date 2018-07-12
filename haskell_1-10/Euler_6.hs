module Main where

sq_sum :: Int -> Int -> Int
sq_sum n total =
    if n > 100 then total
    else sq_sum (n+1) (total+n^2)

main = 
    print((sum [1..100])^2 - sq_sum 1 0)
