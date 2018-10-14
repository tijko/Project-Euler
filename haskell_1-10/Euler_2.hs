module Main where

fibonacci :: Int -> Int -> Int -> Int -> Int
fibonacci n1 n2 total limit  
    | n1 > limit        = total
    | n1 `mod` 2 == 0   = fibonacci n2 (n2 + n1) total limit
    | otherwise         = fibonacci n2 (n2 + n1) (total + n1) limit

main =
    print(fibonacci 0 1 0 4000000)

