use std::fmt::Write;
use std::io::{stdin, Read};

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();

    let mut input = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<u32>().unwrap());

    let t = input.next().unwrap();
    let mut output = String::new();

    for _ in 0..t {
        writeln!(output, "{}", input.next().unwrap() + input.next().unwrap()).unwrap();
    }

    print!("{}", output);
}
