// Find the only pythagorean triplet that a + b + c = 1000 

use std::time::Instant;


fn main() {
    let timer = Instant::now();
    let mut answer = 0;

    for x in 1..1000 as u64 {
        for y in x+1..1000 as u64 {
            let tmp = (x*x + y*y) as f64;
            let zi = tmp.sqrt();
            let z = zi as u64;
            if z == zi && x + y + z == 1000 {
                println!("{} + {} + {}", x, y, z);
                answer = x * y * z;
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
