#!/usr/bin/bash

# sum of all multiples of 3 and 5 below 1000

function three_and_five() {

    let total=0

    for i in {1..999}
        do 
            if [[ "$i % 3" -eq 0 || "$i % 5" -eq 0 ]]
            then
                let "total += $i"
            fi
        done
    echo Answer: $total
}

three_and_five
time
