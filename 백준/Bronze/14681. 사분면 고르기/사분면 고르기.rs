use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();

    let v: Vec<i16> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    if let [x, y] = v[..] {
        let ans = match () {
            _ if x > 0 && y > 0 => 1,
            _ if x < 0 && y > 0 => 2,
            _ if x < 0 && y < 0 => 3,
            _ if x > 0 && y < 0 => 4,
            _ => panic!("x, y should not be 0."),
        };
        print!("{}", ans);
    } else {
        panic!("Number of inputs should be 2.");
    }
}
