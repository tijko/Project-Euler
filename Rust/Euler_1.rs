// sum of all multiples of 3 and 5 below 1000?

use std::time::Instant;


fn main() {

    let timer = Instant::now();
    let mut val = 0; 

    for n in 1..1000 {

        if n % 3 == 0 || n % 5 == 0 {
            val = val + n;
        }
    }

    println!("Answer: {}", val);
    println!("Time:   {:?}", timer.elapsed());
}
