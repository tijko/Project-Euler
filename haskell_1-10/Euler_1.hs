module Main where

five_or_three :: Int -> Int
five_or_three n 
    | n `mod` 5 == 0 || mod n 3 == 0 = n
    | otherwise                      = 0

main = print(sum (map five_or_three [1..999]))

                    
