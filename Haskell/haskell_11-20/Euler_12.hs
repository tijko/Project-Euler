-- First triangle number with +500 divisors

module Main where
import Text.Printf
import System.Clock


isDivisible :: Int -> Int -> Bool
isDivisble _ 0  = False
isDivisible x y = x `mod` y == 0

range :: Int -> Int
range n = (ceiling $ sqrt $ fromIntegral n) + 1

-- keep track of the "range n" passing in an extra [Int] parameter
divisors :: Int -> Int
divisors n = sum [ 1 | x <- [2..range n], isDivisible n x] * 2

triangle :: Int -> Int -> Int -> Int
triangle n c lim
    | divs > lim = n
    | otherwise  = triangle (n + c) (c + 1) lim
  where
    divs = divisors n

getTotalTime :: TimeSpec -> Float
getTotalTime t = fromIntegral (sec t) + (fromIntegral(nsec t) / 10^9)

main = 
  do
    start <- getTime Monotonic
    printf "Answer: %d\n" (triangle 3 3 500)
    stop <- getTime Monotonic
    printf "Time:   %.4f\n" (getTotalTime(stop) - getTotalTime(start))
