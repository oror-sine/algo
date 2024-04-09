use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();

    let v: Vec<i16> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    if let [mut a, mut b, c] = v[..] {
        b += c;
        a += b / 60;
        a %= 24;
        b %= 60;

        print!("{} {}", a, b);
    }
}