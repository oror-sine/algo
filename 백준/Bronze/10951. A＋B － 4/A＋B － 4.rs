use std::fmt::Write;
use std::io::stdin;

fn main() {
    let mut output = String::new();
    for line in stdin().lines() {
        writeln!(
            output,
            "{}",
            line.unwrap()
                .split_ascii_whitespace()
                .map(|x| x.parse::<u8>().unwrap())
                .sum::<u8>()
        )
        .unwrap();
    }
    print!("{}", output);
}
