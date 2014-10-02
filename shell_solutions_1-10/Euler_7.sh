#!/usr/bin/env bash

# The 10001st prime number is?


function is_prime()
{
    nroot=$(echo "sqrt($1)" | bc)
    ((nroot++))
    for (( i=3; i<nroot; i++ )); do
        if [[ "$1 % $i" -eq 0 ]]; then
            echo 0; return
        fi
    done
    echo 1; return
}

function prime_counter()
{
    nth=$1
    for ((cnt=1, curr=3; cnt<$nth; curr+=2)); do
        if [[ $(echo $(is_prime $curr)) -eq 1 ]]; then
            ((cnt++))
        fi
    done
    echo $(($curr-2))
}

prime_counter 10001
