use ::std::time::Instant;


fn main() {

    let start = Instant::now();
    let mut total = 0;

    let mut x = 0;
    let mut y = 1;
    let mut tmp = y;

    while y <= 4000000 {
        tmp = x;
        x = y;
        y = tmp + x;
        if y % 2 == 0 {
            total = total + y;
        }
    }
    let stop = Instant::now();

    println!("Answer: {}", total);
    println!("Time:   {:#?}", stop - start);
}
