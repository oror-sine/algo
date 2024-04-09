use std::{collections::BTreeSet, io::stdin};

fn main() {
    let mut set: BTreeSet<u8> = (1..=30).collect();
    for line in stdin().lines() {
        set.remove(&line.unwrap().trim().parse::<u8>().unwrap());
    }
    for i in set {
        println!("{}", i);
    }
}
