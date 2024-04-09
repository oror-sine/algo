use std::io::{stdin, Read};

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();

    let mut input = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());

    let mut x = input.next().unwrap();
    let n = input.next().unwrap();

    for _ in 0..n {
        x -= input.next().unwrap() * input.next().unwrap();
    }

    print!("{}", if x == 0 { "Yes" } else { "No" });
}
