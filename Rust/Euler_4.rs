// Find the largest palindrome number made from the product of two 3-digit 
// numbers?

// Create a generator function - i.e. see what Rust offers
// Does Rust have functional form?

use std::time::Instant;


fn main() {
    let timer = Instant::now();

    let mut answer:u32 = 0;
    for i in 100..999 {
        for j in i..999 {
            let current = i * j;
            let canidate:String = current.to_string();
            let reverse:String = canidate.chars().rev().collect();
            if reverse == canidate && current > answer {
                answer = current;
            }
        }
    }
    println!("Answer: {}", answer);
    println!("Time:   {:?}", timer.elapsed());
}
