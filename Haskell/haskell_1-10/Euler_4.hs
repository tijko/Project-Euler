-- Find the highest palindrome from the product of 2 3-digit integers

module Main where
import System.Clock
import Text.Printf


is_palindrome :: Int -> Bool
is_palindrome n = reverse (show n) == show n

max_product_palindrome :: [(Int, Int)] -> Int -> Int
max_product_palindrome [] high = high
max_product_palindrome (x:xs) high
    | is_palindrome canidate &&
      canidate > high           = max_product_palindrome xs canidate
    | otherwise                 = max_product_palindrome xs high
  where
      canidate = fst x * snd x


getTotalTime :: TimeSpec -> Float
getTotalTime t = fromIntegral (sec t) + (fromIntegral(nsec t) / 10^9)

main :: IO ()
main =
  do
    start <- getTime Monotonic
    printf "Answer:    %d\n" (max_product_palindrome [(x, y) | x <- [100..999], y <- [x..999]] 0)
    stop <- getTime Monotonic
    printf "Time:    %.6f\n" (getTotalTime(stop) - getTotalTime(start))
