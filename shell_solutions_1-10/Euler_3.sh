#!/usr/bin/env bash

# what is the largest prime factor of 600851475143


function is_prime() 
{
    n=$1
    if [[ "$n" -eq 2 || "$n" -eq 3 ]]; then
        echo 1 
    elif [[ "$n" -lt 2 || "$n % 2" -eq 0 ]]; then
        echo 0
    else
        nroot=$(echo "sqrt($n)" | bc)
        ((nroot++))
        for (( i=3; i<=nroot; i+=2 )); do
            if [[ "$n % $i" -eq 0 ]]; then
                echo 0; return
            fi
        done; echo 1
    fi
    return
}

function large_prime_factor() 
{
    high=0
    factor_of=$(echo 'sqrt(600851475143)' | bc)

    for (( i=$factor_of; i>0; i-- )); do
        if [[ "600851475143 % $i" -eq 0 && 
              $(is_prime $i) -eq 1 &&
              "$i" -gt "$high" ]]; then
            high=$i
        fi
    done
    echo $high         
}

echo Answer: $(large_prime_factor)
