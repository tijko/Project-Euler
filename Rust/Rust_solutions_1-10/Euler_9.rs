// Find the only pythagorean triplet that a + b + c = 1000 

use std::time::Instant;


fn main() {
    let timer = Instant::now();
    let mut answer = 0;
    for x in 1..1000 as u64 {
        for y in x+1..1000 as u64 {
            let z = ((x*x + y*y) as f64).sqrt();
            if z != (z as u32) as f64 {
                continue;
            }
            if x + y + z as u64 == 1000 {
                answer = x * y * z as u64;
                break;
            }
            if answer != 0 {
                break;
            }
        }
    }

    println!("Answer: {}", answer);
    println!("Time: {:?}", timer.elapsed());
}
