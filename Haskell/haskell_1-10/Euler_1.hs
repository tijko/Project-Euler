-- Find sum of all multiples of 3 and 5 under 1000

module Main where
import Text.Printf
import System.Clock

five_or_three :: Int -> Int
five_or_three n 
    | n `mod` 5 == 0 = n
    | n `mod` 3 == 0 = n
    | otherwise      = 0

getTotalTime :: TimeSpec -> Float
getTotalTime t = fromIntegral (sec t) + (fromIntegral(nsec t) / 10^9)

main :: IO ()
main = 
  do 
    start <- getTime Monotonic
    printf "Answer: %d\n" (sum (map five_or_three [1..999]))
    stop <- getTime Monotonic
    printf "Time:   %.6f\n" (getTotalTime(stop) - getTotalTime(start))
