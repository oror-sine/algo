use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let ans = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<f64>().unwrap())
        .reduce(|acc, e| acc / e)
        .unwrap();

    print!("{}", ans);
}
