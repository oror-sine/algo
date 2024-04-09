use std::{collections::BTreeMap, fmt::Write, io::stdin};

fn main() {
    let mut map: BTreeMap<char, i8> = ('a'..='z').zip([-1; 26]).collect();

    let mut output = String::new();
    for line in stdin().lines() {
        for (i, char) in line.unwrap().chars().enumerate() {
            if map[&char] == -1 {
                map.insert(char, i as i8);
            }
        }
    }
    for (_, value) in map {
        write!(output, "{} ", value).unwrap();
    }

    print!("{}", output.trim_end());
}
