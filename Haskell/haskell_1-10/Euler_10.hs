module Main where

prime :: Int -> Bool
prime 2 = True
prime 3 = True
prime n
    | n < 2 || n `mod` 2 == 0 = False
    | otherwise = z
  where
    z = foldl (&&) True [ n `mod` i /= 0 | i <- [3..round(sqrt(fromIntegral n))+1] ]

main =
  print(sum(filter prime [1..2000000]))
