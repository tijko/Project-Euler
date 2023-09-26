// what is the largest prime factor of 600851475143 ? 

use std::time::Instant;

fn is_prime(n:u64) -> bool {
    if n == 2 {
        return true;
    }

    if n < 2 || n % 2 == 0 {
        return false;
    }

    let range:u64 = n.sqrt() + 1;

    for i in 3..range {
        if n % i == 0 {
            return false;
        }
    }

    return true;
}

fn main() {
    let timer = Instant::now();

    let factor:u64 = 600851475143;
    let current:u64 = factor / 2;

    let answer = {
        while true {
            if factor % current == 0 && is_prime(current) {
                break current;
            }

            current -= 1;
        };
    };

    println!("Answer: {}", answer);
    println!("Time: {:?}", timer.elapsed());
}
