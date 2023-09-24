#!/usr/bin/env bash

# What is the smallest number that can be divided evenly by every number 1-20?


function factor()
{
    for i in {1..20}; do
        if [[ "$1 % $i" -ne 0 ]]; then
            echo 0; return
        fi
    done
    echo 1; return
}

#XXX extremely slow
function range_divisible_by_twenty()
{
    curr=20
    while [ 1 ]; do
        if [[ "$curr % 7" -eq 0 ]]; then
            ret=$(echo $(factor $curr))        
            if [[ "$ret" -eq 1 ]]; then
                break
            fi
            ((curr+=20))
        else
            ((curr+=20*(( $curr % 7 )))) # slight gain...
        fi
    done
    echo ${curr}
}

range_divisible_by_twenty
