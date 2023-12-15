use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();

    let mut cnts = [0; 9];

    for num in buf.trim().chars() {
        cnts[if num == '9' {
            6
        } else {
            num.to_digit(10).unwrap() as usize
        }] += 1;
    }
    cnts[6] = (cnts[6] + 1) >> 1;

    let ans = *cnts.iter().max().unwrap();
    println!("{ans}");
}
