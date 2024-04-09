use std::io::stdin;

const ZERO_ASCII: u16 = '0' as u16;

fn main() {
    stdin().read_line(&mut String::new()).unwrap();
    for line in stdin().lines() {
        let ans: u16 = line.unwrap().chars().map(|x| (x as u16) - ZERO_ASCII).sum();
        print!("{}", ans);
    }
}
