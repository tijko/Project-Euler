// Find the difference between the sum of the squares of the first one hundred
// natural numbers and the square of the sum? 

use std::time::Instant;

fn sum_of_sqs() -> u64 {
    let svec:Vec<u64> = (1..101).collect();
    let sum_sq:u64 = svec.into_iter().map(|x| x * x).sum();
    return sum_sq;
}

fn sq_of_sum() -> u64 {
    let svec:Vec<u64> = (1..101).collect();
    let sq_sum:u64 = svec.into_iter().sum();
    return sq_sum * sq_sum;
}

fn main() {
    let timer = Instant::now();
    let sq_sum:u64 = sq_of_sum();
    let sum_sqs:u64 = sum_of_sqs();
    let answer = sq_sum - sum_sqs;
    println!("Answer: {}", answer);
    println!("Time:  {:?}", timer.elapsed());
}
