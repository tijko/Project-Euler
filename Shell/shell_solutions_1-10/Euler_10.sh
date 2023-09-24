#!/usr/bin/env bash

# Find the sum of all the primes below two million.


function is_prime()
{
    n=$1
    if [[ "$n" -eq 2 ]]; then
        echo 1
    elif [[ "$n" -lt 2 || $(($n % 2)) -eq "0" ]]; then
        echo 0
    else
        nroot=$(echo "sqrt($n)" | bc)
        ((nroot++))
        for (( i=3; i<=nroot; i+=2 )); do
            if [[ $(($n % $i)) -eq "0" ]]; then
                echo 0; return
            fi
        done; echo 1
    fi
    return
}

function primes_to()
{
    prime_limit=$1
    prime_sum=0
    for (( i=0; i<$prime_limit; i++ )); do
        if [[ $(is_prime $i) -eq 1 ]]; then
            ((prime_sum+=$i))
        fi
    done 
    echo $prime_sum
}

primes_to 2000000
