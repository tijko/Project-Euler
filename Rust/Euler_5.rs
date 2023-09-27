// What is the smallest number that can be divided evenly by all the numbers 
// from 1-20?  

use std::time::Instant;


fn main() {
    let timer = Instant::now();

    let multiples:[u64;11] = [19, 18, 17, 16, 15, 14, 13, 12, 11, 8, 6];
    let mut current:u64 = 20 * 19;
    let mut idx = 0;

    let answer = loop {
        while idx < multiples.len() {
            if current % multiples[idx] != 0 {
                break;
            }
            
            idx += 1;
        }

        if idx == multiples.len() && current % 19 == 0 {
            break current;
        } else {
            idx = 0;
            current += 20;
        }
    };

    println!("Answer: {}", answer);
    println!("Time:   {:?}", timer.elapsed());
}
