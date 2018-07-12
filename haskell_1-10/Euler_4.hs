module Main where

is_palindrome :: Int -> Bool
is_palindrome n = reverse (show n) == show n
    
test :: [Int] -> [Int]
test n = drop 1 n

second :: [Int] -> [(Int, Int)]
second n = map (\x -> (n!!0, x)) test n

main = 
  do
    print(second [1..3])
