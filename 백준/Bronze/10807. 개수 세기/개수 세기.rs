use std::{
    collections::HashMap,
    io::{stdin, Read},
};

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();

    let mut input = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i8>().unwrap());

    let mut counter: HashMap<i8, u8> = HashMap::new();
    let n = input.next().unwrap();

    for _ in 0..n {
        *counter.entry(input.next().unwrap()).or_default() += 1;
    }

    print!("{}", counter.entry(input.next().unwrap()).or_default());
}
