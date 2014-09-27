#!/usr/bin/bash

# sum of even fibonacci numbers below 4 million

function fibonacci() {
    
    a1=1
    b1=1
    b2=0
    limit=4000000
    total=0

    while [[ "$b2" -le "$limit" ]]
        do
            let "b2 = $a1 + $b1"
            let "a1 = $b1"
            let "b1 = $b2"
            if [[ "$b2 % 2" -eq 0 ]]
            then
                let "total += $b2"
            fi
        done
    echo Answer: $total
}

fibonacci
time
                        
