module Main where

pretest_factor :: Int -> [Int] -> Int
pretest_factor n rng =
    if (n `mod` 7 == 0 || n `mod` 9 == 0 || n `mod` 3 == 0) &&
        range_factor n rng
    then 
        n 
    else
        pretest_factor (n+20) rng

range_factor :: Int -> [Int] -> Bool
range_factor n rng =
    if length rng == 0 then True
    else if mod n (rng!!0) /= 0 then False
    else range_factor n (tail rng)

main =
  do
    let rng = [6,8,11,12,13,14,15,16,17,18,19]
    let dividend = 20
    print(pretest_factor dividend rng)
