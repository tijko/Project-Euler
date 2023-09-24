#!/usr/bin/env bash

# Find the only pythagorean triplet that a + b + c = 1000

function triplet_thousand()
{
    for ((a=1, b=1; a < 3000; a++)); do
        ((b=$a+1))
        for ((; b < 3000; b++)); do
            ((c=a**2+b**2))
            c=$(echo "scale=3;sqrt($c)" | bc)
            triplet=$(echo "scale=3;$a+$b+$c" | bc)
            if [[ $(echo "$triplet == 1000" | bc) -eq 1 ]]; then
                echo "scale=0;$a*$b*$c" | bc; return
            fi
            if [[ $(echo "$triplet > 1000" | bc) -eq 1 ]]; then
                break
            fi
        done
    done
}

triplet_thousand
