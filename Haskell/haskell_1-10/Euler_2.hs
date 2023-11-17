-- Total of all even fibonacci numbers below 4 million
module Main where
import Text.Printf
import System.Clock


fib :: Int -> Int -> Int -> Int
fib n1 n2 total
    | n1 > 4000000      = total
    | n1 `mod` 2 == 0   = fib n2 (n2 + n1) total
    | otherwise         = fib n2 (n2 + n1) (total + n1)

getTotalTime :: TimeSpec -> Float
getTotalTime t = fromIntegral (sec t) + (fromIntegral(nsec t) / 10^9)

main :: IO ()
main =
  do
    start <- getTime Monotonic
    printf "Answer:  %d\n" (fib 0 1 0)
    stop <- getTime Monotonic
    printf "Time:    %.6f\n" (getTotalTime(stop) - getTotalTime(start))
