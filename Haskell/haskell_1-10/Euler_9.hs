module Main where

-- only pythagorean triplet that a + b + c == 1000
 
triplet :: [(Float, Float)] -> Float
triple [] = 0
triplet (pair:xs)
    | (fst pair) + (snd pair) + z == 1000 = (fst pair) * (snd pair) * z
    | otherwise = triplet xs
  where
    z = sqrt((fst pair)^2 + (snd pair)^2)
main =
    print(triplet [ (x, y) | x <- [1..1000], y <- [x+1..1000] ])
    
