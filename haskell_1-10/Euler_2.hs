module Main where

fibonacci :: Int -> Int -> Int -> Int -> Int
fibonacci n1 n2 total limit = 
    if n1 > limit 
    then 
        total
    else
        if mod n1 2 == 0
        then
            fibonacci n2 (n2 + n1) total limit
        else
            fibonacci n2 (n2 + n1) (total + n1) limit
main =
    print(fibonacci 0 1 0 4000000)

