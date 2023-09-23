module Main where

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


main = 
  do
    print(max_product_palindrome [(x, y) | x <- [100..999], y <- [x..999]] 0)
