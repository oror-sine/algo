use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();

    let mut v: Vec<u16> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    v.sort();

    if let [a, b, c] = v[..] {
        let reward: u16 = match () {
            _ if a == b && b == c => 10_000 + c * 1_000,
            _ if a == b => 1_000 + a*100,
            _ if b == c => 1_000 + b*100,
            _ => c * 100,
        };
        print!("{}", reward);
    }
}
