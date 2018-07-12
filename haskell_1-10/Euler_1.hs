module Main where

five_or_three :: Int -> Int

five_or_three n = if mod n 5 == 0 || mod n 3 == 0 then n else 0

main = print(sum (map five_or_three [1..1000]))

                    
