use std::io::stdin;

fn main() {
    let pieces = vec![1, 1, 2, 2, 2, 8];

    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let ans = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<i8>().unwrap())
        .enumerate()
        .map(|(i, e)| (pieces[i] - e).to_string())
        .collect::<Vec<_>>()
        .join(" ");

    print!("{}", ans);
}
