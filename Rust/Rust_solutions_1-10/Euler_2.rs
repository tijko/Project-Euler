// sum of even fibonacci numbers below 4 million? 

use std::time::Instant;


fn main() {

    let timer:Instant = Instant::now();
    
    let mut total:i64 = 0;
    let (mut a, mut b) = (0, 1);

    let answer = loop {

        if b > 4000000 {
            break total;
        };

        if b % 2 == 0 {
            total += b;
        };

        let c = a + b;
        a = b;
        b = c;
    };

    println!("Answer: {}", answer);
    println!("Time:   {:?}", timer.elapsed());
}
