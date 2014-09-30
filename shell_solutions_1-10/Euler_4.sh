#!/usr/bin/env bash

# Find the largest palindrome number made from the product of two 3-digit numbers

function three_digit_palindrome() {

    for x in {100..1000}; do
        for y in {100..1000}; do
            let "forward =  $x * $y"
            for ((i=0, j=${#forward}-1; i<${#forward}; i++, j--)); do
                if [[ ${forward:i:1} -ne ${forward:j:1} ]]; then
                    break
                fi
            if [[ $forward -gt $high && $i -eq ${#forward}-1 ]]; then
                let "high = $forward"
            fi
            done
        done
    done
    echo $high
}

three_digit_palindrome
