module Main where

fib :: Int -> Int -> Int -> Int
fib n1 n2 total
    | n1 > 4000000      = total
    | n1 `mod` 2 == 0   = fib n2 (n2 + n1) total
    | otherwise         = fib n2 (n2 + n1) (total + n1)

main =
    print(fib 0 1 0)

