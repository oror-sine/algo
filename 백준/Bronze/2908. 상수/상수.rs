use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let ans = buf
        .split_ascii_whitespace()
        .map(|x| x.chars().rev().collect::<String>().parse::<u16>().unwrap())
        .max()
        .unwrap();

    print!("{}", ans);
}
