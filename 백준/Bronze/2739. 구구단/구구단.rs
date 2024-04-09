use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let n: i8 = buf.trim().parse().unwrap();

    for i in 1..=9 {
        println!("{} * {} = {}", n, i, n * i);
    }
}
