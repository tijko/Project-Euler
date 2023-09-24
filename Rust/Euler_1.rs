use ::std::time::Instant;


fn main() {

    let start = Instant::now();
    let mut val = 0; 

    for n in 1..1000 {

        if n % 3 == 0 || n % 5 == 0 {
            val = val + n;
        }
    }

    let stop = Instant::now();
    println!("Answer: {}", val);
    println!("Time:   {:#?}", stop - start);

}
