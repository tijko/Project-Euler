module Main where


is_factor :: Int -> [Int] -> Bool
is_factor x y = 
    if length y == 0 then True
    else if mod x (y!!0) == 0 then False
    else is_factor x (tail y)

prime_factor :: Int -> [Int] -> Int
prime_factor n f =
  do
    if length f == 0 then -1
    else if
      mod n (f!!0) == 0 && is_prime (f!!0)
    then
      f!!0
    else
      prime_factor n (tail f)

is_prime :: Int -> Bool
is_prime n = 
  do
    let s = ceiling ( sqrt(fromIntegral n) ) + 1
    let divs = [3..s]
    if n == 2 || n == 3 then True
    else if n < 2 || mod n 2 == 0 then False
    else is_factor n divs    

main =
  do
    let target = 600851475143
    let x = round(sqrt(fromIntegral target))
    let lst = reverse [ 2..x ]
    print( prime_factor target lst )
