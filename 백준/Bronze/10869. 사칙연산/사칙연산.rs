use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let v: Vec<_> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    if let [a, b] = v[..] {
        println!("{}", a + b);
        println!("{}", a - b);
        println!("{}", a * b);
        println!("{}", a / b);
        println!("{}", a % b);
    }
}
