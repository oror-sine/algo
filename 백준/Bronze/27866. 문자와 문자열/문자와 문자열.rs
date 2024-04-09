use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();

    let string: Vec<char> = buf.next().unwrap().chars().collect();
    let index: usize = buf.next().unwrap().parse().unwrap();

    print!("{}", string[index - 1]);
}
