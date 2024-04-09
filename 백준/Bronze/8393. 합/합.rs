use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let n: i32 = buf.trim().parse().unwrap();

    print!("{}", (n + 1) * n / 2);
}
