use std::{fmt::Write, io::stdin};

fn main() {
    stdin().read_line(&mut String::new()).unwrap();

    let mut output = String::new();
    for line in stdin().lines() {
        let chars = line.unwrap().chars().collect::<Vec<_>>();
        writeln!(
            output,
            "{}{}",
            chars.first().unwrap(),
            chars.last().unwrap()
        )
        .unwrap();
    }
    print!("{}", output);
}
