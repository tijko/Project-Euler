module Main where

sq_sum :: Int -> Int -> Int
sq_sum n total 
    | n > 100 = total
    | otherwise = sq_sum (n+1) (total+n^2)

main = 
  do
    let exp_sum = (sum [1..100])^2
    let squares_sum = sq_sum 1 0
    print (exp_sum - squares_sum)
