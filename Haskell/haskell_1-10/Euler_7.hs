-- 10001th prime number

module Main where

is_prime :: Int -> Bool
is_prime 2 = True
is_prime n 
    | n `mod` 2 == 0 = False
    | n < 2 = False
    | otherwise = has_factor n [3..limit]
  where
    limit = ceiling( sqrt(fromIntegral n) )

has_factor :: Int -> [Int] -> Bool
has_factor _ [] = True
has_factor n rng 
    | n `mod` item == 0 = False
    | otherwise = has_factor n (tail rng)
  where
    item = (rng!!0)

prime_limit :: Int -> Int -> Int -> Int
prime_limit x y z 
    | x == y = z
    | is_prime z = prime_limit x (y + 1) (z + 1)
    | otherwise = prime_limit x y (z + 1)

main = 
  do
    print((prime_limit 10001 0 1) - 1)
