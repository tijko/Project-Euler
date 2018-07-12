-- 10001th prime number

module Main where

is_prime :: Int -> Bool
is_prime n =
  do
    let limit = ceiling( sqrt(fromIntegral n) )
    if n == 2 then True
    else if mod n 2 == 0 || n < 2 then False
    else
      has_factor n [3..limit]

has_factor :: Int -> [Int] -> Bool
has_factor n rng =
    if length rng == 0 then True
    else if n `mod` (rng!!0) == 0 then False
    else has_factor n (tail rng)

prime_limit :: Int -> Int -> Int -> Int
prime_limit x y z =
    if x == y then z
    else if is_prime z then prime_limit x (y + 1) (z + 1)
    else prime_limit x y (z + 1)

main = 
  do
    print((prime_limit 10001 0 1) - 1)
