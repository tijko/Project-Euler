// Find the sum of all the primes below two million. 

use std::time::Instant;


fn is_prime(n:u64) -> bool {
    if n == 2 {
        return true;
    }

    if n < 2 || n % 2 == 0 {
        return false;
    }

    let range:u64 = (n as f64).sqrt() as u64;
    for i in 3..range+1 {
        if n % i == 0 {
            return false;
        }
    }

    return true;
}

fn main() {
    let timer = Instant::now();
    let mut total:u64 = 0;
    let mut current:u64 = 0;
    let answer = loop {
        if current == 2000000 {
            break total;
        }

        current += 1;
        if is_prime(current) {
            total += current;
        }
    };

    println!("Answer: {}", answer);
    println!("Time:  {:?}", timer.elapsed());
}
