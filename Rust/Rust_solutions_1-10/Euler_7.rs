// What is the 10001st prime number?

use std::time::Instant;

fn is_prime(n:u64) -> bool {
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
    let mut count:u64 = 1;
    let mut current:u64 = 2;

    let answer = loop {
        if count == 10001 {
            break current;
        }

        current += 1;
        if is_prime(current) {
            count += 1;
        }
    };

    println!("Answer: {}", answer);
    println!("Time:  {:?}", timer.elapsed());
}
