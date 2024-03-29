-- Find the largest prime factor
module Main where
import Text.Printf
import System.Clock


is_factor :: Int -> [Int] -> Bool
is_factor _ [] = True
is_factor x y
    | x `mod` (y!!0) == 0 = False
    | otherwise           = is_factor x (tail y)


prime_factor :: Int -> [Int] -> Int
prime_factor _ [] = -1
prime_factor n f 
    | n `mod` (f!!0) == 0 && 
      is_prime (f!!0)        = f!!0
    | otherwise              = prime_factor n (tail f)

is_prime :: Int -> Bool
is_prime 2 = True
is_prime 3 = True
is_prime n  
    | n < 2          = False
    | n `mod` 2 == 0 = False
    | otherwise = is_factor n divs
  where
    s = ceiling ( sqrt(fromIntegral n) ) + 1
    divs = [3..s]

getTotalTime :: TimeSpec -> Float
getTotalTime t = fromIntegral (sec t) + (fromIntegral(nsec t) / 10^9)

main :: IO ()
main =
  do
    start <- getTime Monotonic
    let target = 600851475143
    let x = round(sqrt(fromIntegral target))
    let lst = reverse [ 2..x ]
    printf "Answer:  %d\n" ( prime_factor target lst )
    stop <- getTime Monotonic
    printf "Time:    %.6f\n" (getTotalTime(stop) - getTotalTime(start))
