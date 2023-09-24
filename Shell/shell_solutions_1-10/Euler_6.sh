#!/usr/bin/env bash

# Find the difference between the sum of the squares of the first one-hundred 
# natural numbers and the square of the sum?


function squared_hundred()
{
    sum_all_squares=0
    square_sum=0
    for i in {1..100}; do
        (( square_sum+=$i ))
        (( sum_all_squares+=$i**2 ))
    done
    echo $(( $((square_sum**2)) - $sum_all_squares ))
}

squared_hundred
